# Retail Trade Turnover
# https://www.bfs.admin.ch/bfs/en/home/statistics/industry-services/surveys/dhu.html

from pyaxis import pyaxis

fp = r"Retail_Trade_Turnover.px"

px = pyaxis.parse(uri=fp, encoding='ISO-8859-2')

data_df = px['DATA']

data_df["Monat"] = pd.to_datetime(data_df["Monat"], format="%YM%m")

data_df["DATA"] = pd.to_numeric(data_df["DATA"], errors='coerce')

data_df["DATA"] = data_df["DATA"].round(3)


grouped_data = data_df.groupby("Branche / Warengruppe")

group_datasets = {}

for group_name, group_data in grouped_data:
    group_datasets[group_name] = group_data.copy()

for i, (group_name, group_data) in enumerate(group_datasets.items(), 1):
    globals()[f'df_{i+1}'] = group_data.copy()
