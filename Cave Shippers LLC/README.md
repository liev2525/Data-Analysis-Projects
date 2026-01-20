# CAVE SHIPPERS LLC ANALYSIS - CAPSTONE PROJECT 

## Table of Contents
- [Overview](##Overview)
- [Methodology](##Methodology)
- [Task](##Task)
- [Dataset](##Dataset)
- [Exploratory](##Exploratory)
- [Visualization](##Visualization)
- [Dataset Quality](##Dataset_Quality)
- [Results](##Results)

## Overview
Dataset Source: [Kaggle Data Science Job Salaries EDA](https://www.kaggle.com/code/varunsaikanuri/data-science-job-salaries-eda/input)

### Description:

The table contains data on employee salaries, including details such as work year, experience level, employment type, job title, and salary in USD. It also includes information about employee and company locations, remote work ratios, and company size. This data can be used for salary benchmarking, analyzing compensation trends across different roles and locations, and understanding the impact of remote work on salaries.

## Methodology
The file 'salaries.csv' was read into Databricks as a delta table using SQL where it was analyzed for its metadata

## Task
Amazon is a global leader in e-commerce, offering a wide range of products and services worldwide. 
This dataset includes product details and real customer reviews, allowing analysts to explore market trends, consumer behavior, and key sales insights.

## Dataset Features
- work_year: year in which the salary data was recorded
- experience_level: level of experience of the employee
- employment_type: nature of the employment
- job_title: title of the job held by the employee
- salary: annual salary of the employee 
- salary_currency: currency in which the salary is paid
- salary_in_usd:  annual salary of the employee expressed in US dollars
- employee_residence:  location where the employee resides
- remote_ratio: percentage of time the employee works remotely
- company_location: geographical location of the company
- company_size: size of the company

## Exploratory Analysis
Preliminary analysis was completed to investigate the dataset and better understand the main characterisitics. This analysis revealed there are 145k rows and 11 columns having only bigint and string datatypes. There are 416 distinct job titles and 97 distinct locations with no missing or null values. The top 5 job roles which appeared with the most frequency were: Data Scientist, Software Engineer, Data Engineer, Data Analyst and Engineer making up 51% of the total. The average salary fell between $157548 and median at $146542 with a min and max salary ranged between 1500 to 800000 USD between roles having either full-time, part-time, or contract and level of entry, mid, senior, or executive.

## Visualization Highlights

## Dataset Quality Assessment
#### Data Validity: Validated salary values, year ranges, and remote work ratios to ensure accuracy and remove invalid records prior to analysis.
#### Data Accessibility: Dataset available via Kaggle / public source and imported into Databricks.
#### Data Completeness: Assessed null distributions across key attributes (salary, job_title, experience_level, location) and addressed gaps through filtering, imputation, and “Unknown” classification where appropriate.
#### Data Consistency: Standardized categories and naming conventions (job titles, experience levels, employment types) to ensure consistent grouping and reliable comparative analysis across segments.
#### Data Size: Dataset contained approximately 145414 rows and 11 columns, supporting exploratory analysis, KPI creation, and segmented reporting without performance limitations.

## Results and Conclusion
My analysis of the dataset revealed several strong compensation patterns across roles, experience levels, employment types, and geography. Machine Learning (ML) and Artificial Intelligence (AI) roles consistently showed salaries that were highly competitive, often matching (and in some cases rivaling) compensation levels typically associated with Engineer, Manager, and Executive positions.
When comparing employment arrangements, experienced professionals working in Full-Time and Contract roles earned noticeably higher salaries than those providing Freelance services, indicating stronger earning potential in more structured employment types.
Experience level also played a major role in compensation. Senior-level professionals had the highest salary ratio overall, followed closely by Mid-level roles. Entry-level and Executive-level roles showed similar ratios, although the salary gap between those two levels was the largest, highlighting the sharp difference in pay at the top end of leadership roles.
From a geographic standpoint, the United States ranked highest in salary by role, with Canada emerging as the second-highest-paying location, showing strong earning potential outside the U.S. market as well.
Lastly, remote work trends showed that remote roles represented only about 38% compared to on-site positions, suggesting that the majority of opportunities in this dataset still lean toward on-site work.

## Recommendations
- Identify roles/levels with below-market salaries and prioritize compensation corrections to reduce attrition risk.
- Track salary movement by year and refresh compensation benchmarks annually to stay aligned with market trends.
- Develop a defined career ladder with salary ranges per level to improve transparency, reduce pay bias, and strengthen employee growth pathways.
  
## Dashboard
[Salary Dashboard](https://public.tableau.com/app/profile/elizabeth.elizondo/viz/JobTitle_Salary_v2025_2/Dashboard1)
