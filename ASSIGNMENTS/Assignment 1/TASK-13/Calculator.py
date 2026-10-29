
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
STEP_SIZE = Decimal("0.1")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
SNF_STEP_VALUE = Decimal("0.30")
BONUS_PER_LITRE = Decimal("0.50")
BONUS_LIMIT = Decimal("500")


def get_rate_card(month):
    """Return the correct rate card for the selected month."""
    month = month.strip().lower()

    if month in ["april", "may", "june"]:
        return Decimal("32.00"), Decimal("0.45")

    return Decimal("30.00"), Decimal("0.40")


def calculate_rate(fat, snf, month):
    """Calculate the rate using the selected seasonal rate card."""
    base_rate, fat_step_value = get_rate_card(month)

    fat_steps = ((fat - STANDARD_FAT) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )

    snf_steps = ((snf - STANDARD_SNF) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )

    rate = base_rate + fat_steps * fat_step_value
    rate += snf_steps * SNF_STEP_VALUE

    return rate.quantize(CENT)


def calculate_ten_day_payments(entries, month):
    """Calculate payments and the eligible ten-day bonus."""
    if not entries:
        raise ValueError("At least one entry is required.")

    total_litres = sum(
        (litres for litres, fat, snf in entries),
        Decimal("0")
    )

    for litres, fat, snf in entries:
        if not all(value.is_finite() for value in (litres, fat, snf)):
            raise ValueError("All readings must be finite numbers.")

        if litres <= 0:
            raise ValueError("Litres must be positive.")

        if not Decimal("2.0") <= fat <= Decimal("7.0"):
            raise ValueError("Fat must be between 2.0 and 7.0.")

        if snf <= 0:
            raise ValueError("SNF must be positive.")

    bonus_eligible = total_litres > BONUS_LIMIT
    results = []
    total_payment = Decimal("0.00")

    for litres, fat, snf in entries:
        rate = calculate_rate(fat, snf, month)
        milk_payment = (litres * rate).quantize(CENT)

        bonus = Decimal("0.00")
        if bonus_eligible:
            bonus = (litres * BONUS_PER_LITRE).quantize(CENT)

        payment = milk_payment + bonus
        total_payment += payment

        results.append((rate, milk_payment, bonus, payment))

    return total_litres, results, total_payment


if __name__ == "__main__":
    print("TASK 12 - UPDATED MILK PAYMENT CALCULATOR")
    print("=" * 48)

    # Two-decimal analyser readings; total is 550 litres.
    entries = [
        (Decimal("300"), Decimal("3.55"), Decimal("8.52")),
        (Decimal("250"), Decimal("4.25"), Decimal("8.55"))
    ]

    month = "April"

    total_litres, results, total_payment = (
        calculate_ten_day_payments(entries, month)
    )

    print("Month:", month)
    print("Total litres over ten days:", total_litres)
    print("Bonus eligible:", total_litres > BONUS_LIMIT)

    for index, result in enumerate(results, start=1):
        rate, milk_payment, bonus, payment = result

        print("\nEntry", index)
        print("Rate per litre: Rs.", rate)
        print("Milk payment:  Rs.", milk_payment)
        print("Bonus:         Rs.", bonus)
        print("Total payment: Rs.", payment)

    print("\nFINAL TEN-DAY TOTAL: Rs.", total_payment)

    # Test the original rate card outside April-June.
    print("\nOUTSIDE SEASON TEST")
    print("July rate for fat 4.2 and SNF 8.7:",
          calculate_rate(
              Decimal("4.20"), Decimal("8.70"), "July"
          ))
