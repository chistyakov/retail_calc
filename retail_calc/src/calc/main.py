#!/usr/bin/env python3

from calc.marshall import marshall_total_price
from calc.total_price import total_price
from calc.unmarshall import unmarshall_command_line_args

import logging

logger = logging.getLogger("retail_calc")


def main():
    args = unmarshall_command_line_args()
    total = total_price(
        quantity=args.quantity,
        unit_cost=args.unit_cost,
        state=args.state,
    )
    logger.info(marshall_total_price(total=total, verbose=args.verbose))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    main()
