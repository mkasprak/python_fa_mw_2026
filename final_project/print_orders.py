"""
Printing helpers (label + optional receipt).

🧠 Original student work:
- Started a `print_label()` stub and a basic "Would you like a receipt?" prompt.

✅ Completed by Codex (2026-11-11):
- 🖨️ `print_label()` now prints real employee + order details passed in from `main.py`.
- 💾 Receipt saving to `final_project/receipts/receipt_<order_id>.txt`.
"""

from __future__ import annotations

import datetime
from pathlib import Path
from typing import Any

_BASE_DIR = Path(__file__).resolve().parent
_RECEIPT_DIR = _BASE_DIR / "receipts"
_ERROR_FILE = _BASE_DIR / "error.txt"


def _log_error(e: Exception) -> None:
    # 🛡️ Safety: keep a simple local error log instead of crashing the whole program.
    right_now = datetime.datetime.now()
    try:
        with open(_ERROR_FILE, "a", encoding="utf-8") as f:
            f.write(f"{right_now}: {type(e).__name__}: {e}\n")
    except Exception:
        pass


def _format_label(order: dict[str, Any], employee_id: int, employee: dict[str, Any]) -> str:
    # 🖨️ Display formatting for the label/receipt.
    # ℹ️ Codex note: build the output as a list of individual lines first.
    # - Each item in `lines` is ONE line of text.
    # - Blank lines are just "".
    # This makes it easy to edit the label without worrying about newline characters everywhere.
    lines = [
        "Coffee Order Label",
        "------------------",
        f"Order ID:   {order.get('order_id', '')}",
        f"Employee:   {employee.get('f_name','')} {employee.get('l_name','')} (ID {employee_id})",
        f"Office:     {employee.get('office','')}",
        f"Extension:  {employee.get('extension','')}",
        f"Allergies:  {employee.get('allergies','')}",
        "",
        f"Drink:      {order.get('drink','')}",
        f"Size:       {order.get('size','')}  (${order.get('base_price', 0):.2f})",
        f"Milk:       {order.get('milk','')}",
        f"Flavor:     {order.get('flavor','')}",
        f"Pumps:      {order.get('pumps', 0)}  (${order.get('pump_price', 0):.2f})",
        "",
        f"Total:      ${order.get('total_price', 0):.2f}",
        f"Timestamp:  {order.get('timestamp','')}",
    ]
    # ℹ️ `"\\n".join(lines)` combines the list into ONE multi-line string.
    # Example:
    #   ["A", "B", "C"]  ->  "A\\nB\\nC"
    # Why we do it: `print(...)` and `f.write(...)` both want a single string.
    return "\n".join(lines)


def print_label(order: dict[str, Any], employee_id: int, employee: dict[str, Any]) -> None:
    # 🖨️ Print the label to the console.
    print()
    print(_format_label(order, employee_id, employee))
    print()


def maybe_print_receipt(order: dict[str, Any], employee_id: int, employee: dict[str, Any]) -> Path | None:
    # 🧠 Ask whether to save a receipt; returns the path if saved.
    receipt = input("Would you like a receipt saved to a file (y/n)?  ").strip().lower()
    if receipt != "y":
        return None

    try:
        _RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
        order_id = order.get("order_id", "unknown")
        receipt_path = _RECEIPT_DIR / f"receipt_{order_id}.txt"
        with open(receipt_path, "w", encoding="utf-8") as f:
            f.write(_format_label(order, employee_id, employee))
            f.write("\n")
        return receipt_path
    except Exception as e:
        _log_error(e)
        return None
