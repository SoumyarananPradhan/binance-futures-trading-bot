def validate_symbol(symbol: str) -> str:
    """
    Ensures the symbol is alphanumeric and returns it in uppercase.
    """
    if not symbol.isalnum():
        raise ValueError(f"Invalid symbol '{symbol}'. Symbol must be alphanumeric (e.g., BTCUSDT).")
    return symbol.upper()

def validate_side(side: str) -> str:
    """
    Ensures the order side is strictly BUY or SELL.
    """
    side_upper = side.upper()
    if side_upper not in ['BUY', 'SELL']:
        raise ValueError(f"Invalid side '{side}'. Side must be 'BUY' or 'SELL'.")
    return side_upper

def validate_order_type(order_type: str) -> str:
    """
    Ensures the order type is supported (MARKET or LIMIT).
    """
    type_upper = order_type.upper()
    if type_upper not in ['MARKET', 'LIMIT']:
        raise ValueError(f"Invalid order type '{order_type}'. Type must be 'MARKET' or 'LIMIT'.")
    return type_upper

def validate_quantity(quantity: float) -> float:
    """
    Ensures the quantity is a positive number.
    """
    if quantity <= 0:
        raise ValueError(f"Invalid quantity {quantity}. Quantity must be greater than zero.")
    return quantity

def validate_price(order_type: str, price: float = None) -> float:
    """
    Ensures a valid price is provided if the order type is LIMIT.
    """
    if order_type.upper() == 'LIMIT':
        if price is None or price <= 0:
            raise ValueError("A valid price greater than zero is strictly required for LIMIT orders.")
    return price