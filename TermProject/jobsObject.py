import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from diceStateDAO import DiceDAO

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.jobs


# Derive collection name
#diceJobs = DiceDAO(db, "python", "07059")
diceJobs = DiceDAO(db, "python", "07059")
#diceJobs.retreiveJobs()

# number of jobs which need a jobSkill in a location
print(diceJobs.countJobs())

# call filterByCity and pass in the city name
#diceJobs.filterJobsByCity("Warren, NJ")
#diceJobs.filterJobsByCity("Newark, NJ")

# call groupBy which uses the aggregation framework
#diceJobs.groupByLocation()

# call groupBy and order in descending
cursor = diceJobs.topCompanies()
#print(type(cursor))

# Use pandas to create a df
df = pd.DataFrame(list(cursor))
print(df)

# plot a bar plot
sns.barplot(x="JobCount", y="Company", data=df, orient="h")
plt.xlabel("Number of jobs")
plt.title("{} jobs in a 30 mile radius of {}".format("python", "07059"))
plt.yticks(fontsize=6)
plt.xticks(fontsize=6)
plt.show()






