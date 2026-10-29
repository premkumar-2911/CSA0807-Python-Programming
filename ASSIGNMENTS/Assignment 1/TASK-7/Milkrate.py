from decimal import Decimal

# Named constants
BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
FAT_ADJUSTMENT = Decimal("0.40")
SNF_ADJUSTMENT = Decimal("0.30")
STEP = Decimal("0.1")


def calculate_rate(fat, snf):
    """Calculate the milk rate per litre."""
    fat_difference = (fat - STANDARD_FAT) / STEP
    snf_difference = (snf - STANDARD_SNF) / STEP

    fat_amount = fat_difference * FAT_ADJUSTMENT
    snf_amount = snf_difference * SNF_ADJUSTMENT

    return BASE_RATE + fat_amount + snf_amount


def calculate_payment(litres, rate):
    """Calculate the total payment."""
    return litres * rate
