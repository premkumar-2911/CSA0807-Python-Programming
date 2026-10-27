
from decimal import Decimal, InvalidOperation

# Named constants
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")

# Read farmer details
farmer_id = input("Enter farmer ID: ").strip()
litres_text = input("Enter milk quantity in litres: ")
fat_text = input("Enter fat percentage: ")
snf_text = input("Enter SNF percentage: ")
shift = input("Enter shift (Morning/Evening): ").strip().title()

# Check farmer ID
if farmer_id == "":
    print("Invalid: Farmer ID cannot be empty.")

else:
    # Check numeric values
    try:
        litres = Decimal(litres_text)
        fat = Decimal(fat_text)
        snf = Decimal(snf_text)

        if not litres.is_finite() or not fat.is_finite() or not snf.is_finite():
            print("Invalid: Enter finite numeric values.")

        elif litres <= 0:
            print("Invalid: Milk quantity must be greater than zero.")

        elif not MIN_FAT <= fat <= MAX_FAT:
            print("Invalid: Fat must be between 2.0% and 7.0%.")

        elif snf <= 0:
            print("Invalid: SNF must be greater than zero.")

        elif shift not in ("Morning", "Evening"):
            print("Invalid: Shift must be Morning or Evening.")

        else:
            print("\nFarmer entry accepted!")
            print("Farmer ID:", farmer_id)
            print("Milk quantity:", litres, "litres")
            print("Fat percentage:", fat, "%")
            print("SNF percentage:", snf, "%")
            print("Shift:", shift)

    except InvalidOperation:
        print("Invalid: Quantity, fat, and SNF must be numeric.")
