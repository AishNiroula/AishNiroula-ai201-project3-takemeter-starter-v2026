import re, nbformat
from nbclient import NotebookClient

nb = nbformat.read("takemeter.ipynb", as_version=4)

# 1. Fix the notebook itself (needed again in unit 6)
for c in nb.cells:
    if c.cell_type == "code":
        c.source = c.source.replace(
            'LABELS = ["analysis", "hot_take", "reaction"]',
            'LABELS = ["analysis", "hot_take", "reaction", "question"]')
        c.source = c.source.replace('NAME  = "Your Name"', 'NAME  = "Aishwarya"')
        c.source = c.source.replace('EMAIL = "you@example.com"',
                                    'EMAIL = "165102993+AishNiroula@users.noreply.github.com"')
nbformat.write(nb, "takemeter.ipynb")

# 2. Run everything before the "Unit 6 starts here" heading
cut = next(i for i, c in enumerate(nb.cells)
           if c.cell_type == "markdown" and "Unit 6 starts here" in c.source)
print("running", cut, "cells (sections 1-5)")
nb.cells = nb.cells[:cut]
NotebookClient(nb, timeout=-1, kernel_name="takemeter",
               resources={"metadata": {"path": "."}}).execute()

# 3. Show the outputs you need
keys = ("check_dataset(df, LABELS)", "describe_splits(train_df", "results = evaluate", "pick_device()")
for c in nb.cells:
    if c.cell_type == "code" and any(k in c.source for k in keys):
        for o in c.get("outputs", []):
            if o.get("output_type") == "stream":
                print(o["text"])
print("done")