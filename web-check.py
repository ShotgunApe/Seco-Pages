# source .venv/bin/activate
# deactivate

import requests
import csv
import os
import time
import json
from dotenv import load_dotenv

filename = os.getcwd() + '/output/pages.csv'

headers = { 
}

# Dict to hold results of requests
results = {
}

def check_page(page):
    url = 'https://' + page + '/'
    print("Obtaining Page:", url)
    try:
        res = requests.get(url, headers = headers)
    except requests.exceptions.RequestException as e:
        print('Not a *github.io page')
    else:
        print("Status:", res.status_code)
        results.setdefault(res.status_code, []).append(page)

if __name__ == "__main__":
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        for i, line in enumerate(reader):
            print(line[0])
            check_page(line[0])
            time.sleep(0.5)

            for key in results:
                print(key, "->", len(results[key]))
    file.close()

    json_obj = json.dumps(results, indent = 4) 
    with open(f"output/git-pages-statuscode.json", "w") as outfile:
        outfile.write(json_obj)
    outfile.close()