
from decimal import Decimal, InvalidOperation

# Named constants
BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
FAT_ADJUSTMENT = Decimal("0.40")
SNF_ADJUSTMENT = Decimal("0.30")
STEP = Decimal("0.1")
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")


# Function to validate farmer details
def validate_entry(farmer_id, litres, fat, snf, shift):
    return (
        bool(farmer_id.strip())
        and litres.is_finite()
        and fat.is_finite()
        and snf.is_finite()
        and litres > 0
        and MIN_FAT <= fat <= MAX_FAT
        and snf > 0
        and shift in ("Morning", "Evening")
    )


# Function to calculate the rate per litre
def calculate_rate(fat, snf):
    fat_difference = (fat - STANDARD_FAT) / STEP
    snf_difference = (snf - STANDARD_SNF) / STEP

    fat_amount = fat_difference * FAT_ADJUSTMENT
    snf_amount = snf_difference * SNF_ADJUSTMENT

    return BASE_RATE + fat_amount + snf_amount


# Function to calculate the total payment
def calculate_payment(litres, rate):
    return litres * rate


# Main program
farmer_id = input("Enter farmer ID: ").strip()
shift = input("Enter shift (Morning/Evening): ").strip().title()

try:
    litres = Decimal(input("Enter milk quantity in litres: "))
    fat = Decimal(input("Enter fat percentage: "))
    snf = Decimal(input("Enter SNF percentage: "))

    if validate_entry(farmer_id, litres, fat, snf, shift):
        rate = calculate_rate(fat, snf)
        payment = calculate_payment(litres, rate)

        print("\nFarmer entry accepted!")
        print("Farmer ID:", farmer_id)
        print("Shift:", shift)
        print("Rate per litre: Rs.", rate)
        print("Total payment: Rs.", payment)

    else:
        print("Invalid farmer details. Please check the inputs.")

except InvalidOperation:
    print("Invalid input: Enter valid numeric values.")
