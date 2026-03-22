# ============================================
# SRI LANKAN TAX CALCULATOR - MAIN PROGRAM
# ============================================

from tax_functions import (
    calculate_income_tax,
    print_taxpayer_details,
    print_ranking,
    print_high_earners
)


def main():
    """Main program to demonstrate tax calculations"""

    # Test data
    incomes = [2500000, 4000000, 5000000, 1500000, 3500000]

    print("+-" * 30)
    print("SRI LANKAN TAX CALCULATOR (April 2025 Tax Reforms)")
    print("+-" * 30)

    # Calculate taxes
    taxes = list(map(calculate_income_tax, incomes))

    # Filter high earners
    high_earners = list(filter(lambda income: income >= 4300000, incomes))

    # Sort taxpayers by tax paid
    sorted_incomes_taxes = sorted(
        zip(incomes, taxes),
        key=lambda x: x[1],
        reverse=True
    )

    # ========================================
    # DISPLAY RESULTS
    # ========================================

    print("\n" + "=" * 60)
    print("DETAILED TAX REPORTS")
    print("=" * 60)

    for income in incomes:
        print_taxpayer_details(income)

    print("\n" + "=" * 60)
    print("TOP TAXPAYERS (Ranked by Tax Paid)")
    print("=" * 60)
    print_ranking(sorted_incomes_taxes)

    print("\n" + "=" * 60)
    print("HIGH EARNERS (>= Rs. 4,300,000)")
    print("=" * 60)
    print_high_earners(high_earners)


if __name__ == "__main__":
    main()