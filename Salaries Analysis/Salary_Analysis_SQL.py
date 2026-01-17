# Databricks notebook source
# MAGIC %md
# MAGIC ## EXPLORATORY OVERVIEW

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM read_files(
# MAGIC   '/Volumes/dp_analysis/dp_analysis_1/dp_vol1/salaries.csv',
# MAGIC   format => 'csv'
# MAGIC )
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_rows
# MAGIC FROM dp_analysis.default.salaries;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE EXTENDED dp_analysis.default.salaries;

# COMMAND ----------

spark.sql("DESCRIBE DETAIL dp_analysis.default.salaries")

# COMMAND ----------

# MAGIC %sql DESCRIBE dp_analysis.default.salaries

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM dp_analysis.default.salaries

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     COUNT(DISTINCT job_title) AS job_title_distinct,
# MAGIC     COUNT(DISTINCT company_location) AS company_location_distinct
# MAGIC FROM dp_analysis.default.salaries;

# COMMAND ----------

# DBTITLE 1,NULL OR MISSING VALUES
# MAGIC %sql
# MAGIC SELECT
# MAGIC     SUM(CASE WHEN experience_level IS NULL OR experience_level = '' THEN 1 ELSE 0 END) AS experience_level_missing,
# MAGIC     SUM(CASE WHEN company_location IS NULL OR company_location = '' THEN 1 ELSE 0 END) AS company_location_missing
# MAGIC FROM dp_analysis.default.salaries;

# COMMAND ----------

# DBTITLE 1,JOB TITLE BY FREQUENCY
# MAGIC %sql
# MAGIC SELECT job_title, COUNT(*) AS job_title_frequency
# MAGIC FROM dp_analysis.default.salaries
# MAGIC GROUP BY job_title
# MAGIC ORDER BY job_title_frequency DESC;

# COMMAND ----------

# DBTITLE 1,MIN/MAX/AVG SALARIES
# MAGIC %sql
# MAGIC SELECT
# MAGIC   job_title,
# MAGIC   COUNT (*) AS total_count,
# MAGIC   MIN(salary_in_usd) AS min_salary,
# MAGIC   MAX(salary_in_usd) AS max_salary,
# MAGIC   ROUND(AVG(salary), 0) AS avg_salary,
# MAGIC   PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary_in_usd) AS median_salary,
# MAGIC   STDDEV(salary_in_usd) AS stddev_val
# MAGIC FROM dp_analysis.default.salaries WHERE salary_currency = 'USD' GROUP BY job_title SORT BY AVG(salary_in_usd) DESC
# MAGIC ;

# COMMAND ----------

# DBTITLE 1,EXP LEVEL VS. SALARY CORRELATION
# MAGIC %sql
# MAGIC SELECT corr(CASE WHEN experience_level = 'EN' THEN 1 WHEN experience_level = 'MI' THEN 2 WHEN experience_level = 'SE' THEN 3 
# MAGIC WHEN experience_level = 'EX' THEN 4 ELSE NULL END, salary) AS correlation
# MAGIC FROM dp_analysis.default.salaries;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT job_title, ROUND(AVG(salary), 0) AS avg_salary
# MAGIC FROM dp_analysis.default.salaries
# MAGIC WHERE salary_currency = 'USD'
# MAGIC GROUP BY job_title
# MAGIC ORDER BY avg_salary DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# DBTITLE 1,AVERAGE SALARY BY JOB TITLE
# MAGIC %sql
# MAGIC SELECT job_title, ROUND(AVG(salary), 0) AS avg_salary
# MAGIC FROM dp_analysis.default.salaries
# MAGIC GROUP BY job_title
# MAGIC ORDER BY avg_salary DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ## DATA ANALYSIS

# COMMAND ----------

# DBTITLE 1,Create Table
# MAGIC %sql
# MAGIC CREATE TABLE salaries_raw (
# MAGIC     work_year INT,
# MAGIC     experience_level VARCHAR(2),
# MAGIC     employment_type VARCHAR(2),
# MAGIC     job_title STRING,
# MAGIC     salary INT,
# MAGIC     salary_currency VARCHAR(5),
# MAGIC     salary_in_usd INT,
# MAGIC     employee_residence VARCHAR(2),
# MAGIC     remote_ratio INT,
# MAGIC     company_location VARCHAR(2),
# MAGIC     company_size VARCHAR(1)
# MAGIC );

# COMMAND ----------

# DBTITLE 1,Bronze Layer Raw Ingest
# MAGIC %sql
# MAGIC COPY INTO salaries_raw
# MAGIC FROM '/Volumes/dp_analysis/dp_analysis_1/dp_vol1/salaries.csv'
# MAGIC FILEFORMAT = CSV
# MAGIC FORMAT_OPTIONS (
# MAGIC   'header' = 'true',
# MAGIC   'inferSchema' = 'true'
# MAGIC );
# MAGIC

# COMMAND ----------

# DBTITLE 1,Silver Layer: Clean/Standardize
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE salaries_clean AS
# MAGIC SELECT
# MAGIC     work_year,
# MAGIC     CASE experience_level
# MAGIC         WHEN 'EN' THEN 'Entry'
# MAGIC         WHEN 'MI' THEN 'Mid'
# MAGIC         WHEN 'SE' THEN 'Senior'
# MAGIC         WHEN 'EX' THEN 'Executive'
# MAGIC     END AS experience_level,
# MAGIC     CASE employment_type
# MAGIC         WHEN 'FT' THEN 'Full-Time'
# MAGIC         WHEN 'PT' THEN 'Part-Time'
# MAGIC         WHEN 'CT' THEN 'Contract'
# MAGIC     END AS employment_type,
# MAGIC     job_title,
# MAGIC     salary_in_usd,
# MAGIC     employee_residence,
# MAGIC     remote_ratio,
# MAGIC     company_location,
# MAGIC     CASE company_size
# MAGIC         WHEN 'S' THEN 'Small'
# MAGIC         WHEN 'M' THEN 'Medium'
# MAGIC         WHEN 'L' THEN 'Large'
# MAGIC     END AS company_size
# MAGIC FROM salaries_raw
# MAGIC WHERE salary_in_usd IS NOT NULL;
# MAGIC
# MAGIC SELECT * FROM salaries_clean;

# COMMAND ----------

# DBTITLE 1,Salary by Experience
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE salary_gold_experience AS
# MAGIC SELECT
# MAGIC     experience_level,
# MAGIC     ROUND(AVG(salary_in_usd), 2) AS avg_salary_usd,
# MAGIC     COUNT(*) AS employee_count
# MAGIC FROM salaries_clean
# MAGIC GROUP BY experience_level;
# MAGIC
# MAGIC SELECT * FROM salary_gold_experience
# MAGIC ORDER BY avg_salary_usd DESC
# MAGIC LIMIT 10;
# MAGIC

# COMMAND ----------

# DBTITLE 1,Gold: Avg Salary by Job Title
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE salary_gold_job_title AS
# MAGIC SELECT
# MAGIC     job_title,
# MAGIC     ROUND(AVG(salary_in_usd), 2) AS avg_salary_usd,
# MAGIC     COUNT(*) AS role_count
# MAGIC FROM salaries_clean
# MAGIC GROUP BY job_title
# MAGIC HAVING COUNT(*) >= 10;
# MAGIC
# MAGIC SELECT * FROM salary_gold_job_title
# MAGIC ORDER BY avg_salary_usd DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE salary_gold_remote AS
# MAGIC SELECT
# MAGIC     CASE remote_ratio
# MAGIC         WHEN 0 THEN 'On-Site'
# MAGIC         WHEN 50 THEN 'Hybrid'
# MAGIC         WHEN 100 THEN 'Fully Remote'
# MAGIC     END AS work_type,
# MAGIC     ROUND(AVG(salary_in_usd), 2) AS avg_salary_usd,
# MAGIC     COUNT(*) AS employee_count
# MAGIC FROM salaries_clean
# MAGIC GROUP BY remote_ratio;
# MAGIC
# MAGIC select * from salary_gold_remote
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE salary_gold_country AS SELECT
# MAGIC     CASE company_location
# MAGIC         WHEN 'US' THEN 'United States'
# MAGIC         WHEN 'CA' THEN 'Canada'
# MAGIC         WHEN 'GB' THEN 'United Kingdom'
# MAGIC         WHEN 'DE' THEN 'Germany'
# MAGIC         WHEN 'FR' THEN 'France'
# MAGIC         WHEN 'IN' THEN 'India'
# MAGIC         WHEN 'ES' THEN 'Spain'
# MAGIC         WHEN 'AU' THEN 'Australia'
# MAGIC         WHEN 'NL' THEN 'Netherlands'
# MAGIC         WHEN 'IT' THEN 'Italy'
# MAGIC         WHEN 'BR' THEN 'Brazil'
# MAGIC         WHEN 'PL' THEN 'Poland'
# MAGIC         WHEN 'PT' THEN 'Portugal'
# MAGIC         WHEN 'RU' THEN 'Russia'
# MAGIC         WHEN 'IE' THEN 'Ireland'
# MAGIC         WHEN 'CH' THEN 'Switzerland'
# MAGIC         WHEN 'UA' THEN 'Ukraine'
# MAGIC         WHEN 'AT' THEN 'Austria'
# MAGIC         WHEN 'BE' THEN 'Belgium'
# MAGIC         WHEN 'MX' THEN 'Mexico'
# MAGIC         WHEN 'RO' THEN 'Romania'
# MAGIC         WHEN 'GR' THEN 'Greece'
# MAGIC         WHEN 'TR' THEN 'Turkey'
# MAGIC         WHEN 'SG' THEN 'Singapore'
# MAGIC         WHEN 'AR' THEN 'Argentina'
# MAGIC         WHEN 'CL' THEN 'Chile'
# MAGIC         WHEN 'DK' THEN 'Denmark'
# MAGIC         WHEN 'FI' THEN 'Finland'
# MAGIC         WHEN 'SE' THEN 'Sweden'
# MAGIC         WHEN 'CZ' THEN 'Czech Republic'
# MAGIC         WHEN 'HU' THEN 'Hungary'
# MAGIC         WHEN 'IL' THEN 'Israel'
# MAGIC         WHEN 'ZA' THEN 'South Africa'
# MAGIC         WHEN 'NO' THEN 'Norway'
# MAGIC         WHEN 'EE' THEN 'Estonia'
# MAGIC         WHEN 'LT' THEN 'Lithuania'
# MAGIC         WHEN 'SK' THEN 'Slovakia'
# MAGIC         WHEN 'BG' THEN 'Bulgaria'
# MAGIC         WHEN 'HR' THEN 'Croatia'
# MAGIC         WHEN 'SI' THEN 'Slovenia'
# MAGIC         WHEN 'LU' THEN 'Luxembourg'
# MAGIC         WHEN 'LV' THEN 'Latvia'
# MAGIC         WHEN 'NZ' THEN 'New Zealand'
# MAGIC         WHEN 'JP' THEN 'Japan'
# MAGIC         WHEN 'CN' THEN 'China'
# MAGIC         WHEN 'AE' THEN 'United Arab Emirates'
# MAGIC         WHEN 'TH' THEN 'Thailand'
# MAGIC         WHEN 'MY' THEN 'Malaysia'
# MAGIC         WHEN 'KR' THEN 'South Korea'
# MAGIC         WHEN 'EG' THEN 'Egypt'
# MAGIC         WHEN 'NG' THEN 'Nigeria'
# MAGIC         WHEN 'CO' THEN 'Colombia'
# MAGIC         WHEN 'PE' THEN 'Peru'
# MAGIC         WHEN 'PH' THEN 'Philippines'
# MAGIC         WHEN 'ID' THEN 'Indonesia'
# MAGIC         WHEN 'SA' THEN 'Saudi Arabia'
# MAGIC         WHEN 'PK' THEN 'Pakistan'
# MAGIC         ELSE company_location
# MAGIC     END AS country,
# MAGIC     ROUND(AVG(salary_in_usd), 2) AS avg_salary_usd,
# MAGIC     COUNT(*) AS role_count
# MAGIC FROM salaries_clean
# MAGIC GROUP BY company_location
# MAGIC HAVING COUNT(*) >= 20;
# MAGIC
# MAGIC SELECT * FROM salary_gold_country
# MAGIC ORDER BY avg_salary_usd DESC
# MAGIC LIMIT 10;