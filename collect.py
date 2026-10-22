import json, re, html, csv, urllib.request, random
seen, rows = set(), []
for page in range(0, 12):
    url = f"https://hn.algolia.com/api/v1/search_by_date?tags=comment&hitsPerPage=100&page={page}"
    data = json.load(urllib.request.urlopen(url))
    for h in data["hits"]:
        t = html.unescape(re.sub(r"<[^>]+>", " ", h.get("comment_text") or ""))
        t = re.sub(r"\s+", " ", t).strip()
        if 80 <= len(t) <= 800 and t not in seen:
            seen.add(t)
            rows.append(t)
random.seed(1)
random.shuffle(rows)
with open("labels.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["text", "label", "note"])
    for t in rows[:260]:
        w.writerow([t, "", ""])
print(len(rows[:260]), "posts saved")