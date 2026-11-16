from __future__ import annotations

import ast
import json
from datetime import datetime
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent

EMPLOYEES_JSON = BASE_DIR / "employees.json"
MENU_JSON = BASE_DIR / "menu.json"
ORDERS_JSON = BASE_DIR / "orders.json"

LEGACY_EMPLOYEES_TXT = BASE_DIR / "employees.txt"
LEGACY_MENU_TXT = BASE_DIR / "menu.txt"
LEGACY_ORDERS_TXT = BASE_DIR / "orders.txt"


def _load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _save_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def _parse_legacy_employees() -> dict[str, dict[str, str]]:
    employees: dict[str, dict[str, str]] = {}
    if not LEGACY_EMPLOYEES_TXT.exists():
        return employees

    for raw_line in LEGACY_EMPLOYEES_TXT.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            continue
        employee_id_text, record_text = line.split(":", 1)
        employee_id_text = employee_id_text.strip()
        record_text = record_text.strip()
        try:
            record = ast.literal_eval(record_text)
        except Exception:
            continue
        if not isinstance(record, dict):
            continue
        employees[employee_id_text] = {
            "f_name": str(record.get("f_name", "")).strip(),
            "l_name": str(record.get("l_name", "")).strip(),
            "office": str(record.get("office", "")).strip(),
            "extension": str(record.get("extension", "")).strip(),
            "allergies": str(record.get("allergies", "")).strip(),
        }

    return employees


def _parse_legacy_menu() -> dict[str, list[Any]]:
    menu: dict[str, list[Any]] = {}
    if not LEGACY_MENU_TXT.exists():
        return menu

    for raw_line in LEGACY_MENU_TXT.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or ":" not in line:
            continue
        category, detail = line.split(":", 1)
        category = category.strip().upper()
        detail = detail.strip()
        parts = [p.strip() for p in detail.split(",") if p.strip()]
        if category == "PRICES":
            prices: list[float] = []
            for p in parts:
                try:
                    prices.append(float(p))
                except Exception:
                    continue
            menu[category] = prices
        else:
            menu[category] = parts

    return menu


def _parse_legacy_orders() -> list[dict[str, Any]]:
    orders: list[dict[str, Any]] = []
    if not LEGACY_ORDERS_TXT.exists():
        return orders

    for raw_line in LEGACY_ORDERS_TXT.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        try:
            old = ast.literal_eval(line)
        except Exception:
            continue
        if not isinstance(old, dict):
            continue

        item = {
            "drink": old.get("drink", ""),
            "size": old.get("size", ""),
            "milk": old.get("milk", ""),
            "flavor": old.get("flavor", ""),
            "pumps": int(old.get("pumps", 0) or 0),
            "quantity": 1,
            "base_price": float(old.get("base_price", 0) or 0),
            "pump_price": float(old.get("pump_price", 0) or 0),
            "total_price": float(old.get("total_price", 0) or 0),
        }
        orders.append(
            {
                "order_id": int(old.get("order_id", 0) or 0),
                "employee_id": int(old.get("employee_id", 0) or 0),
                "timestamp": old.get("timestamp", ""),
                "items": [item],
                "total_price": float(old.get("total_price", 0) or 0),
            }
        )

    return orders


def ensure_json_files() -> None:
    if not EMPLOYEES_JSON.exists():
        _save_json(EMPLOYEES_JSON, _parse_legacy_employees())

    if not MENU_JSON.exists():
        menu = _parse_legacy_menu()
        if not menu:
            menu = {
                "COFFEE": ["Drip", "Americano", "Latte"],
                "SIZES": ["Small", "Medium", "Large"],
                "MILK": ["Whole", "2%", "Skim", "Oat", "Soy", "None"],
                "FLAVORS": ["Vanilla", "Caramel", "Chocolate", "None"],
                "PRICES": [4.0, 5.0, 6.0],
            }
        _save_json(MENU_JSON, menu)

    if not ORDERS_JSON.exists():
        _save_json(ORDERS_JSON, _parse_legacy_orders())


def load_employees() -> dict[str, dict[str, str]]:
    ensure_json_files()
    value = _load_json(EMPLOYEES_JSON, {})
    if isinstance(value, dict):
        cleaned: dict[str, dict[str, str]] = {}
        for k, v in value.items():
            if isinstance(k, str) and isinstance(v, dict):
                cleaned[k] = {
                    "f_name": str(v.get("f_name", "")).strip(),
                    "l_name": str(v.get("l_name", "")).strip(),
                    "office": str(v.get("office", "")).strip(),
                    "extension": str(v.get("extension", "")).strip(),
                    "allergies": str(v.get("allergies", "")).strip(),
                }
        return cleaned
    return {}


def save_employees(employees: dict[str, dict[str, str]]) -> None:
    ensure_json_files()
    _save_json(EMPLOYEES_JSON, employees)


def load_menu() -> dict[str, list[Any]]:
    ensure_json_files()
    value = _load_json(MENU_JSON, {})
    if not isinstance(value, dict):
        return {}
    menu: dict[str, list[Any]] = {}
    for k, v in value.items():
        if isinstance(k, str) and isinstance(v, list):
            menu[k.upper()] = v
    return menu


def save_menu(menu: dict[str, list[Any]]) -> None:
    ensure_json_files()
    _save_json(MENU_JSON, menu)


def load_orders() -> list[dict[str, Any]]:
    ensure_json_files()
    value = _load_json(ORDERS_JSON, [])
    if isinstance(value, list):
        return [o for o in value if isinstance(o, dict)]
    return []


def save_orders(orders: list[dict[str, Any]]) -> None:
    ensure_json_files()
    _save_json(ORDERS_JSON, orders)


def next_order_id(orders: list[dict[str, Any]]) -> int:
    max_id = 0
    for order in orders:
        try:
            max_id = max(max_id, int(order.get("order_id", 0)))
        except Exception:
            continue
    return max_id + 1


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")

