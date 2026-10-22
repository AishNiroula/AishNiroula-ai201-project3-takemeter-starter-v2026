Q = [
 ("Overall accuracy on the held-out set is at least", "number 0-1, e.g. 0.xx"),
 ("Every label has an F1 of at least", "number 0-1"),
 ("No single label is more than this share of labels.csv", "percent, e.g. xx"),
 ("The F1 for `question` (my smallest label, about 17 rows) is at least", "number 0-1; remember it only has about 2-3 test posts"),
 ("My agreement with the staff labels on the 30 shared posts is at least", "percent, e.g. xx"),
]
out = ["# Acceptance criteria - TakeMeter\n", "Written in unit 5 before any training.\n"]
for n, (stem, hint) in enumerate(Q, 1):
    print(f"\n{n}. {stem}  ({hint})")
    val = input("   your number: ").strip()
    why = input("   why that number (one sentence about MY data): ").strip()
    unit = "%" if n in (3, 5) else ""
    out.append(f"\n---\n\n## {n}.\n\n{stem} {val}{unit}.\n\n**Why this target:** {why}\n")
open("criteria.md", "w").write("\n".join(out))
print("\nWrote criteria.md")