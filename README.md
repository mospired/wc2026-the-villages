# WC 2026 — The Villages LED Screen Inventory

LED wall installation project for The Villages venue, World Cup 2026.

## How the Math Works

### Per Screen

Each screen entry has an **actual width** and **actual height** (in feet), a **quantity**, and a **cost** from the vendor.

```
Area (sqft)   = Actual Width × Actual Height × Qty
Cost / Sqft   = Cost ÷ Area
```

### Rental Rate

The daily rental rate is based on total square footage across all screens:

```
Daily Rental Rate  = Total Area (sqft) × $10/sqft
Total Rental       = Daily Rental Rate × Rental Days (default: 60)
```

### Purchase Price

Purchase price is calculated as 2× the total cost (including shipping):

```
Sub Total       = Sum of all screen costs
Total           = Sub Total + Shipping ($13,500)
Purchase Price  = Total × 2
```

### Payment Schedule

```
Deposit            = Purchase Price × 50%
1st Installment    = Deposit × 50%   (25% of Purchase Price)
2nd Installment    = Deposit × 50%   (25% of Purchase Price)
```

## Calculator Script

`led_calculator.py` automates all calculations above.

```bash
# Run with default 60-day rental period
python3 led_calculator.py

# Run with custom rental period
python3 led_calculator.py 90
```

To calculate for a subset of screens, edit the `CURRENT_SCREENS` list in the script or import and call `calculate()` directly:

```python
from led_calculator import calculate

screens = [
    {"name": "My Screen", "width": 8.2, "height": 4.92, "qty": 1,
     "cost": 7895.75, "panel_spec": "P2.6", "mount_type": "Wall Mount"},
]

calculate(screens, rental_days=60, shipping=13500)
```

## File Structure

- `spreadsheets/` — Excel inventory files (.xlsx)
- `pdfs/` — PDF documents
- `presentations/` — PowerPoint files (.pptx)
- `screenshots/` — Screenshot images
- `led_calculator.py` — Cost/rental calculator script
