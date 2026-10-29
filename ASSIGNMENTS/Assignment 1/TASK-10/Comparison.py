
from decimal import Decimal, ROUND_HALF_UP
import time

# Task 10: Compare float, Decimal, rounding and rate caching

PAYMENTS = ["300.00", "283.90", "333.60"]
SIZES = [300, 6000, 150000]


def total_float(items):
    """Add payment amounts using float."""
    total = 0.0
    for amount in items:
        total += float(amount)
    return total


def total_decimal(items):
    """Add payment amounts accurately using Decimal."""
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total


def measure(function, items):
    """Return the result and execution time."""
    start = time.perf_counter()
    result = function(items)
    elapsed = time.perf_counter() - start
    return result, elapsed


print("TASK 10 - EXPECTATION VS EXECUTION")
print("=" * 65)

for size in SIZES:
    payments = PAYMENTS * (size // len(PAYMENTS))

    float_total, float_time = measure(total_float, payments)
    decimal_total, decimal_time = measure(total_decimal, payments)

    difference = abs(
        Decimal(str(float_total)) - decimal_total
    )

    print("\nNumber of payments:", size)
    print("Float total:       Rs.", round(float_total, 2))
    print("Decimal total:     Rs.", decimal_total)
    print("Absolute difference: Rs.", difference)
    print("Float time:       ", round(float_time, 6), "seconds")
    print("Decimal time:     ", round(decimal_time, 6), "seconds")


print("\nROUNDING COMPARISON")
print("-" * 65)

raw_payments = [
    Decimal("1.005"),
    Decimal("2.005"),
    Decimal("3.005")
]

rounded_individually = sum(
    amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    for amount in raw_payments
)

rounded_at_end = sum(raw_payments).quantize(
    Decimal("0.01"), rounding=ROUND_HALF_UP
)

print("Raw payments:", raw_payments)
print("Round each payment, then add: Rs.", rounded_individually)
print("Add first, then round total:  Rs.", rounded_at_end)


print("\nRATE-CACHE COMPARISON")
print("-" * 65)

def calculate_rate(fat, snf):
    """Calculate rate from fat and SNF percentages."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return 30.00 + fat_steps * 0.40 + snf_steps * 0.30


samples = [
    (3.5, 8.5),
    (4.2, 8.7),
    (3.1, 8.3)
] * 50000

start = time.perf_counter()
normal_rates = [
    calculate_rate(fat, snf) for fat, snf in samples
]
normal_time = time.perf_counter() - start

start = time.perf_counter()
rate_table = {}
cached_rates = []

for fat, snf in samples:
    key = (fat, snf)

    if key not in rate_table:
        rate_table[key] = calculate_rate(fat, snf)

    cached_rates.append(rate_table[key])

cached_time = time.perf_counter() - start

print("Rates calculated:", len(normal_rates))
print("Different rate pairs stored:", len(rate_table))
print("Recalculation time:", round(normal_time, 6), "seconds")
print("Cache lookup time:", round(cached_time, 6), "seconds")
print("Results match:", normal_rates == cached_rates)
