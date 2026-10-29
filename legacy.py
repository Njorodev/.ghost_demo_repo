"""Historical billing helpers from the demo archive."""

def calculate_legacy_total(items, tax_rate=0.16):
    """Calculate a total using the old inclusive-tax rule."""
    subtotal = sum(item["price"] * item["quantity"] for item in items)
    return round(subtotal * (1 + tax_rate), 2)

def format_receipt(total):
    return f"LEGACY TOTAL: {total:.2f}"
