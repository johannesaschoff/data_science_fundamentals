# Kaufkraftparität

# https://www.bfs.admin.ch/bfs/de/home/statistiken/preise/landesindex-konsumentenpreise.assetdetail.29065706.html
# Die columns zwischen Datum und den Prozentanzahlen zeigen die Veränderungen, skaliert auf das jeweilige Jahr als Basisjahr
# % m-1 zeigt die monatliche Veränderung und m-12 zeigt die jährliche Veränderung

import pandas as pd
lik = pd.read_excel("Konsumentenpreise_CH.xlsx")
lik["Datum / Date"] = pd.to_datetime(lik["Datum / Date"], format="%Y-%m-%d")
lik.loc[lik["Datum / Date"] >= "2022-03-01"]

import pandas as pd

lik = pd.read_excel("Konsumentenpreise_CH.xlsx")
lik["Datum / Date"] = pd.to_datetime(lik["Datum / Date"], format="%Y-%m-%d")
lik = lik.loc[lik["Datum / Date"] >= "2022-03-01"]

lik

