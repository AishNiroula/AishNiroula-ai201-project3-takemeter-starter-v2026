# Acceptance criteria - TakeMeter

Written in unit 5 before any training.


---

## 1.

Overall accuracy on the held-out set is at least .50.

**Why this target:** Always guessing hot_take would score about 0.50 on my data, so my target has to be clearly above that to show the model learned something.


---

## 2.

Every label has an F1 of at least .50.

**Why this target:** My two smallest labels, reaction (about 16%) and question (about 8%), have the least training data. One floor for every label stops hot_take from hiding weak labels in the overall accuracy.


---

## 3.

No single label is more than this share of labels.csv 60%%.

**Why this target:** hot_take is already about half my file. Above 70% a model can score well by guessing it, so I'm keeping a ten-point margin below the hard cap.


---

## 4.

The F1 for `question` (my smallest label, about 17 rows) is at least .35.

**Why this target:** question has only about 17 examples, so about 2 or 3 land in the test split. A single post changes its F1 a lot between seeds, so I'm setting it looser than the all-label floor of 0.50.


---

## 5.

My agreement with the staff labels on the 30 shared posts is at least 70%%.

**Why this target:** Staff chose ambiguous posts on purpose, and some of my own labels were pre-labelled and then reviewed. I don't expect high agreement, but below 70% would suggest I applied the decision rule inconsistently.
