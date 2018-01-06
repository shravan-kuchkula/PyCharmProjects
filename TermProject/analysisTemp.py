from analysisState import AnalysisState
from analysisCountry import AnalysisCountry
from analysisSkills import AnalysisSkills


# Create skills analysis object and pass a list of skills
list = ["r", "python", "java", "sas", "scala", "javascript"]
skills = AnalysisSkills(list, "US")

# get number of jobs per skill
skills.getJobsBySkill(barplot=False)
skills.getJobsBySkill()