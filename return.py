class Investment():
    '''
    principal: initial amount
    annuity: Yearly investment (default 401k max = $19,500)
    apr: annual rate of return on investment (default 10%)
    dpr: daily rate of return on investment
    inflation: annual depreciation due to inflation (default 3%)
    '''
    def __init__(self, principal : float, annuity : float = 19500, apr : int = 10, inflation : int = 3):
        self.principal = principal
        self.annuity = annuity
        self.dpr = apr / 36500 # divide by 365 days, then convert to decimal 
        self.inflation = inflation / 100 # convert percent to decimal

    '''
    Assumes interest is compounded daily and annuity occurs every 14 days (paycheck cycle)
    finalAmount: Amount made by end of numYears
    adjustedAmount: What finalAmount is worth today after adjusting for inflation
    numYears: defaults to 30 years
    '''
    def invest(self, numYears : int = 30):
        quotient, remainder = divmod(365, numYears)
        print(f'Quotient, Remainder = {quotient}, {remainder}')
        tmp : float = self.principal
        for i in range(quotient):
            tmp = tmp*(1 + self.dpr)**12
            tmp += self.annuity

        finalAmount : float = tmp*(1 + self.dpr)**remainder
        adjustedAmount : float = finalAmount*(1 - self.inflation)
        return finalAmount, adjustedAmount

def main():
    investor = Investment(principal = 20000)
    final, adjusted = investor.invest(numYears = 30)
    print(f'Final, Adjusted = {final}, {adjusted}')

if __name__ == '__main__':
    main()