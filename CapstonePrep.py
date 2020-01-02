import requests
import time
from typing import Dict, List


def get_github_jobs_data() -> List[Dict]:
    all_data = []
    page = 1
    more_data = True
    while more_data:
        url = f"https://jobs.github.com/positions.json?page={page}"
        raw_data = requests.get(url)
        partial_jobs_list = raw_data.json()
        all_data.extend(partial_jobs_list)
        if len(partial_jobs_list) < 50:
            more_data = False
        time.sleep(.1)  # short sleep between requests so I dont wear out my welcome.
        page += 1
    return all_data


def main():
    data = get_github_jobs_data()
    for item in data:
        print(item)


if __name__ == '__main__':
    main()