#goal: how does a fico score impact interest rates

import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate
#[]

cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
loansData['Loan.Length'] = cleanLoanLength

cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])
loansData['FICO.Score'] = [x[0] for x in cleanFICORange]

#print loansData['FICO.Score'][0:5]