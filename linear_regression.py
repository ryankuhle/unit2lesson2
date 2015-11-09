#goal: how does a fico score impact interest rates

import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate
#[]

#need to remove "months"
#print loansData['Loan.Length'][0:5]

#need to split and use the first column of the list
#print loansData['FICO.Range'][0:5] 