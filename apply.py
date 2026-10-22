import pandas as pd, re
d = pd.read_csv("labels.csv", keep_default_na=False)
M = {"a": "analysis", "h": "hot_take", "r": "reaction", "q": "question"}
toks = re.findall(r"(\d+)\s*([ahrq])", open("batch.txt").read().lower())
for i, k in toks:
    d.at[int(i), "label"] = M[k]
    d.at[int(i), "note"] = "pre-labelled"
d.to_csv("labels.csv", index=False)
print(len(toks), "labels applied")
print(d[d.label != ""].label.value_counts())