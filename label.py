import sys, tty, termios
import pandas as pd

KEYS = {"a": "analysis", "h": "hot_take", "r": "reaction", "q": "question"}
df = pd.read_csv("labels.csv", keep_default_na=False)

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

def save():
    df.to_csv("labels.csv", index=False)

done = (df.label != "").sum()
history = []
i = 0
while i < len(df):
    if df.at[i, "label"] != "":
        i += 1
        continue
    n_done = (df.label != "").sum()
    print("\033[2J\033[H", end="")
    print(f"[{n_done}/{len(df)} labeled]  a=analysis h=hot_take r=reaction q=question  u=undo  x=save+quit\n")
    print(df.at[i, "text"], "\n")
    k = getkey().lower()
    if k == "x" or k == "\x03":
        break
    if k == "u" and history:
        j = history.pop()
        df.at[j, "label"] = ""
        df.at[j, "note"] = ""
        i = j
        save()
        continue
    if k in KEYS:
        df.at[i, "label"] = KEYS[k]
        if n_done < 20:
            df.at[i, "note"] = "cold"
        history.append(i)
        save()
        i += 1

save()
print("\nSaved.")
print(df[df.label != ""].label.value_counts())