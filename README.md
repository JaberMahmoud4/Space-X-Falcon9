#   SpaceX Falcon 9 Landing Prediction

The goal is to analyze SpaceX Falcon 9 launch data and **predict whether the first stage booster will land successfully**. The project demonstrates end-to-end data science skills including data collection, cleaning, visualization, and machine learning.

---

##  Project Overview

SpaceX’s reusable boosters significantly reduce launch costs. This project uses historical launch data to:

* Explore and visualize trends in successful and failed landings.
* Build predictive models to forecast landing outcomes.
* Present interactive dashboards for data exploration.

---

##  Tools & Technologies

* **Languages**: Python
* **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Plotly, Folium, Scikit-learn
* **Data Sources**: SpaceX API, Wikipedia
* **SQL**: For querying launch data
* **Dashboards**: Plotly Dash for interactive visualizations

---

##  Project Steps

1. **Data Collection & Cleaning**

   * Gathered data via SpaceX API and Wikipedia scraping.
   * Handled missing values, duplicates, and encoded categorical features.

2. **Exploratory Data Analysis (EDA)**

   * Analyzed payloads, launch sites, orbits, and booster versions.
   * Visualized data trends with static (Matplotlib/Seaborn) and interactive plots (Plotly/Folium).

3. **Predictive Modeling**

   * Built classifiers: Logistic Regression, Decision Tree, KNN, SVM.
   * Hyperparameter tuning and cross-validation for model optimization.
   * Evaluated models using accuracy scores and confusion matrices.

4. **Interactive Dashboard**

   * Created a Plotly Dash dashboard to explore launches, payloads, and landing outcomes.

---

##  Key Insights

* Launch site and booster version have a significant impact on landing success.
* Payload mass influences outcomes but is less critical than technical booster details.
* Machine learning models can predict landings with **\~95% accuracy**.

---

##  Repository Structure

```
├── data/                  # Raw and processed datasets
├── notebooks/             # Jupyter notebooks for EDA and modeling
├── dashboard/             # Plotly Dash dashboard files
├── README.md
└── requirements.txt       # Python dependencies
```

---

##  How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/JaberMahmoud4/Space-X-Falcon9.git
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run Jupyter notebooks for EDA and modeling.
4. Launch the dashboard:

   ```bash
   python dashboard/app.py
   ```

---

##  References

* [SpaceX API](https://api.spacexdata.com/)
* [Wikipedia: Falcon 9](https://en.wikipedia.org/wiki/Falcon_9)

---
