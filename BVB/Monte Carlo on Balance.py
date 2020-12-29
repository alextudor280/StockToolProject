import numpy as np
import matplotlib.pyplot as plt

#Monte Carlo for gross profit prediction
# We first assign estimations for mean revenue and deviation (in millions of dollars)

rev_m = 170
rev_stdev = 20
iterations = 1000

rev = np.random.normal(rev_m, rev_stdev, iterations)

plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.title('Revenue')
plt.show()

#Now we create a normal distribution for COGS(cost of goods sold) given that we know a mean (0.6 out of revenue) for it and standard deviation(0.1)\

COGS = - (rev * np.random.normal(0.6,0.1))

plt.figure(figsize=(15,6))
plt.plot(COGS)
plt.title('Cost of goods sold')
plt.show()

#We can now compute the Gross Profit by adding the 2 of them (sum not difference since we added a minus in COGS)

gross_profit = rev + COGS

plt.figure(figsize=(15, 6))
plt.plot(gross_profit)
plt.title('Gross Profit')
plt.show()

print('The maximum gross profit is: $ ' + str(round(max(gross_profit), 3)) + ' million')
print('The minimum gross profit is: $ ' + str(round(min(gross_profit), 3)) + ' million')
print('The average gross profit is: $ ' + str(round(gross_profit.mean(), 3)) + ' million')

plt.figure(figsize=(10,6))
plt.hist(gross_profit, bins=20)
plt.show()

#Monte Carlo for EBITDA
#Do the same thing but instead of gross_profit calculate EBITDA which is gross_profit - operational costs

