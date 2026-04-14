from .payment_frequency import PaymentFrequency
ADMIN_PASSWORD = "admin123"

class Mortgage():
    years_for_amortizing = [5,10,15,20,25,30]

    
    
    def __init__(self, loan_amount:float, annual_interest_rate:float,
                 amortization:int, frequency):
        
        assert loan_amount > 0
        
        self.__loan_amount = loan_amount
        self.__annual_interest_rate = annual_interest_rate
        self.__amortization = amortization

        if isinstance(frequency, str):
            self.frequency = eval(f"PaymentFrequency.{frequency}")
        else:
            self.frequency = frequency

        
        
        if amortization not in self.years_for_amortizing:
            raise ValueError(f"Amortization must be a value in {self.years_for_amortizing}")
        
        self.__amortization = amortization
        
        # if frequency not in PaymentFrequency.__members__:
        #     raise ValueError("Frequency must be a value of PaymentFrequency type")
        
        self.frequency = frequency
        
    def __str__(self) -> str:
        amt = f"${self.loan_amount:,.2f}"
        rate = f"{self.annual_interest_rate * 100:.2f}%"
        amort = f"{self.amortization}"
        freq = f"{self.frequency.name}"
        payment = self.get_payment()
        pay_str = f"${payment:,.1f}"
        return (
            f"Mortgage Amount: {amt}\n"
            f"Rate: {rate}\n"
            f"Amortization: {amort}\n"
            f"Frequency: {freq}\n"
            f" -- Calculated Payment: {pay_str}")

    
    def __repr__(self):
     return (
        f"Mortgage({self.loan_amount}, "
        f"{self.annual_interest_rate}, "
        f"{self.amortization}, "
        f"{self.frequency.name})")

    
    
    def get_payment(self):
       
        P = self.loan_amount
        freq = self.frequency.value
        i = self.annual_interest_rate / freq
        n = self.amortization * freq
        return P * i * (1 + i)**n / ((1 + i)**n - 1)



    @property
    def loan_amount(self):
    
      return self.__loan_amount

    @loan_amount.setter
    def loan_amount(self,new_amt):
      if not isinstance(new_amt,(int , float)):
        raise TypeError("Loan amount must be a value of a numeric type")
      if new_amt <=0:
        raise ValueError("Loan Amount must be a value greater than zero")
      self.__loan_amount = new_amt
    
    
    @property
    def annual_interest_rate(self):
       return self.__annual_interest_rate
    
    @annual_interest_rate.setter
    def annual_interest_rate(self,new_rate):
       
       if not isinstance(new_rate,(float,int)):
            raise TypeError("Annual interest rate must be a value of a numeric type")
       if new_rate <=0 or new_rate > 1:
            raise ValueError("Annual interest rate must be a value greater than zero and less than or equal to 1")
       
       self.__annual_interest_rate = new_rate
    
    @property
    def amortization(self):
        """Accessor for the private amortization years."""
        return self.__amortization

    @amortization.setter
    def amortization(self, years):
        """Mutator: validate then store the amortization value."""
        if years not in Mortgage.years_for_amortizing:
            raise ValueError(f"Amortization must be a value in {Mortgage.years_for_amortizing}")
        self.__amortization = years
       
    @property
    def frequency(self):
        return self.__payment_frequency

    @frequency.setter
    def frequency(self, value):
        if value not in PaymentFrequency.__members__:
            raise ValueError("Frequency must be a value of PaymentFrequency type")
        self.__payment_frequency = PaymentFrequency[value]
