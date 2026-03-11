#!/usr/bin/env python3
"""LED Wall Install Calculator for The Villages - WC 2026"""

import sys

# Defaults
DEFAULT_RENTAL_DAYS = 60
DEFAULT_RENTAL_RATE_PER_SQFT = 10  # $/sqft/day
DEFAULT_SHIPPING = 13500

def calculate(screens, rental_days=DEFAULT_RENTAL_DAYS, shipping=DEFAULT_SHIPPING):
    """
    Calculate LED wall install numbers.

    screens: list of dicts with keys:
        - name: str (location description)
        - width: float (actual width in ft)
        - height: float (actual height in ft)
        - qty: int (number of panels)
        - cost: float (total cost for this line item)
        - panel_spec: str (e.g. 'P2.6')
        - mount_type: str (e.g. 'Wall Mount')
    """
    results = []
    total_area = 0
    total_cost = 0

    print("=" * 80)
    print("LED WALL INSTALL — COST BREAKDOWN")
    print("=" * 80)
    print()

    for i, s in enumerate(screens, 1):
        area = s["width"] * s["height"] * s["qty"]
        cost_per_sqft = s["cost"] / area if area > 0 else 0
        daily_rental = area * DEFAULT_RENTAL_RATE_PER_SQFT

        total_area += area
        total_cost += s["cost"]

        results.append({**s, "area": area, "cost_per_sqft": cost_per_sqft, "daily_rental": daily_rental})

        print(f"  {i}. {s['name']}")
        print(f"     {s.get('panel_spec', '')} | {s['width']}ft × {s['height']}ft | Qty: {s['qty']} | {s.get('mount_type', '')}")
        print(f"     Area: {area:,.2f} sqft | Cost: ${s['cost']:,.2f} | Cost/sqft: ${cost_per_sqft:,.2f} | Daily Rental: ${daily_rental:,.2f}")
        print()

    # Summary
    subtotal = total_cost
    grand_total = subtotal + shipping
    avg_cost_per_sqft = grand_total / total_area if total_area > 0 else 0
    total_daily_rental = total_area * DEFAULT_RENTAL_RATE_PER_SQFT
    total_rental = total_daily_rental * rental_days

    purchase_price = grand_total * 2
    deposit = purchase_price * 0.50
    installment = deposit * 0.50

    print("-" * 80)
    print(f"  {'Sub Total:':<30} ${subtotal:>12,.2f}")
    print(f"  {'Shipping:':<30} ${shipping:>12,.2f}")
    print(f"  {'Total:':<30} ${grand_total:>12,.2f}")
    print(f"  {'Total Area:':<30} {total_area:>12,.2f} sqft")
    print(f"  {'Avg Cost/sqft:':<30} ${avg_cost_per_sqft:>12,.2f}")
    print()
    print(f"  {'Daily Rental Rate:':<30} ${total_daily_rental:>12,.2f} /day")
    print(f"  {'Rental Period:':<30} {rental_days:>12} days")
    print(f"  {'Total Rental:':<30} ${total_rental:>12,.2f}")
    print()
    print(f"  {'Purchase Price (2x):':<30} ${purchase_price:>12,.2f}")
    print(f"  {'Deposit (50%):':<30} ${deposit:>12,.2f}")
    print(f"  {'1st Installment (25%):':<30} ${installment:>12,.2f}")
    print(f"  {'2nd Installment (25%):':<30} ${installment:>12,.2f}")
    print("=" * 80)

    return results


# ── Current inventory ──────────────────────────────────────────────────────────
CURRENT_SCREENS = [
    {"name": "MAIN FLOOR SEC 1 - Front Wall",          "width": 8.2,   "height": 4.92,  "qty": 1, "cost": 7895.75,  "panel_spec": "P1.5", "mount_type": "Wall Mount"},
    {"name": "MAIN FLOOR SEC 1 - Back Wall",            "width": 8.2,   "height": 9.34,  "qty": 1, "cost": 8404.00,  "panel_spec": "P2.6", "mount_type": "Wall Mount"},
    {"name": "MAIN FLOOR SEC 2 - Around the Bar Area",  "width": 24.61, "height": 3.28,  "qty": 3, "cost": 8514.00,  "panel_spec": "P2.6", "mount_type": "Wall Mount"},
    {"name": "MAIN FLOOR SEC 2 - Window Side",          "width": 24.61, "height": 4.1,   "qty": 1, "cost": 9986.64,  "panel_spec": "P2.6", "mount_type": "Wall Mount"},
    {"name": "MAIN FLOOR SEC 2 - Behind Bar / Hallway", "width": 18.04, "height": 4.92,  "qty": 1, "cost": 9060.00,  "panel_spec": "P2.6", "mount_type": "Wall Mount"},
    {"name": "MAIN FLOOR SEC 3 - Exterior Wall",        "width": 8.2,   "height": 4.92,  "qty": 1, "cost": 7895.75,  "panel_spec": "P1.5", "mount_type": "Wall Mount"},
    {"name": "MAIN FLOOR SEC 3 - Over Booths",          "width": 8.2,   "height": 4.92,  "qty": 1, "cost": 8322.75,  "panel_spec": "P1.5", "mount_type": "Hanging Rental Style"},
    {"name": "MAIN FLOOR SEC 4 - Full Wall by Entrance", "width": 9.84, "height": 8.2,   "qty": 1, "cost": 8404.00,  "panel_spec": "P2.6", "mount_type": "Wall Mount"},
    {"name": "MAIN FLOOR SEC 4 - Over Interior Wall",   "width": 41.01, "height": 4.92,  "qty": 1, "cost": 18099.00, "panel_spec": "P2.6", "mount_type": "Wall Mount"},
    {"name": "2ND FLOOR VIP - Glass Wall",              "width": 13.12, "height": 8.2,   "qty": 1, "cost": 11682.00, "panel_spec": "P2.6", "mount_type": "Hanging Rental Style"},
    {"name": "OUTDOOR PATIO - Between Posts",            "width": 8.2,   "height": 4.92,  "qty": 4, "cost": 30511.00, "panel_spec": "P2.9", "mount_type": "Hanging Rental Style"},
    {"name": "OUTDOOR - Rear Parking",                   "width": 14.76, "height": 8.2,   "qty": 1, "cost": 13784.75, "panel_spec": "P3.9", "mount_type": ""},
]


if __name__ == "__main__":
    days = DEFAULT_RENTAL_DAYS
    if len(sys.argv) > 1:
        try:
            days = int(sys.argv[1])
        except ValueError:
            print(f"Usage: {sys.argv[0]} [rental_days]  (default: {DEFAULT_RENTAL_DAYS})")
            sys.exit(1)

    calculate(CURRENT_SCREENS, rental_days=days)
