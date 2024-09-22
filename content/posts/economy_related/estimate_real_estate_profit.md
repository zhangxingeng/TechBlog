---
title: "Estimate Real Estate Profits over time "
date: 2024-04-01
---

Let's break down the investment estimation for a rental property at 10 Penrose Ln, Piscataway NJ 08854, valued at $670,000, considering various financial factors over time. We will write a Python program to perform these calculations.

Here's what we'll include in our model:

1. **Initial Purchase Details**:
   - Purchase price.
   - Down payment percentage.
   - Loan details (interest rate and term).

2. **Operational Costs**:
   - Property taxes (based on average local rates).
   - Insurance costs.
   - Maintenance and repair costs.
   - Management fees.

3. **Rental Income**:
   - Expected monthly rent (based on local rental market).
   - Vacancy rate (probability of the property being unrented).

4. **Appreciation and Inflation**:
   - Annual property appreciation.
   - Inflation rate to adjust future cash flows to present value.

5. **Sales Exit Strategy**:
   - Estimated selling price at the end of a specified period, considering appreciation.
   - Sales commission and closing costs.

6. **Financial Metrics**:
   - Net Present Value (NPV) to evaluate the profitability considering the time value of money.
   - Internal Rate of Return (IRR) to understand the efficiency of the investment.

Let’s implement this in Python:

```python
import numpy as np

def calculate_real_estate_investment(purchase_price, down_payment_percent, loan_interest_rate, loan_term,
                                     property_tax_rate, insurance_rate, maintenance_rate, management_fee_rate,
                                     expected_rent, vacancy_rate, appreciation_rate, inflation_rate, years_to_hold):
    # Financial assumptions
    down_payment = purchase_price * down_payment_percent
    loan_amount = purchase_price - down_payment
    monthly_interest_rate = loan_interest_rate / 12
    total_payments = loan_term * 12

    # Monthly mortgage payment calculation
    monthly_mortgage_payment = np.pmt(monthly_interest_rate, total_payments, loan_amount)

    # Annual operational costs and income
    annual_property_tax = purchase_price * property_tax_rate
    annual_insurance = purchase_price * insurance_rate
    annual_maintenance = purchase_price * maintenance_rate
    annual_management_fees = expected_rent * 12 * management_fee_rate
    gross_annual_rent = expected_rent * 12
    expected_vacancy_losses = gross_annual_rent * vacancy_rate

    net_annual_rent = gross_annual_rent - expected_vacancy_losses - annual_property_tax - annual_insurance - annual_maintenance - annual_management_fees

    # Adjustments for inflation and discount cash flows
    cash_flows = []
    for year in range(1, years_to_hold + 1):
        future_value_rent = net_annual_rent * ((1 + inflation_rate) ** year)
        discounted_cash_flow = future_value_rent / ((1 + inflation_rate) ** year)
        cash_flows.append(discounted_cash_flow - (monthly_mortgage_payment * 12))

    # Property sale price at the end of holding period
    sale_price = purchase_price * ((1 + appreciation_rate) ** years_to_hold)
    sales_commission = sale_price * 0.06
    net_sale_proceeds = sale_price - sales_commission - loan_amount * np.pv(monthly_interest_rate, total_payments - years_to_hold * 12, monthly_mortgage_payment, 0)
    cash_flows.append(net_sale_proceeds)

    # NPV and IRR
    npv = np.npv(inflation_rate, cash_flows)
    irr = np.irr(cash_flows)

    return {
        'NPV': npv,
        'IRR': irr,
        'Annual Cash Flow': cash_flows[:-1],
        'Net Sale Proceeds': net_sale_proceeds
    }

# Example usage
result = calculate_real_estate_investment(
    purchase_price=670000,
    down_payment_percent=0.20,
    loan_interest_rate=0.04,
    loan_term=30,
    property_tax_rate=0.025,
    insurance_rate=0.005,
    maintenance_rate=0.01,
    management_fee_rate=0.08,
    expected_rent=3000,
    vacancy_rate=0.07,
    appreciation_rate=0.03,
    inflation_rate=0.02,
    years_to_hold=10
)

print(f"NPV: ${result['NPV']:,.2f}")
print(f"IRR: {result['IRR']*100:.2f}%")
for i, cf in enumerate(result['Annual Cash Flow'], 1):
    print(f"Year {i} Cash Flow: ${cf:,.2f}")
print(f"Net Sale Proceeds: ${result['Net Sale Proceeds']:,.2f}")
```

This script will calculate the net present value (NPV) and internal rate of return (IRR) based on the given parameters. Adjust the parameters such as rent, appreciation, and interest rates as per current or expected future market conditions.
