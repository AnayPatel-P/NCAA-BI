import os
import requests
import pandas as pd
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.environ.get("CFBD_API_KEY")
BASE_URL = "https://api.collegefootballdata.com"
headers = {"Authorization": f"Bearer {API_KEY}"}


def fetch(endpoint, params=None):
    url = BASE_URL + endpoint
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()



def main():
    df = pd.DataFrame(fetch("/teams"))
    df.to_csv("data/dim_team.csv", index=False)
    print("teams saved")

    df = pd.DataFrame(fetch("/games", params={"year": 2024}))
    df.to_csv("data/dim_game.csv", index=False)
    print("games saved")

    df = pd.DataFrame(fetch("/stats/player/season", params={"year": 2024}))
    df.to_csv("data/fact_player_stats.csv", index=False)
    print("players saved")

    df = pd.DataFrame(fetch("/stats/season", params={"year": 2024}))
    df.to_csv("data/fact_team_stats.csv", index=False)
    print("team stats saved")

    df = pd.DataFrame(fetch("/drives", params={"year": 2024}))
    df.to_csv("data/fact_drives.csv", index=False)
    print("drives saved")

if __name__ == "__main__":
    main()