# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include="object")
print(categorical_var)

numerical_var = bank.select_dtypes(include = "number")
print(numerical_var)







# code ends here


# --------------
# code starts here
banks = bank.drop("Loan_ID", axis=1)
print(banks.isnull().sum())

bank_mode = banks.mode()
values = bank_mode.values[0]
cols = [i for i in bank_mode.columns]
filled = {i:j for i, j in zip(cols, values)}
banks.fillna(filled, inplace=True)

print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks, values = "LoanAmount", index = ["Gender", "Married", "Self_Employed"])




# code ends here



# --------------
# code starts here


# code ends here
loan_approved_se = banks[(banks.Self_Employed == "Yes") & (banks.Loan_Status == 'Y')]
loan_approved_nse = banks[(banks.Self_Employed == "No") & (banks.Loan_Status == 'Y')]

percentage_se = len(loan_approved_se.values)  / 614 * 100
percentage_nse = len(loan_approved_nse.values) / 614 * 100


# --------------
# code starts here
month_to_year = lambda x: x / 12

loan_term = banks.Loan_Amount_Term.apply(month_to_year)

big_loan_term = len(loan_term[loan_term >= 25])


# code ends here


# --------------
# code ends here

columns = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])[columns]

# Check the mean value 
mean_values=loan_groupby.agg([np.mean])

print(mean_values)

# code ends here


