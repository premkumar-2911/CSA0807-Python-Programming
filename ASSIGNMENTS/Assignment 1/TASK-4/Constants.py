
from decimal import Decimal

# Named constants
BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
FAT_ADJUSTMENT = Decimal("0.40")
SNF_ADJUSTMENT = Decimal("0.30")
FAT_STEP = Decimal("0.1")
SNF_STEP = Decimal("0.1")

# Sample farmer details
farmer_id = "F001"
litres = Decimal("10.0")
fat = Decimal("3.7")
snf = Decimal("8.6")

# Calculate adjustments using constants
fat_difference = (fat - STANDARD_FAT) / FAT_STEP
snf_difference = (snf - STANDARD_SNF) / SNF_STEP

fat_amount = fat_difference * FAT_ADJUSTMENT
snf_amount = snf_difference * SNF_ADJUSTMENT

# Calculate payment
rate_per_litre = BASE_RATE + fat_amount + snf_amount
total_payment = litres * rate_per_litre

# Display constants and results
print("Base rate: Rs.", BASE_RATE)
print("Standard fat:", STANDARD_FAT, "%")
print("Standard SNF:", STANDARD_SNF, "%")
print("Fat adjustment per 0.1%: Rs.", FAT_ADJUSTMENT)
print("SNF adjustment per 0.1%: Rs.", SNF_ADJUSTMENT)
print("------------------------------")
print("Farmer ID:", farmer_id)
print("Milk quantity:", litres, "litres")
print("Calculated rate per litre: Rs.", rate_per_litre)
print("Total payment: Rs.", total_payment)
