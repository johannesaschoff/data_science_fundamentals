# Data Science Fundamentals Project

## Project Overview

The goal of this project is to develop a predictive model that estimates pedestrian traffic on an hourly basis at Bahnhofstrasse Zürich. The model aims to assist non-governmental organizations (NGOs) in determining optimal locations and times to set up stands or initiatives based on various features like weather conditions, seasons, GDP, and public holidays.

## Dataset

The dataset contains hourly pedestrian counts, weather conditions, timestamps, and other relevant information for Bahnhofstrasse Zürich. It is sourced from [https://data.stadt-zuerich.ch/dataset/hystreet_fussgaengerfrequenzen].

![Plot of the three zones where the measured the pedestrians at Bahnhofstrasse Zurich](https://github.com/johannesaschoff/data_science_fundamentals/blob/main/target_preprocessing/bahnhofstrasse_zones_plot.png?raw=true)

### Dataset Features:

- Timestamp: Date and time of the pedestrian count.
- Pedestrians_count: Number of pedestrians counted.
- Weather_condition: Description of the weather at the time of the count.
- Hourly traffic in Zurich
- Hourly sunshine in Zurich
- Retail Trade Turnover Switzerland
- Consumer Price Index Switzerland
- Hotel Guests in Zurich
- Population of Zurich
- Weekday
- School Holidays
- Big Events
- Closed Stores

## Objective

NGOs often set up stands or initiatives to raise awareness, collect donations, or engage with the public. Understanding the foot traffic patterns helps in identifying the best time and location to maximize engagement. The predictive model created in this project will be utilized to recommend ideal locations and timings for the NGOs to set up stands.

## Model Development

The predictive model will be developed using various machine learning techniques to predict pedestrian counts based on the features provided in the dataset. The model will consider the historical pedestrian data along with the weather, season, GDP, and public holiday information to make hourly predictions.

## Usage

To utilize the model predictions, the output will provide insights into the expected pedestrian counts at different locations and times, assisting NGOs in making informed decisions about stand setups.

## Requirements

The following tools and libraries were used in this project:

- Python
- Pandas
- Scikit-learn
- GeoPandas
- Matplotlib
- Keras

## Getting Started

1. **Data Collection:** Ensure you have the updated dataset, preferably in CSV format.
2. **Data Preprocessing:** Clean the data, handle missing values, and perform feature engineering as required.
3. **Model Development:** Train and test the predictive model using appropriate machine learning algorithms.
4. **Prediction:** Use the model to predict pedestrian counts based on new data.

### Contributors

We'd like to thank the following individuals who have contributed to this project:

- Anne Bally
- Berit Schrader
- Richard Eden
- Johannes Aschoff

## Acknowledgments

- Acknowledge any sources or references used in the project.
