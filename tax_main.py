# ============================================
# SRI LANKAN TAX CALCULATOR PROJECT
# ============================================
# Name: K. V. Dhanuja Senarathna
# Date: 17/02/2026

# ============================================
# SRI LANKA TAX BRACKETS (Effective April 1, 2025) 
# ============================================
# Annual Income (LKR):
#   Up to 1,800,000: 0% (Tax-free!)
#   1,800,001 - 2,800,000: 6%
#   2,800,001 - 3,300,000: 18%
#   3,300,001 - 3,800,000: 24%
#   3,800,001 - 4,300,000: 30%
#   Greater than 4,300,000: 36%
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
# HELPER FUNCTIONS FOR DISPLAY
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
    """Print details for high earners (>= Rs. 4,300,000)"""
    for income in high_earner_incomes:
        tax = calculate_income_tax(income)
        print(f"Income: Rs. {income:,.2f} - Tax: Rs. {tax:,.2f}")


# ============================================
# MAIN PROGRAM
# ============================================

def main():
    """Main program to demonstrate tax calculations"""

    # Test data: Multiple taxpayer incomes (in LKR)
    incomes = [2500000, 4000000, 5000000, 1500000, 3500000]

    print("+-" * 30)
    print("SRI LANKAN TAX CALCULATOR (April 2025 Tax Reforms)")
    print("+-" * 30)

    # Calculate taxes for all incomes 
    taxes = list(map(calculate_income_tax, incomes))

    # Filter high earners 
    high_earners = list(filter(lambda income: income >= 4300000, incomes))

    # Create (income, tax) pairs and sort
    sorted_incomes_taxes = sorted(zip(incomes, taxes), key=lambda x: x[1], reverse=True)

    # ========================================
    # Display Results
    # ========================================

    # Display detailed tax reports
    print("\n" + "=" * 60)
    print("DETAILED TAX REPORTS")
    print("=" * 60)
    for income in incomes:
        print_taxpayer_details(income)

    # Display top taxpayers ranking
    print("\n" + "=" * 60)
    print("TOP TAXPAYERS (Ranked by Tax Paid)")
    print("=" * 60)
    print_ranking(sorted_incomes_taxes)

    # Display high earners
    print("\n" + "=" * 60)
    print("HIGH EARNERS (>= Rs. 4,300,000 - Top Tax Bracket)")
    print("=" * 60)
    print_high_earners(high_earners)


# Run the program
if __name__ == "__main__":
    main()