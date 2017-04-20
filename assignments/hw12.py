import pandas as pd
import matplotlib.pyplot as plt


#Import the Iris.csv data
iris = pd.read_csv("Iris.csv")
print(iris.head())

# drop the id column
iris = iris.drop('Id', axis=1)
print(iris.head())
print(iris.info())

# Subset the dataframe to create a new dataframe that includes
# only the measurements from the setosa species.
irisNew = iris[iris['Species'] == 'Iris-setosa']
print(irisNew.head())
print(irisNew.info())

# Use describe to get summary statistics

print(iris.describe())

# Group-by and then use describe

print(iris.groupby('Species').describe())

#iris.boxplot(column='PetalLengthCm', by='Species')

# Use matplotlib
#plt.plot(iris[['Species']], iris[['PetalLengthCm']], color='blue')
#plt.show()



