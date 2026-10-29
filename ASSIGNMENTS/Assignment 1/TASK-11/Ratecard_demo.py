
import json
import time
from decimal import Decimal, ROUND_HALF_UP

# Measure the time taken to load the rate card
start = time.perf_counter()

with open("task11_ratecard.json", "r") as file:
    rate_card = json.load(file)

startup_time = time.perf_counter() - start

# Read rate values as Decimal for money calculations
BASE_RATE = Decimal(rate_card["base_rate"])
STANDARD_FAT = Decimal(rate_card["standard_fat"])
STANDARD_SNF = Decimal(rate_card["standard_snf"])
FAT_STEP_VALUE = Decimal(rate_card["fat_step_value"])
SNF_STEP_VALUE = Decimal(rate_card["snf_step_value"])
STEP_SIZE = Decimal(rate_card["step_size"])
MIN_FAT = Decimal(rate_card["min_fat"])
MAX_FAT = Decimal(rate_card["max_fat"])


def rate_per_litre(fat, snf):
    """Calculate the rate for one litre of milk."""
    fat_steps = ((fat - STANDARD_FAT) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )

    snf_steps = ((snf - STANDARD_SNF) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE
    rate += snf_steps * SNF_STEP_VALUE

    return rate.quantize(Decimal("0.01"))


def calculate_payment(litres, fat, snf):
    """Validate values and calculate the payment."""
    if litres <= 0:
        raise ValueError("Litres must be positive.")

    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat must be between 2.0 and 7.0.")

    if snf <= 0:
        raise ValueError("SNF must be positive.")

    rate = rate_per_litre(fat, snf)
    payment = (litres * rate).quantize(Decimal("0.01"))

    return rate, payment


print("TASK 11 - FINAL DESIGN")
print("-" * 35)
print("Rate card loaded successfully.")

print("Rate-card loading time:",
      round(startup_time, 6), "seconds")

litres = Decimal("8.5")
fat = Decimal("4.2")
snf = Decimal("8.7")

rate, payment = calculate_payment(litres, fat, snf)

print("\nSample farmer entry")
print("Litres:", litres)
print("Fat:", fat)
print("SNF:", snf)
print("Rate per litre: Rs.", rate)
print("Total payment: Rs.", payment)
