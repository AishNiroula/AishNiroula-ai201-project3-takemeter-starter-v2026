import pandas as pd
d = pd.read_csv("labels.csv", keep_default_na=False)
todo = d[d.label == ""].head(40)
for i, t in todo.iterrows():
    print(f"[{i}] {t.text[:350]}\n")