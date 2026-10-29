
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP_SIZE = Decimal("0.1")
MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")
CENT = Decimal("0.01")


def rate_per_litre(fat, snf):
    """Calculate the rate per litre."""
    fat_steps = ((fat - STANDARD_FAT) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )
    snf_steps = ((snf - STANDARD_SNF) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE
    rate += snf_steps * SNF_STEP_VALUE
    return rate.quantize(CENT)


def calculate_payment(farmer_id, litres, fat, snf):
    """Validate an entry and calculate its payment."""
    farmer_id = str(farmer_id).strip()

    if not farmer_id:
        raise ValueError("Farmer ID cannot be empty.")

    try:
        litres = Decimal(str(litres))
        fat = Decimal(str(fat))
        snf = Decimal(str(snf))
    except Exception:
        raise ValueError("Enter valid numeric values.")

    if not all(x.is_finite() for x in (litres, fat, snf)):
        raise ValueError("Values must be finite numbers.")

    if litres <= 0:
        raise ValueError("Litres must be positive.")

    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat must be between 2.0 and 7.0.")

    if snf <= 0:
        raise ValueError("SNF must be positive.")

    rate = rate_per_litre(fat, snf)
    payment = (litres * rate).quantize(CENT)

    return rate, payment


if __name__ == "__main__":
    print("VILLAGE MILK CO-OPERATIVE")
    print("-------------------------")

    farmer_id = input("Enter farmer ID: ")
    litres = input("Enter litres: ")
    fat = input("Enter fat percentage: ")
    snf = input("Enter SNF percentage: ")

    try:
        rate, payment = calculate_payment(
            farmer_id, litres, fat, snf
        )
        print(f"Rate per litre: Rs. {rate:.2f}")
        print(f"Payment: Rs. {payment:.2f}")
    except ValueError as error:
        print("Error:", error)
