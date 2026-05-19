# NCAA Football Scouting Dashboard

A portfolio-grade Power BI report built on real 2024 college football data, demonstrating end-to-end data engineering and business intelligence skills — from API ingestion to a published, interactive dashboard.

---

## Tech Stack

- **Python** — data pipeline (requests, pandas)
- **Power BI Desktop / Service** — data modeling, DAX, and report publishing
- **College Football Data API (CFBD)** — data source

---

## Project Structure

```
ncaa-football-powerbi/
├── pipeline/
│   ├── fetch_data.py       # pulls data from CFBD API and exports CSVs
│   └── requirements.txt    # Python dependencies
├── data/
│   ├── dim_team.csv
│   ├── dim_game.csv
│   ├── fact_player_stats.csv
│   ├── fact_team_stats.csv
│   └── fact_drives.csv
├── docs/
│   └── screenshots/        # dashboard screenshots for portfolio
└── README.md
```

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/ncaa-football-powerbi.git
cd ncaa-football-powerbi
```

### 2. Install dependencies

```bash
pip install -r pipeline/requirements.txt
```

### 3. Configure your API key

Register for a free API key at [collegefootballdata.com](https://collegefootballdata.com), then create a `.env` file in the project root:

```
CFBD_API_KEY=your_key_here
```

> Do not commit `.env` to GitHub. It is listed in `.gitignore`.

---

## Running the Pipeline

```bash
python pipeline/fetch_data.py
```

This pulls 2024 season data from 5 CFBD endpoints and exports clean CSVs to the `data/` folder. All CSVs are fully regenerable from this script with no manual edits required.

---

## Data Model

The Power BI report uses a star schema with two fact tables and three dimension tables:

| Table | Type | Description |
|---|---|---|
| `fact_player_stats` | Fact | One row per player per game — rushing, passing, receiving, defense |
| `fact_team_stats` | Fact | One row per team per game — EPA, success rate, yards per play |
| `fact_drives` | Fact | One row per drive — result, plays, yards, time of possession |
| `dim_player` | Dimension | Player lookup — name, position, team |
| `dim_team` | Dimension | Team lookup — school, conference, division |
| `dim_game` | Dimension | Game lookup — week, teams, scores, date |

---

## Dashboard Pages

- **Page 1 — Team Overview:** Conference-level snapshot with EPA rankings, standings table, and offensive vs. defensive profile scatter plot
- **Page 2 — Player Scouting Card:** Dynamic player profile with position-filtered slicers, weekly trend lines, and peer comparison scatter plot
- **Page 3 — Game Log & Drill-Through:** Full season game log with drill-through into drive-by-drive breakdowns for any individual game
- **Page 4 — Team Comparison:** Side-by-side radar chart and stat table for any two user-selected teams

---

## DAX Measures

12 custom DAX measures are implemented in a dedicated `Measures` table, including:

- `Avg EPA Per Play` — efficiency metric across all teams
- `Team EPA Rank` — RANKX-based conference and national rankings
- `Rolling 4-Wk Avg` — recent form trend for player stats
- `Peer Percentile` — player ranking within position group
- `Team A / Team B Metric + Delta` — dynamic two-team comparison

---

## Portfolio

**Published Report:** [Power BI Service Link](#) *(coming soon)*

**Resume Bullet:**
> Built a 4-page NCAA Football scouting dashboard in Power BI, featuring dynamic player comparison cards, drill-through game logs, and 12 custom DAX measures including rolling averages, RANKX-based team rankings, and EPA-driven team comparison — published to Power BI Service from a Python-ingested CFBD API pipeline.

---

## Author

**Anay Patel** — [LinkedIn](#) | [GitHub](#)
