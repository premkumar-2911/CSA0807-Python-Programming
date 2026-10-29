
from decimal import Decimal
from task09_calculator import calculate_payment

tests = [
    ("Standard", "10", "3.5", "8.5", "30.00", "300.00"),
    ("Above standard", "8.5", "4.2", "8.7", "33.40", "283.90"),
    ("Below standard", "12", "3.1", "8.3", "27.80", "333.60"),
    ("Minimum fat", "1", "2.0", "8.5", "24.00", "24.00"),
    ("Maximum fat", "1", "7.0", "8.5", "44.00", "44.00"),
]

print("TASK 9 - VALID TESTS")
print("-" * 45)

for name, litres, fat, snf, expected_rate, expected_pay in tests:
    rate, payment = calculate_payment("F001", litres, fat, snf)

    assert rate == Decimal(expected_rate), name + " rate failed"
    assert payment == Decimal(expected_pay), name + " payment failed"

    print(name, "- PASS")

invalid_tests = [
    ("Text input", "ten", "3.5", "8.5"),
    ("Negative litres", "-2", "3.5", "8.5"),
    ("Fat below limit", "10", "1.9", "8.5"),
    ("Fat above limit", "10", "7.1", "8.5"),
]

print("\nTASK 9 - INVALID TESTS")

for name, litres, fat, snf in invalid_tests:
    try:
        calculate_payment("F001", litres, fat, snf)
    except ValueError:
        print(name, "- PASS: rejected")
    else:
        raise AssertionError(name + " should have failed")

print("\nAll tests passed!")
