"""A wandering cartoon challenges passersby to one simplified Hold'em hand."""

import random
from collections import Counter
from itertools import combinations

STARTING_MONEY = 1000
ANTE = 10
MIN_BET = 10
MAX_BET = 250
ENCOUNTER_CHANCE = 0.35

RANK_NAMES = {
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
}
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
SUIT_SYMBOLS = {
    "Hearts": "♥",
    "Diamonds": "♦",
    "Clubs": "♣",
    "Spades": "♠",
}
HAND_NAMES = [
    "high card",
    "one pair",
    "two pair",
    "three of a kind",
    "straight",
    "flush",
    "full house",
    "four of a kind",
    "straight flush",
]
CHALLENGERS = ["Milo the Mole", "Penny Possum", "Rex Raccoon", "Tilly Turtle"]
PLACES = [
    "a sunny meadow",
    "a creaky bridge",
    "the edge of a pond",
    "a patch of clover",
]


def make_deck():
    """Create and shuffle a standard 52-card deck."""
    deck = []
    for suit in SUITS:
        for rank in range(2, 15):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def show_card(card):
    """Turn a card tuple into compact text with a Unicode suit symbol."""
    rank, suit = card
    return f"{RANK_NAMES[rank]}{SUIT_SYMBOLS[suit]}"


def rank_five_cards(cards):
    """Return a comparable score for exactly five poker cards."""
    ranks = sorted((card[0] for card in cards), reverse=True)
    suits = [card[1] for card in cards]
    counts = Counter(ranks)
    groups = sorted(((count, rank) for rank, count in counts.items()), reverse=True)

    is_flush = len(set(suits)) == 1
    distinct_ranks = sorted(set(ranks), reverse=True)
    is_straight = False
    straight_high = 0

    if len(distinct_ranks) == 5:
        if distinct_ranks[0] - distinct_ranks[-1] == 4:
            is_straight = True
            straight_high = distinct_ranks[0]
        elif distinct_ranks == [14, 5, 4, 3, 2]:
            # In a wheel straight, the ace counts as low.
            is_straight = True
            straight_high = 5

    if is_straight and is_flush:
        return (8, straight_high)
    if groups[0][0] == 4:
        return (7, groups[0][1], groups[1][1])
    if groups[0][0] == 3 and groups[1][0] == 2:
        return (6, groups[0][1], groups[1][1])
    if is_flush:
        return (5, *ranks)
    if is_straight:
        return (4, straight_high)
    if groups[0][0] == 3:
        kickers = sorted((rank for rank in ranks if rank != groups[0][1]), reverse=True)
        return (3, groups[0][1], *kickers)
    if groups[0][0] == 2 and groups[1][0] == 2:
        high_pair = max(groups[0][1], groups[1][1])
        low_pair = min(groups[0][1], groups[1][1])
        kicker = next(rank for rank in ranks if rank != high_pair and rank != low_pair)
        return (2, high_pair, low_pair, kicker)
    if groups[0][0] == 2:
        pair_rank = groups[0][1]
        kickers = sorted((rank for rank in ranks if rank != pair_rank), reverse=True)
        return (1, pair_rank, *kickers)
    return (0, *ranks)


def rank_seven_cards(cards):
    """Find the best five-card poker hand from seven Hold'em cards."""
    return max(rank_five_cards(five_cards) for five_cards in combinations(cards, 5))


def describe_hand(score):
    """Give a short name to a hand score."""
    return HAND_NAMES[score[0]]


def show_cards(cards):
    return ", ".join(show_card(card) for card in cards)


def get_player_bet(money_available):
    """Ask for a bet, or return None if the player folds."""
    maximum = min(MAX_BET, money_available)
    while True:
        answer = (
            input(f"Choose a bet from ${MIN_BET} to ${maximum}, or type F to fold: ")
            .strip()
            .lower()
        )

        if answer == "f":
            return None

        try:
            bet = int(answer)
        except ValueError:
            print("Please enter a whole-dollar amount or F.")
            continue

        if MIN_BET <= bet <= maximum:
            return bet
        print(f"Your bet must be between ${MIN_BET} and ${maximum}.")


def computer_calls(bet, hole_cards):
    """Make a simple opponent decision using its private cards and bet size."""
    first_rank = hole_cards[0][0]
    second_rank = hole_cards[1][0]
    chance = 0.35

    if first_rank == second_rank:
        chance += 0.40
    if max(first_rank, second_rank) >= 12:
        chance += 0.15
    if min(first_rank, second_rank) >= 10:
        chance += 0.10
    if hole_cards[0][1] == hole_cards[1][1]:
        chance += 0.05

    # Large bets make the opponent less likely to call.
    chance -= bet / 500
    chance = max(0.05, min(chance, 0.95))
    return random.random() < chance


def play_hand(opponent, money):
    """Play one hand and return the player's updated bankroll."""
    print(f"\n{opponent} sits down for a hand of Texas Hold'em.")
    print(f"You both put in a ${ANTE} ante.")
    money -= ANTE

    deck = make_deck()
    player_cards = [deck.pop(), deck.pop()]
    computer_cards = [deck.pop(), deck.pop()]
    board = [deck.pop() for _ in range(5)]
    print(f"Your cards: {show_cards(player_cards)}")
    print(f"Community cards: {show_cards(board)}")

    bet = get_player_bet(money)
    if bet is None:
        print(f"You fold. {opponent} wins the ${ANTE * 2} ante pot.")
        return money

    money -= bet
    if not computer_calls(bet, computer_cards):
        # The opponent folds, so the pot contains both antes and your bet.
        winnings = ANTE * 2 + bet
        money += winnings
        print(f"{opponent} folds. You win ${winnings}.")
        return money

    print(f"{opponent} calls your ${bet} bet.")

    player_score = rank_seven_cards(player_cards + board)
    computer_score = rank_seven_cards(computer_cards + board)
    pot = ANTE * 2 + bet * 2

    print(f"Your best hand: {describe_hand(player_score)}")
    print(f"{opponent}'s cards: {show_cards(computer_cards)}")
    print(f"{opponent}'s best hand: {describe_hand(computer_score)}")

    if player_score > computer_score:
        money += pot
        print(f"You win the ${pot} pot!")
    elif player_score < computer_score:
        print(f"{opponent} wins the ${pot} pot.")
    else:
        money += pot // 2
        print(f"It's a tie. You split the ${pot} pot.")

    return money


def main():
    """Let the cartoon wander until the player quits or runs out of money."""
    money = STARTING_MONEY
    print("(^_^) Your cartoon wanderer is ready for a poker adventure!")
    print(f"Starting money: ${money}")
    print("Press Enter to take a random step, or type Q to quit.")

    while money >= ANTE + MIN_BET:
        command = input("\nNext step? ").strip().lower()
        if command == "q":
            break

        place = random.choice(PLACES)
        print(f"You wander into {place}.")

        if random.random() < ENCOUNTER_CHANCE:
            opponent = random.choice(CHALLENGERS)
            print(f"{opponent} challenges you to one hand!")
            answer = input("Accept the challenge? (y/n): ").strip().lower()
            if answer in ("y", "yes"):
                money = play_hand(opponent, money)
            else:
                print("You politely decline and keep wandering.")
        else:
            print("No challengers here. Your cartoon keeps wandering...")

        print(f"Money: ${money}")

    if money < ANTE + MIN_BET:
        print("You don't have enough money for the ante and minimum bet.")
        print("Your poker adventure is over.")
    else:
        print(f"You head home with ${money}. Thanks for playing!")


if __name__ == "__main__":
    main()
