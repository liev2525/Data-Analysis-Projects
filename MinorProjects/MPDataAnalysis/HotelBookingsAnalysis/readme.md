# Hotel Analytics Dashboard – BRD + KPI Reporting Implementation

## 🛠 Tools Used
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=Snowflake&logoColor=white)

<img width="1647" height="875" alt="Dashboard" src="https://github.com/user-attachments/assets/32cbff1b-ec6b-4a74-abb0-279d526d3df0" />

## Table of Contents
- [Overview](###Overview)
- [Business Context](##BusinessContext)
- [Objectives](##Objectives)
- [Dataset](##Dataset)
- [Functional Requirements](##FunctionalRequirements)
- [Data Architecture](##DataArchitecture)
- [Deliverables](##Deliverables)
- [Dataset Quality & Validation](##DatasetQuality&Validation)
- [Testing & Validation](##Testing&Validation)
- [Screenshots](##Screenshots)
- [Business Impact](##BusinessImapct)

### 📌 Overview 
This pull request delivers a business-driven analytics solution by translating stakeholder requirements into a structured dashboard and data model. The implementation focuses on improving visibility into revenue performance, booking trends, and city-level insights using standardized and validated data.

### 🏢 Business Context

The table contains data on employee salaries, including details such as work year, experience level, employment type, job title, and salary in USD. It also includes information about employee and company locations, remote work ratios, and company size. This data can be used for salary benchmarking, analyzing compensation trends across different roles and locations, and understanding the impact of remote work on salaries.

### 🎯 Objectives
- Standardize and clean raw booking data
- Enable monthly revenue and booking trend analysis
- Identify top-performing cities by revenue
- Segment bookings by type and status
- Deliver clear KPIs for executive decision-making
  
### ⚙️ Functional Requirements
- Data cleansing (duplicates, nulls, inconsistent formats)
- Date standardization and transformation
- Aggregation to monthly grain
- KPI calculation (Total Revenue, Total Bookings)
- Dashboard visualizations:
- Revenue by Month (Line Chart)
- Bookings by Month (Line Chart)
- Top Cities by Revenue (Bar Chart)
- Bookings by Type (Bar Chart)
- Bookings by Status (Bar Chart)

### 🧱 Data Architecture
- Bronze Layer: Raw ingestion (original dataset)
- Silver Layer: Cleaned and standardized data
- Gold Layer: Aggregated metrics for reporting

![Flow Diagram](MinorProjects/MPDataAnalysis/HotelBookingsAnalysis/images/FlowDiagramDark.png)
  
### 📊 Deliverables
- Clean, validated dataset (analysis-ready)
- KPI-driven dashboard
- Monthly aggregated metrics
- Business-aligned visualizations
- Documentation (BRD + README)

### ✅ Dataset Quality & Validation
- Removed duplicate records
- Handled missing/null values
- Standardized date formats
- Validated revenue and booking counts against source data

### 🧪 Testing & Validation
- Verified KPI calculations against aggregated totals
- Cross-checked monthly trends for consistency
- Confirmed dashboard accuracy with sample scenarios

### 📸 Screenshots
Flow Diagram
<img width="782" height="351" alt="FlowDiagramDark" src="https://github.com/user-attachments/assets/ae4a452a-2388-4279-ada0-29cbbb9189a9" />


### 🚀 Business Impact
- Enables faster, data-driven decision-making
- Improves visibility into revenue and booking performance
- Provides a scalable foundation for future analytics enhancements
