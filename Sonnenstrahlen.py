# Retail Trade Turnover
# Wetter auf Stundenbasis in Zürich an 3 Orten

# https://data.stadt-zuerich.ch/dataset/ugz_meteodaten_stundenmittelwerte

url_cs_2021 = "https://data.stadt-zuerich.ch/dataset/ugz_meteodaten_stundenmittelwerte/download/ugz_ogd_meteo_h1_2021.csv"    
url_cs_2022 = "https://data.stadt-zuerich.ch/dataset/ugz_meteodaten_stundenmittelwerte/download/ugz_ogd_meteo_h1_2022.csv"
url_cs_2023 = "https://data.stadt-zuerich.ch/dataset/ugz_meteodaten_stundenmittelwerte/download/ugz_ogd_meteo_h1_2023.csv"

weather_2021 = pd.read_csv(
    url_cs_2021,
    sep=',',
    encoding='utf-8',
)
weather_2022 = pd.read_csv(
    url_cs_2022,
    sep=',',
    encoding='utf-8',
)
weather_2023 = pd.read_csv(
    url_cs_2023,
    sep=',',
    encoding='utf-8',
)

weather_2021.loc[weather_2021["Standort"] == "Zch_Rosengartenstrasse"]
weather_2021["Datum"] = pd.to_datetime(weather_2021["Datum"], format="%Y-%m-%dT%H:%M+0100")

weather_2022.loc[weather_2022["Standort"] == "Zch_Rosengartenstrasse"]
weather_2022["Datum"] = pd.to_datetime(weather_2022["Datum"], format="%Y-%m-%dT%H:%M+0100")

weather_2023.loc[weather_2023["Standort"] == "Zch_Rosengartenstrasse"]
weather_2023["Datum"] = pd.to_datetime(weather_2023["Datum"], format="%Y-%m-%dT%H:%M+0100")

concatenated_weather = pd.concat([weather_2022, weather_2023, weather_2021], ignore_index=True)
concatenated_weather= concatenated_weather.loc[concatenated_weather["Einheit"] == "W/m2"]
concatenated_weather=concatenated_weather.sort_values(by = "Datum")
concatenated_weather=concatenated_weather.loc[concatenated_weather["Datum"] >= "2021-09-28 00:00:00"]
concatenated_weather=concatenated_weather.loc[concatenated_weather["Datum"] <= "2023-11-09 00:00:00"]

concatenated_weather.to_csv("Sonnenstrahlen.csv")