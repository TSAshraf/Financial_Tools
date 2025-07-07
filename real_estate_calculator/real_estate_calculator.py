# Need to still calculate personal taxes
# Need to still calculate corporate taxes

# Initial inputs
CurrentAccount = 0 # Starting Cash
CurrentIncome = 60_000 # Starting Income
RealHouseValuation = 0 # Starting House Value
RealDebtValuation = 0 # Starting Debt
RentalYield = 0 # Starting Rental Yield
AverageHouseValue = 100_000 # Average value of house in GBP USD etc
Deposit = 0.25 * AverageHouseValue # A house is bought with 25% deposit
LoanAmount = 0.75 * AverageHouseValue # A house is bought at 75% LTV

# Modifiers (as percentage in decimals)
InterestRate = 0.06 # APR on loan
IncomeRaise = 1.02 # Average Yearly raise
Inflation = 0.975 # Average Yearly Inflation
HouseAppreciation = 1.025 # Average House Appreciation
SavingsRate = 0.5 # Average Savings rate
RentalYieldRate = 0.05 # Average rental yield

# Counter
Years = 0
NumberOfHouses = 0

# Can change the while statement to change the parameters of the loop
# e.g. RealHouseValuation < 10_000_000 to see by when you would have 10,000,000 (in today's money) in real estate
while RentalYield < 1_000_000:
    Years += 1

    # Annual Projections
    CurrentIncome *= IncomeRaise  # Projected Income
    RealHouseValuation *= HouseAppreciation # Projected Total house value
    RealDebtValuation *= Inflation # Projected Total Debt

    InterestPayment = InterestRate * RealDebtValuation # Projected yearly interest payments
    Savings = CurrentIncome * SavingsRate # Projected yearly Savings
    RentalYield = RealHouseValuation * RentalYieldRate # Projected yearly Rental Yields

    # CurrentAccount Calculations
    CurrentAccount += RentalYield
    CurrentAccount += Savings
    CurrentAccount -= InterestPayment

    while CurrentAccount >= Deposit:
        print(f"Years: {Years}: Buying a New house")
        CurrentAccount -= Deposit
        RealHouseValuation += AverageHouseValue
        RealDebtValuation += LoanAmount
        NumberOfHouses += 1

    print(f"Years: {Years} House value {RealHouseValuation}")
    print(f"Years: {Years} Debt value {RealDebtValuation}")
    print(f"Years: {Years} Rental Yield {RealHouseValuation}")
    print(f"Years: {Years} CurrentIncome {CurrentIncome}")
    print(f"Years: {Years} CurrentAccount {CurrentAccount}")
    print(f"Years: {Years} NumberOfHouses {NumberOfHouses}")
