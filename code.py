import math


# Function to calculate the poisson pmf

def poisson_pmf(number_of_events1,alpha1):
  result = (math.exp(-alpha1) * alpha1**number_of_events1) / math.factorial(number_of_events1)
  return result

# Function to calculate the poisson cdf

def poisson_cdf(number_of_events2,alpha2):
  summation = 0
  for i in range(number_of_events2 + 1):
        summation += poisson_pmf(i, alpha2)
  return summation


# Getting alpha from user as alpha_value

print("! Alpha value should be a positive real number")
alpha_value = float(input("Enter alpha value: "))

# Display The table > the tale have columns (X , PMF , CDF)
print("\nX\t\t\t\tPMF\t\t\t\tCDF")
for number_of_events in range(10):
  print("________________________________________________________________________________")
  # Calling the 2 functions
  pmf = poisson_pmf(number_of_events,alpha_value)
  cdf = poisson_cdf(number_of_events,alpha_value)
  print(number_of_events,"\t\t|\t",pmf,"\t\t|",cdf,"\t|")

