from decimal import Decimal

TAX_FACTOR_PER_STATE_CODE = {
    "UT": Decimal("0.0685"),
    "NV": Decimal("0.08"),
    "TX": Decimal("0.0625"),
    "AL": Decimal("0.04"),
    "CA": Decimal("0.0825"),
}


def get_tax_factor(state_code: str) -> Decimal:
    try:
        return TAX_FACTOR_PER_STATE_CODE[state_code]
    except KeyError:
        raise ValueError(
            f"Unsupported state code. Options: {list(TAX_FACTOR_PER_STATE_CODE)}"
        )
