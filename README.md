IBM Data Science Capstone – SpaceX Falcon 9 Landing Prediction

This is the final project of the IBM Data Science Professional Certificate. The goal is to analyze SpaceX Falcon 9 launch data and predict whether the first stage booster will land successfully. The project demonstrates end-to-end data science skills including data collection, cleaning, visualization, and machine learning.

Project Overview

SpaceX’s reusable boosters significantly reduce launch costs. This project uses historical launch data to:

Explore and visualize trends in successful and failed landings.

Build predictive models to forecast landing outcomes.

Present interactive dashboards for data exploration.

Tools & Technologies

Languages: Python

Libraries: Pandas, NumPy, Matplotlib, Seaborn, Plotly, Folium, Scikit-learn

Data Sources: SpaceX API, Wikipedia

SQL: For querying launch data

Dashboards: Plotly Dash for interactive visualizations

Project Steps

Data Collection & Cleaning

Gathered data via SpaceX API and Wikipedia scraping.

Handled missing values, duplicates, and encoded categorical features.

Exploratory Data Analysis (EDA)

Analyzed payloads, launch sites, orbits, and booster versions.

Visualized data trends with static (Matplotlib/Seaborn) and interactive plots (Plotly/Folium).

Predictive Modeling

Built classifiers: Logistic Regression, Decision Tree, KNN, SVM.

Hyperparameter tuning and cross-validation for model optimization.

Evaluated models using accuracy scores and confusion matrices.

Interactive Dashboard

Created a Plotly Dash dashboard to explore launches, payloads, and landing outcomes.

Key Insights

Launch site and booster version have a significant impact on landing success.

Payload mass influences outcomes but is less critical than technical booster details.

Machine learning models can predict landings with ~95% accuracy.

Repository Structure
├── data/                  # Raw and processed datasets
├── notebooks/             # Jupyter notebooks for EDA and modeling
├── dashboard/             # Plotly Dash dashboard files
├── README.md
└── requirements.txt       # Python dependencies

How to Run

Clone the repository:

git clone https://github.com/yourusername/spacex-capstone.git


Install dependencies:

pip install -r requirements.txt


Run Jupyter notebooks for EDA and modeling.

Launch the dashboard:

python dashboard/app.py

References

SpaceX API

Wikipedia: Falcon 9

IBM Data Science Professional Certificate, Capstone Project
