import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("Iris.csv")
print(iris.shape)

print(iris.head())

#iris.plot(x= 'SepalLengthCm', y= 'SepalWidthCm')
#plt.show()

iris.boxplot(column = 'SepalLengthCm', by='Species')
plt.title('Sepal Length')
plt.show()

iris.boxplot(column = 'SepalWidthCm', by='Species')
plt.title('Sepal Width')
plt.show()

iris.boxplot(column = 'PetalLengthCm', by='Species')
plt.title('Petal Length')
plt.show()

iris.boxplot(column = 'PetalWidthCm', by='Species')
plt.title('Petal Width')
plt.show()

