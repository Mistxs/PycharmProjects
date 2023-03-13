import requests
import datetime

now = datetime.date.today()

salon_id = 216720
date = "2023-02-01"
enddate = now

def get_kkm_id(salon_id,date, enddate):
    kkm = []
    docs = []
    url = f"https://api.yclients.com/api/v1/kkm_transactions/{salon_id}?start_date={date}&end_date={enddate}&editable_length=1000"
    payload = {}
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
        'Cookie': '__cf_bm=dnigEGEw3ptS6QERE116noZ8Mzcv771hc15Cgu7juHs-1675446257-0-AQlXxGDz/f88YhROdXbTNvNJolcFCF4QAWWmZTbtSYLhwu1buou4i8cCreIMjjLP2YF70XVLwkO3/+aG6qIFp5o=; _cfuvid=1wJyCXBCk1G0sB22H8b_BAYEhEgvZrlopXuFMDmygIU-1675324909407-0-604800000; auth=1ssiuqf71r7sethgdi176k8ll6gju5tc8rapffud16sqa5oihdh01s13sjlj7jjb'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    pretty_response = response.json()
    print(pretty_response)
    for i in range(len(pretty_response["data"])):
        if pretty_response["data"][i]["type"]["id"] == 0 and pretty_response["data"][i]["status"]["id"] == 1:
            kkm.append(pretty_response["data"][i]["id"])
            docs.append(pretty_response["data"][i]["document_id"])

    print(f"KKM: {len(kkm)},  {kkm}")
    print(f"DOC: {len(docs)}, {docs}")

    temp = []

    for x in docs:
        if x not in temp:
            temp.append(x)
    docs = temp

    print(f"NEWDOC: {len(docs)}, {docs}")


get_kkm_id(salon_id, date, enddate)
