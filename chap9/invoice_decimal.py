from decimal import Decimal
from decimal import ROUND_HALF_UP

choice = "y"
while choice == "y":

    # get the user entry
    order_total = Decimal(input("Enter order total:     "))
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print()

    # determine the discount percent
    if order_total > 0 and order_total < 100:
        discount_precent = Decimal("0")
    elif order_total >= 100 and order_total < 250:
        discount_precent = Decimal(".1")
    elif order_total >= 250:
        discount_precent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_precent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)
    subtotal = order_total - discount
    tax_percent = Decimal(".05")
    sales_tax = subtotal * tax_percent
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)
    invoice_total = subtotal + sales_tax

    # display the results
    print("Order total:         {:10,}".format(order_total))
    print("Discount amount:     {:10,}".format(discount))
    print("Subtotal:            {:10,}".format(subtotal))
    print("Sales tax:           {:10,}".format(sales_tax))
    print("Invoice total:       {:10,}".format(invoice_total))

    choice = input("Continue? (y/n): ")
    print()

print("Bye")