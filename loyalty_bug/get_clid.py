import pprint

import requests
import json
from datetime import datetime

with open('input.csv', 'r') as file:
    salon_id = file.readline().strip()
    delta_ch = int(file.readline().strip())

with open('clients.csv', 'r') as file:
    cli_array = [row.strip() for row in file]

url = f"https://api.yclients.com/api/v1/company/{salon_id}/clients/search"


def api_run(client_phone):
    payload = json.dumps({
        "filters": [
            {
                "type": "quick_search",
                "state": {
                    "value": f"{client_phone}"
                }
            }
        ]
    })
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
        'Cookie': '__cf_bm=OUTsKJ_ZXy4_JeEDvDDIO1PL6wKI5BsTojYx9O7.7IE-1667291069-0-ARftKvlitsQtBvgdJIRYCxWp7OrRMgSu/XPtZWkT11N9KxKOI1wOyr3yK71yokCePnewdoE4OYQS0RzuC4FT1KA=; _cfuvid=fmWZ03G_V9rPBss5Eo3MRKoMLmGPD3HRsZyxSObmIao-1667289715646-0-604800000'
    }

    response = requests.request("POST", f"{url}", headers=headers, data=payload)
    request_data = response.json()
    if int(len((request_data["data"])) > 0):
        return request_data["data"][0]["id"]


def get_cli_id(cli_array):
    cli_id = []
    for i in range(0, len(cli_array)):
        ch_id = api_run(cli_array[i])
        if ch_id is not None:
            cli_id.append(ch_id)
    return cli_id

print(get_cli_id(cli_array))
