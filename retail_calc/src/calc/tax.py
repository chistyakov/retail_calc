from decimal import Decimal

TAX_FACTOR_PER_STATE = {
    "UT": Decimal("0.0685"),
    "NV": Decimal("0.08"),
    "TX": Decimal("0.0625"),
    "AL": Decimal("0.04"),
    "CA": Decimal("0.0825"),
}


def get_tax_factor(state: str) -> Decimal:
    try:
        return TAX_FACTOR_PER_STATE[state]
    except KeyError:
        raise ValueError(f"Supported states: {list(TAX_FACTOR_PER_STATE)}")
