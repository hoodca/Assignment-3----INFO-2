# Assignment-3----INFO-2
# Iris Data Analysis Project

## Overview
This project analyzes iris flower measurements by combining two datasets—one containing **sepal** measurements and one containing **petal** measurements. After merging the datasets, the project computes:

- Pairwise correlations between all numeric variables  
- Mean, median, and standard deviation for each species  
- A comparison of species similarity based on statistical measurements  

The goal is to understand how the three iris species differ and which species are most similar.

---

## Dataset Description
Two CSV files are used:

- `Petal_Data.csv`  
- `Sepal_Data.csv`

Each file contains:

- `sample_id`  
- `species`  
- Two numeric measurements (petal or sepal)

After merging, the final dataset includes:

- `sepal_length`  
- `sepal_width`  
- `petal_length`  
- `petal_width`

---

## Data Cleaning
The following steps were performed:

1. Loaded CSV files using `pandas.read_csv()`
2. Removed unwanted index columns such as `Unnamed: 0`
3. Converted numeric columns to `float`
4. Merged datasets on `sample_id` and `species`
5. Verified data types and cleaned missing values

---

## Statistical Analysis

### **1. Correlation Matrix**
A correlation matrix was generated for:

- sepal_length  
- sepal_width  
- petal_length  
- petal_width  

There are **6 unique pairwise comparisons**.  
These correlations help identify which measurements move together and how strongly.

---

### **2. Summary Statistics (per species)**

For each species, the following were computed:

- **Mean**  
- **Median**  
- **Standard deviation**  

These values help compare species based on central tendency and variability.

---

## Species Similarity Findings

### Most Similar: **Versicolor & Virginica**
These two species show:

- Similar sepal lengths and widths  
- Strong correlations between petal_length and petal_width  
- Overlapping ranges in petal measurements  
- Comparable standard deviations  

Their measurements cluster closely, making them the most alike.

---

### Least Similar: **Setosa**
Setosa differs significantly:

- Much smaller petal_length and petal_width  
- Distinct sepal proportions  
- Lower correlations between variables  
- Lower variability overall  

Setosa stands out as the most unique species in the dataset.

---

## Class Design

### **Class: `IrisSample`**
Represents a single iris flower.

**Attributes**
- `sample_id`  
- `species`  
- `sepal_length`  
- `sepal_width`  
- `petal_length`  
- `petal_width`  

**Methods**
- `to_dict()` — returns the sample as a dictionary  
- `describe()` — prints all measurements  

---

### **Class: `IrisDataset`**
Handles loading, cleaning, merging, and analyzing the dataset.

**Attributes**
- `df` — main pandas DataFrame  
- `numeric_cols` — list of numeric measurement columns  

**Methods**
- `load_data()`  
- `clean_data()`  
- `merge_data()`  
- `compute_correlations()`  
- `compute_summary_stats()`  

---

## Limitations
- Assumes all measurements are accurate  
- No outlier removal  
- No visualizations included  
- Only supports the three iris species in the dataset  

---

## How to Run
```bash
pip install pandas
python assignment_3.py
