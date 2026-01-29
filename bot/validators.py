def validate_symbol(symbol: str) -> str:
    """Validates that symbol is a non-empty string."""
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string.")
    return symbol.upper()

def validate_side(side: str) -> str:
    """Validates that side is either BUY or SELL."""
    if side.upper() not in ['BUY', 'SELL']:
        raise ValueError("Side must be 'BUY' or 'SELL'.")
    return side.upper()

def validate_order_type(order_type: str) -> str:
    """Validates that order_type is either MARKET or LIMIT."""
    if order_type.upper() not in ['MARKET', 'LIMIT']:
        raise ValueError("Order type must be 'MARKET' or 'LIMIT'.")
    return order_type.upper()

def validate_quantity(quantity: float) -> float:
    """Validates that quantity is a positive number."""
    try:
        qty = float(quantity)
    except ValueError:
        raise ValueError("Quantity must be a number.")
    
    if qty <= 0:
        raise ValueError("Quantity must be greater than 0.")
    return qty

def validate_price(price: float) -> float:
    """Validates that price is a positive number."""
    try:
        p = float(price)
    except ValueError:
        raise ValueError("Price must be a number.")
        
    if p <= 0:
        raise ValueError("Price must be greater than 0.")
    return p
