# Task from job interview
Tom, an owner of small grocery stores with fixed prices from America, asked for help.

Last year, Tom opened his own business in a small town and so far he has to do everything himself (he does not trust anyone from the locals, and his kinsfolk is far away), including sitting at the checkout. Now he calculates the cost of the order manually, which is very inconvenient, since he needs to take into account state taxes and a discounts.

The situation is complicated by the fact that Tom recently expanded into other states (his kinsfolk lives there), and now he needs to take into account the taxes of other states in his calculations.

After a little thought, he came to the conclusion that he needs an application with a simple user interface, 3 input fields and 1 output field for the total price.
“Tom's Retail Calculator,” as Tom called it.

Finished Product - Retail Calculator of Tom

3 input fields:
* Quantity of goods.
* Cost of good.
* State code.

Output field:
* Total price

How should it work:
* The discount is calculated based on costs and the discounted price is displayed.
* State tax is then added based on the state code and discounted price, and the total price including discount and total price with tax is displayed

| Price without tax, USD | Discount, % |
| ---------------------- |:-----------:|
| \>= 1000               | 3           |
| \>= 5000               | 5           |
| \>= 7000               | 7           |
| \>= 10000              | 10          |
| \>= 50000              | 15          |

| State code | Tax rate |
| ---------- |:--------:|
| UT         | 6.85     |
| TX         | 6.25     |
| NV         | 8        |
| AL         | 4        |
| CA         | 8.25     |


For code stability control, write Unit tests


## How to run
```shell
make calc QUANTITY=10000 UNITY_COST=2.00 STATE=AL VERBOSE=true

# run tests:
make tests

# static check of code:
make static_check
```