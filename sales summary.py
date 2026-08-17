product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10

gross_sales = unit_price * quantity_sold
discount_amount = gross_sales * discount_percentage
final_sales = gross_sales - discount_amount

print(f"Product: {product_name}")
print(f"Gross sales: NPR {gross_sales:.2f}")
print(f"Discount: NPR {discount_amount:.2f}")
print(f"Final sales: NPR {final_sales:.2f}")