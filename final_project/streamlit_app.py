from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import streamlit as st

import data_store


PUMP_COST = 0.10
MAX_PUMPS = 10


@dataclass(frozen=True)
class CartItem:
    drink: str
    size: str
    milk: str
    flavor: str
    pumps: int
    quantity: int
    base_price: float
    pump_price: float
    total_price: float


def _as_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except Exception:
        return default


def _get_menu_lists(menu: dict[str, list[Any]]) -> tuple[list[str], list[str], list[str], list[str], list[float]]:
    coffees = [str(x) for x in menu.get("COFFEE", [])]
    sizes = [str(x) for x in menu.get("SIZES", [])]
    milks = [str(x) for x in menu.get("MILK", [])]
    flavors = [str(x) for x in menu.get("FLAVORS", [])]
    prices = [_as_float(x) for x in menu.get("PRICES", [])]
    return coffees, sizes, milks, flavors, prices


def _item_prices(size_index: int, prices: list[float], pumps: int, quantity: int) -> tuple[float, float, float]:
    base = prices[size_index] if 0 <= size_index < len(prices) else 0.0
    pump_price = float(pumps) * PUMP_COST
    total = (base + pump_price) * float(quantity)
    return float(base), float(pump_price), float(total)


def _ensure_state() -> None:
    if "employee_id" not in st.session_state:
        st.session_state.employee_id = None
    if "employee_confirmed" not in st.session_state:
        st.session_state.employee_confirmed = False
    if "cart" not in st.session_state:
        st.session_state.cart = []
    if "last_saved_order_id" not in st.session_state:
        st.session_state.last_saved_order_id = None


def _set_current_employee(employee_id: int) -> None:
    st.session_state.employee_id = employee_id
    st.session_state.employee_confirmed = True


def employees_tab() -> None:
    st.header("Employees")

    employees = data_store.load_employees()

    with st.form("employee_lookup"):
        employee_id_text = st.text_input("Employee number", value="")
        submitted = st.form_submit_button("Find / Create")

    if submitted:
        try:
            employee_id = int(employee_id_text.strip())
        except Exception:
            st.error("Employee number must be a whole number.")
            return

        st.session_state.employee_id = employee_id
        st.session_state.employee_confirmed = False

    employee_id = st.session_state.employee_id
    if employee_id is None:
        st.info("Enter an employee number to get started.")
        return

    employee_key = str(employee_id)
    existing = employees.get(employee_key)

    if existing is None:
        st.subheader(f"New employee #{employee_id}")
        with st.form("new_employee"):
            f_name = st.text_input("First name")
            l_name = st.text_input("Last name")
            office = st.text_input("Office")
            extension = st.text_input("Extension")
            allergies = st.text_input("Allergies (comma-separated)", value="")
            save_new = st.form_submit_button("Save employee")

        if save_new:
            employees[employee_key] = {
                "f_name": f_name.strip(),
                "l_name": l_name.strip(),
                "office": office.strip(),
                "extension": extension.strip(),
                "allergies": allergies.strip(),
            }
            data_store.save_employees(employees)
            _set_current_employee(employee_id)
            st.success("Employee saved and selected.")
        return

    st.subheader(f"Employee #{employee_id}")
    st.write("Confirm the information on file.")

    with st.form("confirm_employee"):
        f_name = st.text_input("First name", value=existing.get("f_name", ""))
        l_name = st.text_input("Last name", value=existing.get("l_name", ""))
        office = st.text_input("Office", value=existing.get("office", ""))
        extension = st.text_input("Extension", value=existing.get("extension", ""))
        allergies = st.text_input("Allergies (comma-separated)", value=existing.get("allergies", ""))

        col1, col2 = st.columns(2)
        with col1:
            confirm = st.form_submit_button("Confirm")
        with col2:
            update = st.form_submit_button("Update & Confirm")

    if confirm:
        _set_current_employee(employee_id)
        st.success("Employee confirmed.")

    if update:
        employees[employee_key] = {
            "f_name": f_name.strip(),
            "l_name": l_name.strip(),
            "office": office.strip(),
            "extension": extension.strip(),
            "allergies": allergies.strip(),
        }
        data_store.save_employees(employees)
        _set_current_employee(employee_id)
        st.success("Employee updated and confirmed.")

    with st.expander("View employee list"):
        if not employees:
            st.write("No employees saved yet.")
        else:
            st.dataframe(
                [
                    {"employee_id": k, **v}
                    for k, v in sorted(employees.items(), key=lambda kv: int(kv[0]) if kv[0].isdigit() else kv[0])
                ],
                hide_index=True,
            )


def order_tab() -> None:
    st.header("Order")

    if not st.session_state.employee_confirmed or st.session_state.employee_id is None:
        st.info("Go to the Employees tab and confirm an employee number first.")
        return

    menu = data_store.load_menu()
    coffees, sizes, milks, flavors, prices = _get_menu_lists(menu)

    if not coffees or not sizes or not milks or not flavors:
        st.error("Menu is missing. Update menu.json or menu.txt and refresh.")
        return

    with st.expander("Menu (for reference)", expanded=False):
        st.write({"COFFEE": coffees, "SIZES": sizes, "MILK": milks, "FLAVORS": flavors, "PRICES": prices})

    st.subheader("Add item")
    with st.form("add_item"):
        drink = st.selectbox("Drink", coffees)
        size = st.selectbox("Size", sizes)
        milk = st.selectbox("Milk", milks)
        flavor = st.selectbox("Flavor", flavors)
        pumps = st.number_input("Pumps", min_value=0, max_value=MAX_PUMPS, value=0, step=1)
        quantity = st.number_input("Quantity", min_value=1, max_value=20, value=1, step=1)
        add = st.form_submit_button("Add to order")

    if add:
        size_index = sizes.index(size) if size in sizes else 0
        base_price, pump_price, total_price = _item_prices(size_index, prices, int(pumps), int(quantity))
        st.session_state.cart.append(
            CartItem(
                drink=drink,
                size=size,
                milk=milk,
                flavor=flavor,
                pumps=int(pumps),
                quantity=int(quantity),
                base_price=base_price,
                pump_price=pump_price,
                total_price=total_price,
            )
        )
        st.success("Item added.")

    st.subheader("Current order")
    cart: list[CartItem] = st.session_state.cart
    if not cart:
        st.write("No items yet.")
        return

    rows = []
    grand_total = 0.0
    for i, item in enumerate(cart):
        grand_total += float(item.total_price)
        rows.append(
            {
                "#": i + 1,
                "drink": item.drink,
                "size": item.size,
                "milk": item.milk,
                "flavor": item.flavor,
                "pumps": item.pumps,
                "qty": item.quantity,
                "item_total": f"${item.total_price:.2f}",
            }
        )

    st.dataframe(rows, hide_index=True, use_container_width=True)
    st.write(f"Total: ${grand_total:.2f}")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Remove last item"):
            st.session_state.cart = cart[:-1]
            st.rerun()
    with col2:
        if st.button("Clear order"):
            st.session_state.cart = []
            st.rerun()
    with col3:
        confirm = st.button("Confirm & save order", type="primary")

    if confirm:
        orders = data_store.load_orders()
        order_id = data_store.next_order_id(orders)

        order = {
            "order_id": order_id,
            "employee_id": int(st.session_state.employee_id),
            "timestamp": data_store.now_iso(),
            "items": [item.__dict__ for item in cart],
            "total_price": float(grand_total),
        }

        orders.append(order)
        data_store.save_orders(orders)

        st.session_state.last_saved_order_id = order_id
        st.session_state.cart = []
        st.success(f"Order #{order_id} saved.")


def history_tab() -> None:
    st.header("Order History")

    if st.session_state.employee_id is None:
        st.info("Enter an employee number in the Employees tab first.")
        return

    employee_id = int(st.session_state.employee_id)
    orders = data_store.load_orders()

    employee_orders = [o for o in orders if int(o.get("employee_id", -1) or -1) == employee_id]
    employee_orders.sort(key=lambda o: str(o.get("timestamp", "")), reverse=True)

    if not employee_orders:
        st.write("No orders found for this employee yet.")
        return

    st.write(f"Showing orders for employee #{employee_id}.")

    for order in employee_orders:
        order_id = order.get("order_id", "")
        timestamp = order.get("timestamp", "")
        total = _as_float(order.get("total_price", 0))

        with st.expander(f"Order #{order_id} — {timestamp} — ${total:.2f}"):
            items = order.get("items", [])
            if isinstance(items, list):
                st.dataframe(
                    [
                        {
                            "drink": str(i.get("drink", "")),
                            "size": str(i.get("size", "")),
                            "milk": str(i.get("milk", "")),
                            "flavor": str(i.get("flavor", "")),
                            "pumps": int(i.get("pumps", 0) or 0),
                            "qty": int(i.get("quantity", 1) or 1),
                            "item_total": f"${_as_float(i.get('total_price', 0)):.2f}",
                        }
                        for i in items
                        if isinstance(i, dict)
                    ],
                    hide_index=True,
                    use_container_width=True,
                )

            if st.button(f"Re-order this order", key=f"reorder_{order_id}"):
                cart: list[CartItem] = []
                for i in items if isinstance(items, list) else []:
                    if not isinstance(i, dict):
                        continue
                    cart.append(
                        CartItem(
                            drink=str(i.get("drink", "")),
                            size=str(i.get("size", "")),
                            milk=str(i.get("milk", "")),
                            flavor=str(i.get("flavor", "")),
                            pumps=int(i.get("pumps", 0) or 0),
                            quantity=int(i.get("quantity", 1) or 1),
                            base_price=_as_float(i.get("base_price", 0)),
                            pump_price=_as_float(i.get("pump_price", 0)),
                            total_price=_as_float(i.get("total_price", 0)),
                        )
                    )
                st.session_state.cart = cart
                st.success("Loaded items into Current order. Go to the Order tab to confirm & save.")


def main() -> None:
    st.set_page_config(page_title="Coffee Ordering System", layout="wide")
    _ensure_state()
    data_store.ensure_json_files()

    st.title("Coffee Ordering System")

    if st.session_state.employee_confirmed and st.session_state.employee_id is not None:
        st.caption(f"Current employee: #{st.session_state.employee_id}")
    else:
        st.caption("No employee selected yet.")

    tab_employees, tab_order, tab_history = st.tabs(["Employees", "Order", "Order History"])
    with tab_employees:
        employees_tab()
    with tab_order:
        order_tab()
    with tab_history:
        history_tab()


if __name__ == "__main__":
    main()

