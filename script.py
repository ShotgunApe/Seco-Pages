# source .venv/bin/activate
# deactivate

import requests
import json
import os
from dotenv import load_dotenv

url = 'https://api.github.com/search/repositories?q=.github.io+in:name+created:2024-10-15..2024-10-16+pushed:>=2024-10-16&per_page=100&page=1'
headers = {
    'X-GitHub-Api-Version': '2022-11-28',
    'Authorization': str(os.getenv('auth'))
}

def main():
    print("Obtaining Page:", url)
    res = requests.get(url, headers = headers)
    print("Status:", res.status_code)

    output = res.json()
    page = 1

    while 'next' in res.links.keys():
        print("Obtaining Page:", res.links['next']['url'])
        res = requests.get(res.links['next']['url'], headers = headers)
        print("Status:", res.status_code)

        output = res.json()
    
        with open(f"output/git-pages-{page}.json", "w") as outfile:
            outfile.write(json.dumps(output, indent = 4))
        outfile.close()
        page = page + 1

if __name__ == "__main__":
    main()