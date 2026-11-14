# Dash introduction

Three Plotly Dash apps that chart the percent of honeybee colonies impacted, by state and year.

## What it does

- `src/intro_dashboard.py` loads the bee table from the original tutorial URL.
- `src/challenge_a.py` and `src/challenge_b.py` load `data/intro_bees.csv` and add the tutorial's end-of-video challenges.
- Each app has a year dropdown for 2015 through 2018 and a bar chart of colony impact.

## Layout

- `src/intro_dashboard.py` — tutorial dashboard
- `src/challenge_a.py` — first challenge
- `src/challenge_b.py` — second challenge
- `data/intro_bees.csv` — colony impact by state and year

## Run

From the repository root:

```bash
pip install -r requirements.txt
python src/intro_dashboard.py
```

The challenge apps run the same way: `python src/challenge_a.py` and `python src/challenge_b.py`.

## Stack

Python, pandas, Plotly, Dash.
