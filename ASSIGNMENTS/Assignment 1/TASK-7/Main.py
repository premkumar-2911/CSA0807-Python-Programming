
from decimal import Decimal, InvalidOperation
import milkrate

print("VILLAGE MILK CO-OPERATIVE")
print("-------------------------")

farmer_id = input("Enter farmer ID: ").strip()
litres_text = input("Enter milk quantity in litres: ")
fat_text = input("Enter fat percentage: ")
snf_text = input("Enter SNF percentage: ")

try:
    litres = Decimal(litres_text)
    fat = Decimal(fat_text)
    snf = Decimal(snf_text)

    if not farmer_id:
        print("Error: Farmer ID cannot be empty.")

    elif not all(value.is_finite() for value in (litres, fat, snf)):
        print("Error: Values must be finite numbers.")

    elif litres <= 0 or snf <= 0:
        print("Error: Litres and SNF must be positive.")

    else:
        rate = milkrate.calculate_rate(fat, snf)
        payment = milkrate.calculate_payment(litres, rate)

        print("\nFarmer ID:", farmer_id)
        print("Rate per litre: Rs.", rate)
        print("Total payment: Rs.", payment)

except InvalidOperation:
    print("Error: Enter valid numeric values.")
