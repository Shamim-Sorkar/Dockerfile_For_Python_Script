# all_commits_checker.py
import requests

REPO = "Shamim-Sorkar/Dockerfile_For_Python_Script"
URL = f"https://api.github.com/repos/{REPO}/commits"

def fetch_all_commits(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        commits = response.json()

        print(f"📦 Total Commits Fetched: {len(commits)}\n")
        for idx, commit in enumerate(commits, start=1):
            sha = commit.get('sha', 'N/A')
            message = commit.get('commit', {}).get('message', 'N/A')
            author = commit.get('commit', {}).get('author', {}).get('name', 'N/A')
            date = commit.get('commit', {}).get('author', {}).get('date', 'N/A')

            print(f"🔹 Commit #{idx}")
            print(f"   🔸 Hash: {sha}")
            print(f"   🔸 Message: {message}")
            print(f"   🔸 Author: {author}")
            print(f"   🔸 Date: {date}")
            print("-" * 40)

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching commits: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    fetch_all_commits(URL)
