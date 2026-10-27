
from decimal import Decimal

# Named constants
BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")

# Sample farmer details
farmer_id = "F001"
litres = Decimal("10.0")
fat = Decimal("3.5")
snf = Decimal("8.5")
shift = "Morning"

# Validate the record
valid = (
    bool(farmer_id.strip())
    and litres > 0
    and MIN_FAT <= fat <= MAX_FAT
    and snf > 0
    and shift in ("Morning", "Evening")
)

# Display the results
print("Farmer ID:", farmer_id)
print("Milk quantity:", litres, "litres")
print("Fat percentage:", fat, "%")
print("SNF percentage:", snf, "%")
print("Shift:", shift)
print("Base rate: Rs.", BASE_RATE)
print("Entry valid:", valid)
