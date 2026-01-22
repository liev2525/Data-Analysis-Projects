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
Dataset Source: Derived

### Description:

This dataset and analysis were completed as part of a graduate-level capstone project for the master’s program in Information Science 2023. In collaboration with a cohort, I helped to develop a mock company—Cave Shippers LLC—where my responsibility was to conduct an end-to-end analysis of historical performance and future sales potential for shipping containers produced using various material types. 
Through this assessment, I delivered insights and reporting to support key business questions, including:
Developing an interactive dashboard to evaluate quarterly sales trends and units sold
Performing a 10-year sales forecast to estimate long-term performance
Conducting statistical analysis to assess material type performance, order frequency, and customer-level sales behavior

## Methodology
Created a mock dataset from a similarly aligned company of shipment data, and assess the dataset’s size and metadata to understand its structure and determine the appropriate handling approach based on each field’s attributes. 

## Task
To build a Tableau dashboard having visualizations driven by MySQL queries to highlight key trends in work type, remote ratio, and salary by work year. 

## Dataset Features
- carrier: carrier type
- customer: customer number
- desitnation_port: locations of where shipping contents were sent
- material_type: types of material which made up shipping container
- order_date: date of order
- order_id: id belonging to individual order
- origin_port: location where shipper container derived from
- plant_code:  code used for plant of origin manufactured
- product_id:  id for product type
- sales: company sales
- service_level: type of delivery to customer
- ship_ahead_day_count: days shipped early
- ship_late_day_count: days product was shipped late
- weight: weight of shipping container prior to contents added
- retail: cost of shipping container to customer
- unit_quantity: quantity of units sold

## Exploratory Analysis
During exploratory analysis, I assessed sales volume, revenue performance, and shipment characteristics to identify key trends and anomalies across material types and time periods. Results showed that Steel and Tungsten were among the strongest-performing materials, while Polyethylene consistently ranked as the lowest-selling material type. Overall, average sales across material types were approximately $600M, indicating stable baseline demand across most categories. Sales performance also revealed that higher revenue was sometimes generated from fewer transactions, suggesting certain premium products yield greater returns. Weight-based trends indicated most shipments fell under 1,000 lbs, with a small number of outliers requiring further review. Quarterly distribution analysis showed greater variability and outliers in Q3, while order frequency revealed a notable anomaly tied to a high-performing order, potentially influenced by seasonal purchasing patterns.

## Visualization Highlights
- [Google Analysis Visualizations](https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Fview%2Fcavellcshippers%2Fdata-analysis&sa=D&sntz=1&usg=AOvVaw2qzA48tiEnjxde1tIV2gtk)
- [Tableau Visualizations](https://public.tableau.com/app/profile/elizabeth.elizondo/vizzes)


## Dataset Quality Assessment
#### Data Validity: Data was modified to ensure it met the required validity to accomodate the scope of the project.
#### Data Accessibility: Dataset was derived as mock data and imported into MySQL for analysis.
#### Data Completeness: Addressed gaps through filtering, imputation and insertion to modify data for completeness where appropriate.
#### Data Consistency: Standardized categories and naming conventions to ensure consistent grouping and reliable comparative analysis across segments.
#### Data Size: 6971 rows and 16 columns of data.

## Results and Conclusion
#### Sales Insights:
- Sales lows 9,181,000 with 37 count of sales, versus 9,181,000 with only 24 count of
sales made 10,296,000 - This indicates less sales generated a higher yield return value
for a specific product that may have cost more to the consumer.
- Sales high was 1,685 count of sales ylelded $357,770,750 compared to its 2nd highest
sales count at 1,054 returning sales dollar amount of $25,144,000.
- Sales by weight appear to be approximately under 1000 lbs. However a couple of
outliers are present.
- Unit quantity trend positive along with sales increasing
- Unit quantity have an even spread up to 200 range, despite weight fluctuations under
1000 lbs.
#### Statistical Insights:
- Q1: The interquartile range (IQR) allows is positively skewed, does contain some
outliers however data is less dispersed to due starting sales frequency at a low.
- Q2: IQR has normal distribution with a few outliers which have wider dispersion
with a greater increase in sales.
- Q3: IQR is positively skewed similar Q1 with the most outliers, an indicator that
sales are more inconsistent this quarter.
- Q4: Data points only pinpointing few sales data generated for Q4
Insights:
- All shipper material types fall less than or near -0.5 whereas Steel falls slightly over 2.2
which indicates that it an outlier with steel as it is the material most sold out of all
categories
- Order date frequency was observed for its z-score and it was determined that quarter
Contains an anomaly at 4.027 for order no. 1447371268 which indicates a greater
frequency sold than normal, this could be attributed to the approaching holiday season
and needs further investigation.
- Sales by customer were all consistent within the +3 z-score permissible limitation.


## Recommendations
Based on the sales and statistical findings, the business should prioritize high-yield product categories, particularly those generating stronger revenue with fewer transactions, and further investigate top-performing spikes (e.g., unusually high-frequency orders tied to seasonal demand). Given that most sales are concentrated under 1,000 lbs with few outliers, inventory and shipping strategies should be optimized around standard weight ranges while flagging exceptions for special handling. Additionally, since steel is a major sales outlier, the company should strengthen supplier planning and pricing strategy for steel-related materials to reduce stock risk and capitalize on its demand. Finally, because Q3 shows the highest inconsistency and most outliers, leadership should implement closer quarterly monitoring and forecasting adjustments to stabilize performance and improve planning accuracy.
  
## Dashboard
[Salary Dashboard](https://sites.google.com/view/cavellcshippers/data-analysis)
