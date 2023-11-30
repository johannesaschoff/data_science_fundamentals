# Urlaubstage und Public Holidays

import requests
import pandas as pd

# https://www.openholidaysapi.org/en/#school-holidays

api_url_p = "https://openholidaysapi.org/PublicHolidays"
api_url_s = "https://openholidaysapi.org/SchoolHolidays"

params = {
    "countryIsoCode": "CH",

    "validFrom": "2022-03-03",
    "validTo": "2023-11-13"
}

headers = {'accept': 'text/json'}

response_p = requests.get(api_url_p, params=params, headers=headers)
response_s = requests.get(api_url_s, params=params, headers=headers)

holidays_data_p = response_p.json()
holidays_data_s = response_s.json()
holidays_df_p = pd.DataFrame(holidays_data_p)
holidays_df_s = pd.DataFrame(holidays_data_s)

concatenated_df = pd.concat([holidays_df_p, holidays_df_s], ignore_index=True)


extract_text = lambda col: col[0]["text"] if col else None
concatenated_df["publicHoliday"] = concatenated_df["name"].apply(extract_text)

concatenated_df["startDate"] = pd.to_datetime(concatenated_df["startDate"], format="%Y-%m-%d")
concatenated_df["endDate"] = pd.to_datetime(concatenated_df["endDate"], format="%Y-%m-%d")

concatenated_df["subdivision_short_names"] = concatenated_df["subdivisions"].apply(lambda x: [entry["shortName"] for entry in x] if isinstance(x, list) else [])

all_unique_short_names = set()
_ = concatenated_df["subdivision_short_names"].apply(lambda x: all_unique_short_names.update(x))

for short_name in all_unique_short_names:
    concatenated_df[short_name] = concatenated_df["subdivision_short_names"].apply(lambda x: short_name in x)

concatenated_df.drop(columns = ["id", "name", "subdivisions", "subdivision_short_names", "comment"], axis = 1, inplace = True)

concatenated_df.to_csv("holidays_data.csv", index=False)

