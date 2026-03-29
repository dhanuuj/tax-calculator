# ============================================
# TAX FUNCTIONS MODULE
# ============================================

# ============================================
# SRI LANKA TAX BRACKETS (Effective April 1, 2025)
# ============================================

def calculate_income_tax(annual_income):

    tax = 0

    if annual_income <= 1800000:
        return 0

    if annual_income > 1800000:
        taxable_amount = min(annual_income - 1800000, 1000000)
        tax += taxable_amount * 0.06

    if annual_income > 2800000:
        taxable_amount = min(annual_income - 2800000, 500000)
        tax += taxable_amount * 0.18

    if annual_income > 3300000:
        taxable_amount = min(annual_income - 3300000, 500000)
        tax += taxable_amount * 0.24

    if annual_income > 3800000:
        taxable_amount = min(annual_income - 3800000, 500000)
        tax += taxable_amount * 0.30

    if annual_income > 4300000:
        taxable_amount = annual_income - 4300000
        tax += taxable_amount * 0.36

    return float(tax)


def calculate_effective_tax_rate(annual_income):

    if annual_income <= 0:
        return 0

    total_tax = calculate_income_tax(annual_income)
    effective_rate = (total_tax / annual_income) * 100

    return float(effective_rate)


def calculate_take_home(annual_income):

    total_tax = calculate_income_tax(annual_income)
    return float(annual_income - total_tax)


# ============================================
# HELPER DISPLAY FUNCTIONS
# ============================================

def print_taxpayer_details(income):
    """Print detailed tax information for a single taxpayer"""

    tax = calculate_income_tax(income)
    effective_rate = calculate_effective_tax_rate(income)
    take_home = calculate_take_home(income)
    monthly_take_home = take_home / 12

    print(f"\nAnnual Income: Rs. {income:,.2f}")
    print(f"  Income Tax: Rs. {tax:,.2f} ({effective_rate:.2f}%)")
    print(f"  Take-Home (Annual): Rs. {take_home:,.2f}")
    print(f"  Take-Home (Monthly): Rs. {monthly_take_home:,.2f}")
    print("-" * 60)


def print_ranking(sorted_income_tax_pairs):
    """Print ranked list of taxpayers by tax paid"""

    for rank, (income, tax) in enumerate(sorted_income_tax_pairs, start=1):
        print(f"{rank}. Rs. {income:,.2f} - Tax Paid: Rs. {tax:,.2f}")


def print_high_earners(high_earner_incomes):
    """Print details for high earners"""

    for income in high_earner_incomes:
        tax = calculate_income_tax(income)
        print(f"Income: Rs. {income:,.2f} - Tax: Rs. {tax:,.2f}")

# dhanuja_senarathna