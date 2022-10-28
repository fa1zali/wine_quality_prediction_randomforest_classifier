### Date created
27th Oct 2022

### Project Title
**Wine Quality Prediction using RandomForest Classifier**

### Description
A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.

For this project, we will be building a machine learning model to classify whether the wine is of *Good* or *Bad* quality based on certain chemical measurements included in the dataset. Our goal is to work through this notebook by collecting data, preprocessing it, splitting it into testing and training datasets, train the model and evaluate the accuracy of our model.

**API**

We have also created an API using FastAPI for users to interact with.
You can run the model using uvicorn on your local machine and test the API, refer to wine_quality_ml_api.py & api_testing.py.

```
uvicorn wine_quality_ml_api:app --reload
```

**StreamLit Web App**

We also created a simple web app using Streamlit.
You can run the app on your local machine using StreamLit and test the web app, refer to wine_quality_ml_streamlit.py.

```
streamlit run wine_quality_ml_streamlit.py
```

### Files used
We used the following dataset available on Kaggle to work on this project:

* [Red Wine Quality](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)

The datasets consists of several chemical predictor variables and one target variable, quality. Predictor variables includes the fixed acidity, citric acid, chlorides, density, pH, alcohol and so on.

### Credits
Thanks to Kaggle for teaching me ML :sparkles: :heart: :sparkles:
