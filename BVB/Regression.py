import numpy as np
import pandas as pd

from scipy import stats
import statsmodels.api as sm

import matplotlib.pyplot as plt

data = pd.read_excel('C:/Users/alex_/Desktop/Phynance course/81 Running a Regression'
                     ' in Python/Python 3/Housing.xlsx', engine='openpyxl')


x = data[['House Size (sq.ft.)', 'Number of Rooms', 'Year of Construction']]
y = data['House Price']

x1 = sm.add_constant(x)
reg = sm.OLS(y, x1).fit()
print(reg.summary())

scale=[0, 2500, 0, 1500000]

plt.scatter(x, y)
plt.axis(scale)
plt.xlabel('House Size (sq. ft.)')
plt.ylabel('House Price')
plt.show()




slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print('The slope is: ' + str(slope))
print('The intercept is: ' + str(intercept))
print('The R^2 value is: ' + str(r_value ** 2))
print('The P value is: ' + str(p_value))
print('The standard error is: ' + str(std_err))

