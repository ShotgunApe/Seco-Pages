# source .venv/bin/activate
# deactivate

import aiohttp
import asyncio
import json

async def main():
    headers = {
        'X-GitHub-Api-Version': '2022-11-28'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.github.com/search/repositories?q=.github.io+in:name+created:2024-10-01..2024-10-16+pushed:>=2024-10-01&per_page=100&page=1', headers = headers) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            file = json.loads(await response.text())
            
            print("Total Count:", file['total_count'])

            with open("output/git-pages.json", "w") as outfile:
                outfile.write(json.dumps(file, indent = 4))


asyncio.run(main())