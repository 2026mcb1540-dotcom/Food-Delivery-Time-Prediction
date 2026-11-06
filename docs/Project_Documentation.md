# AI101 MINI PROJECT

# FOOD DELIVERY TIME PREDICTION USING MACHINE LEARNING

**Project Documentation**

**Department:** Mathematics and Computing

**Project Team:** 4 Members

**Project Domain:** Artificial Intelligence and Machine Learning

---

## 1. INTRODUCTION

### 1.1 Project Overview

Food delivery services have become an important part of modern life. Customers increasingly expect their orders to arrive within the estimated delivery time. However, accurately predicting delivery duration is challenging because it depends on several factors, including delivery distance, traffic conditions, weather, food preparation time and courier experience.

This project aims to develop a machine learning-based system that predicts food delivery time using relevant order and delivery-related attributes.

### 1.2 Problem Statement

To develop a machine learning model that predicts food delivery time using factors such as delivery distance, weather, traffic conditions, food preparation time, vehicle type, and courier experience

The main objectives of this project are:

1. Analyse historical food delivery data.
2. Identify important factors influencing delivery duration.
3. Perform Exploratory Data Analysis (EDA).
4. Clean and preprocess the dataset.
5. Implement and compare suitable regression algorithms.
6. Evaluate model performance using appropriate evaluation metrics.
7. Develop a reliable food delivery time prediction system.

---

## 2. DATASET OVERVIEW AND INITIAL INSPECTION

### 2.1 Dataset Description

The project utilizes a structured dataset named `Food_Delivery_Times.csv`, consisting of 1,000 records and 9 attributes. The dataset contains numerical and categorical information related to food delivery operations.

### 2.2 Dataset Attributes

The dataset contains the following attributes:

| Attribute | Description |
|---|---|
| Order_ID | Unique order identification number |
| Distance_km | Delivery distance in kilometres |
| Weather | Weather conditions |
| Traffic_Level | Traffic intensity |
| Time_of_Day | Time period of delivery |
| Vehicle_Type | Type of delivery vehicle |
| Preparation_Time_min | Food preparation duration in minutes |
| Courier_Experience_yrs | Courier experience in years |
| Delivery_Time_min | Actual delivery duration in minutes |

### 2.3 Target Variable

The target variable selected for prediction is `Delivery_Time_min`.

Since delivery time is a continuous numerical value, this project is treated as a **regression problem**.

### 2.4 Initial Dataset Inspection

The dataset was loaded into Python using the Pandas library.

The following functions were used for initial inspection:

- `head()` – To display the first few records.
- `shape` – To identify the number of rows and columns.
- `info()` – To examine column names, data types and non-null values.
- `isnull().sum()` – To identify missing values.

The initial inspection confirmed that the dataset contains 1,000 rows and 9 columns.

### 2.5 Missing Value Analysis

The `isnull().sum()` function was used to identify missing values in the dataset.

The initial inspection revealed the following:

| Attribute | Missing Values |
|---|---:|
| Weather | 30 |
| Traffic_Level | 30 |
| Time_of_Day | 30 |
| Courier_Experience_yrs | 30 |
| Other attributes | 0 |

Each of the four affected columns contains 30 missing entries, representing 3% of the total records per column.

These missing values will be further investigated and handled during the data preprocessing stage.

### 2.6 Initial Findings

Based on the initial dataset inspection:

- The dataset contains both numerical and categorical features.
- Four attributes contain missing values.
- The target variable, `Delivery_Time_min`, has no missing entries.
- Further exploratory data analysis is required to understand relationships between the input features and delivery time.

---

## 3. PROJECT DEVELOPMENT STATUS

The project is currently in its initial data exploration stage.

The following activities have been completed:

1. Dataset selection and initial inspection.
2. Loading the dataset into Python using Pandas.
3. Examining the dataset structure and attributes.
4. Identifying missing values.

The next stages will involve exploratory data analysis, data preprocessing, model development and performance evaluation.

---

## 4. TECHNOLOGIES AND LIBRARIES

The following tools and libraries are being used for project development:

- **Python:** Primary programming language.
- **Google Colab:** Cloud-based environment for writing and executing Python code.
- **Pandas:** Data loading and manipulation.
- **NumPy:** Numerical computations.
- **Matplotlib:** Data visualization.
- **Seaborn:** Statistical data visualization.
- **Scikit-learn:** Machine learning model development and evaluation.
- **GitHub:** Project code management and version control.

---

## 5. EXPECTED OUTCOME

The expected outcome is a machine learning model capable of predicting food delivery duration based on relevant order-related features.

The project will also identify important factors that influence delivery time and evaluate how effectively different regression algorithms perform on the selected dataset.

**Note:** The final model results and conclusions will be added after model training and evaluation.
