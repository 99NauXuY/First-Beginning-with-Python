import pandas as pd
sal = pd.read_csv("C:/Users/Yuxuan/Downloads/Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises/Salaries.csv")
#Check the head of the DataFrame.
sal.head()
#Use the .info() method to find out how many entries there are.
'''sal.info()'''
#What is the average BasePay ?
avg = sal["BasePay"].mean()
#What is the highest amount of OvertimePay in the dataset ?
high =sal["OvertimePay"].max()
#What is the job title of JOSEPH DRISCOLL ?
title = sal[sal["EmployeeName"]=="JOSEPH DRISCOLL"]["JobTitle"]
# What is the name of highest paid person (including benefits)?
highest = sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].max()]['EmployeeName']
#What is the name of lowest paid person (including benefits)?Negative paid
lowest = sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].min()]['EmployeeName']
#What was the average (mean) BasePay of all employees per year? (2011-2014) ?
mean = sal.groupby("Year").mean()["BasePay"]
#How many unique job titles are there?
unique = sal["JobTitle"].nunique()
#What are the top 5 most common jobs?
mostcommon = sal["JobTitle"].value_counts().head(5)
#How many Job Titles were represented by only one person in 2013?
job2013 = sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1)
#How many people have the word Chief in their job title?
def chief(title):
    if "chief" in title.lower():
        return True
    else:
        return False
chefs = sum(sal["JobTitle"].apply(lambda x: chief(x)))
#Is there a correlation between length of the Job Title string and Salary?
sal['title_len'] = sal['JobTitle'].apply(len)
corr = sal[['title_len','TotalPayBenefits']].corr() # No correlation.
