# commit_checker.py
import requests

REPO = "Shamim-Sorkar/Dockerfile_For_Python_Script"
URL = f"https://api.github.com/repos/{REPO}/commits"

def fetch_latest_commit(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        latest_commit = response.json()[0]
        print(f"🔹 Commit Hash: {latest_commit['sha']}")
        print(f"🔹 Message: {latest_commit['commit']['message']}")
        print(f"🔹 Author: {latest_commit['commit']['author']['name']}")
        print(f"🔹 Date: {latest_commit['commit']['author']['date']}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching commits: {e}")
    except (KeyError, IndexError):
        print("❌ Failed to parse commit data.")

if __name__ == "__main__":
    fetch_latest_commit(URL)
