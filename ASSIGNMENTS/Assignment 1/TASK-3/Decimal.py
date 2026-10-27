
from decimal import Decimal

# Milk payment constants
BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
FAT_ADJUSTMENT = Decimal("0.40")
SNF_ADJUSTMENT = Decimal("0.30")
STEP = Decimal("0.1")

# Farmer details
farmer_id = "F001"
litres = Decimal("10.0")
fat = Decimal("3.7")
snf = Decimal("8.6")

# Calculate adjustments
fat_difference = (fat - STANDARD_FAT) / STEP
snf_difference = (snf - STANDARD_SNF) / STEP

fat_amount = fat_difference * FAT_ADJUSTMENT
snf_amount = snf_difference * SNF_ADJUSTMENT

# Calculate payment using Decimal
rate_per_litre = BASE_RATE + fat_amount + snf_amount
total_payment = litres * rate_per_litre

print("Farmer ID:", farmer_id)
print("Milk quantity:", litres, "litres")
print("Fat adjustment: Rs.", fat_amount)
print("SNF adjustment: Rs.", snf_amount)
print("Rate per litre: Rs.", rate_per_litre)
print("Total payment: Rs.", total_payment)

# Demonstrate Decimal precision
print("Float calculation:", 0.1 + 0.2)
print("Decimal calculation:", Decimal("0.1") + Decimal("0.2"))
