from calc.convert import decimal_to_str
from calc.total_price import TotalPrice


def marshall_total_price(total: TotalPrice, verbose: bool = False) -> str:
    if not verbose:
        return decimal_to_str(total.price)

    try:
        return (
            f"Total price without tax: {decimal_to_str(total.price_without_tax)} USD\n"
            f"Total price: {decimal_to_str(total.price)} USD"
        )
    except ValueError:
        return "Failed to count"
