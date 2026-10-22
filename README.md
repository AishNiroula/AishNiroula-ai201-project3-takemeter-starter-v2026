# TakeMeter

## What This Does

TakeMeter sorts public Hacker News comments into four labels: `analysis`, `hot_take`, `reaction` and `question`. It is trained on 201 comments I labeled, using a fine-tuned DistilBERT model.

---

## Label Taxonomy

### `analysis`

**Definition:** Makes a point backed by a specific, checkable fact such as a number, date, named source, link, or measurement.

**Example 1:** "Yes, PHP release was scheduled for Wednesday, 21 October 2026 at 14:00 UTC: https://news-web.php.net/php.announce/509"

**Example 2:** "Adding a USB 3 Gigabit adapter to my Onn 4k Pro box was a massive improvement... it was 10/100 and more consistent than the built-in Wifi, but much slower top speeds."

### `hot_take`

**Definition:** A confident claim or opinion with no checkable support offered.

**Example 1:** "The internet is over. We are going back to static htmls for public pages..."

**Example 2:** "the chinese legal system somehow in its flaws is able to hold powerful company execs to account. whereas here in the states - once you're a billionaire - jail... is a foreign concept."

### `reaction`

**Definition:** A feeling or social response to a person or event, with no argument.

**Example 1:** "Correct.... very suspect. Swear you can't trust many posts anymore."

**Example 2:** "Sorry to hear that. So disappointed in the AI companies for making no serious efforts towards transparency..."

### `question`

**Definition:** A genuine request for information or an explanation.

**Example 1:** "Any info on whether Mythos missed this?"

**Example 2:** "How would this work without having to totally prevent anonymity on the internet?"

### The hardest boundary

**Which two labels:** `analysis` vs `hot_take`

**The decision rule I used every time:** If the post contains one specific thing a stranger could look up or verify (a number, date, named source, link, measurement) and uses it to support its point, it is `analysis`. If the only support is "I've seen this" or "everyone knows", it is `hot_take`, even if the writer sounds experienced. A question that is really a challenge ("Why wouldn't you test the idea first?") is `hot_take`, not `question`.

---

## The Dataset

**Where the posts came from:** Public Hacker News comments, pulled on 21 October 2026 from the hn.algolia.com API (no login). I kept comments of 80 to 800 characters, removed duplicates, shuffled them, and saved 260. 201 are labeled in `labels.csv`. The 58 unlabeled extras are in `unlabeled_extra.csv`, and one row of two bare links was dropped because it fit no label.

**How I labelled them:** The first 20 posts I labeled alone and cold, with no help and no tools (marked `cold` in the note column). I labeled posts 20 to 41 myself with a one-keypress terminal tool. For the remaining rows, Claude suggested labels in batches of 40 and I read each post against its suggestion and changed the ones I disagreed with before applying them. Those rows are marked `pre-labelled`.

**Counts per label:**

| Label | Count | Share |
|---|---|---|
| hot_take | 101 | 50.2% |
| analysis | 51 | 25.4% |
| reaction | 32 | 15.9% |
| question | 17 | 8.5% |
| **Total** | 201 | 100% |

`question` is thin, so only about 3 posts land in its test split and its F1 will jump between seeds.

**Three hard cases**

**1.**

> *The post:* "There is no law or regulation which requires institutional investors to hold Meta stock. Sometimes people who don't actually understand the law make spurious claims..."
>
> *Could have been:* `analysis` or `hot_take`
>
> *I chose:* `hot_take`, because it makes a confident legal claim but names no statute, case, or source a stranger could check.

**2.**

> *The post:* "Gotta be able to stop fraudulent payments while maintaining privacy before ecommerce would have any interest in adopting a more private system. I've worked at plenty of companies that have no interest in tracking their customers..."
>
> *Could have been:* `analysis` or `hot_take`
>
> *I chose:* `hot_take`, because its only support is "I've worked at plenty of companies", which is experience, not something a stranger can look up.

**3.**

> *The post:* "It took 8 hours for CloudWays (DigitalOcean) to apply the patch. Big companies suck at responding to major stuff like this."
>
> *Could have been:* `analysis` or `reaction`
>
> *I chose:* `analysis`, because the 8-hour figure and the named vendor are checkable and the second sentence draws a conclusion from them.

---

## The Training Run

**Base model:** `distilbert-base-uncased`

**Settings:** 3 epochs, learning rate 2e-5, batch size 16, 128 tokens per post, seed 42. Trained on an Apple Silicon GPU (`mps`) with torch 2.14.1.

**Anything I changed from the defaults, and why:** I changed no training settings. I added `question` to the notebook's `LABELS` list, which had only three labels, because my data has four.

**Split sizes:** train 139, validation 31, test 31 (stratified 70/15/15). Test posts per label: analysis