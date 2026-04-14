from mortgage.mortgage import Mortgage
from mortgage.payment_frequency import PaymentFrequency

__author__ = "ACE Faculty, Jashanpreet Singh"
__version__ = "1.3.2025"

def main():
    # 1. Create an instance of the Mortgage class. Initialize the object using values of your choosing.
    loan_amount = 400000
    annual_interest_rate = 0.04
    amortization = 20
    frequency = PaymentFrequency.MONTHLY

    mortgage = Mortgage(loan_amount, annual_interest_rate, amortization, frequency)

    # 2. Print the official string representation of the object.
    print(f"Official String Representation: {repr(mortgage)}")

    # 3. Print the payment amount for the mortgage. Format the payment amount as currency.
    payment = mortgage.get_payment()
    print(f"Monthly Payment: ${payment:,.2f}")

    # 4. Update the state of the object such that all attributes values are different than what they were initialized to.
    mortgage.set_loan_amount(500000)
    mortgage.set_annual_interest_rate(0.045)
    mortgage.set_amortization(25)
    mortgage.set_frequency(PaymentFrequency.BI_WEEKLY)

    # 5. Choose any attribute of the object and print its current state.
    print(f"Updated Loan Amount: ${mortgage.get_loan_amount():,.2f}")
    print(f"Updated Amortization Period: {mortgage.get_amortization()} years")

    # 6. Attempt to create another instance of the Mortgage class. The statement must use one value that will cause
    # the initialization to fail. Prevent the script from abnormally ending and print the error message to the console.
    try:
        invalid_mortgage = Mortgage("invalid amount", annual_interest_rate, amortization, frequency)
    except Exception as e:
        print(f"Error: {e}")
