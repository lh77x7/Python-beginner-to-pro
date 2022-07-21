#!/usr/bin/env python3

# display a welome message
print("The Invoice program")
print()

# get user entries
customer_type = input("Enter customer type (r/w):\t")
invoice_total = float(input("Enter invoice total:\t\t"))
print()

# determine discounts for retail customers
if customer_type.lower() == "r":
    if invoice_total > 0 and invoice_total < 100:
        discount_procent = 0
    elif invoice_total >= 100 and invoice_total < 250:
        discount_procent = .1
    elif invoice_total >= 250 and invoice_total < 500:
        discount_procent = .2
    elif invoice_total >= 500:
        discount_procent = .25
# determine discounts for Wholesale customers
elif customer_type.lower() == "w":
    if invoice_total > 0 and invoice_total < 500:
        discount_procent = .4
    elif invoice_total >= 500:
        discount_procent = .5
# set discount to zero if neither Retail or Wholesale
else:
    discount_procent = 0

# calculate discount amount and new invoice total
discount_amount = round(invoice_total * discount_procent, 2)
new_invoice_total = invoice_total - discount_amount

# display the results
print("Invoice total:\t\t" + str(invoice_total))
print("Discount procent:\t" + str(discount_procent))
print("Discount amount:\t" 
+ str(discount_amount))
print("New invoice total:\t" + str(new_invoice_total))
print()
print("Bye")