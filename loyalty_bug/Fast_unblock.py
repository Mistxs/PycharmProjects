import requests

def get_document(salon_id, record_id):
    url = f"https://api.yclients.com/api/v1/record/{salon_id}/{record_id}"

    payload={}
    headers = {
      'Accept': 'application/vnd.yclients.v2+json',
      'Content-Type': 'application/json',
      'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
      'Cookie': '__cf_bm=XJh1nHzmXsYGjnQVQ896rpGR98i2yZ8lQpqbCIi2r5g-1675442726-0-Aclx8cPxOzPDH5VCxvO8OCD6yTMAYXkAr/oSSy8RUfAnak8JpLFFsGaDn5RheuH5NfOKHz8r6/tkf+U2Zzl+5J4=; _cfuvid=1wJyCXBCk1G0sB22H8b_BAYEhEgvZrlopXuFMDmygIU-1675324909407-0-604800000; auth=1ssiuqf71r7sethgdi176k8ll6gju5tc8rapffud16sqa5oihdh01s13sjlj7jjb'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_clean = response.json()

    document = response_clean["data"]["documents"][0]["id"]
    c_date = response_clean["data"]["create_date"]
    c_date_pretty = c_date.split("T")
    new_date = c_date_pretty[0]
    # print(document, new_date)
    return document, new_date

def get_kkm_id(salon_id, doc_id, date):

    url = f"https://api.yclients.com/api/v1/kkm_transactions/{salon_id}?start_date={date}&end_date={date}&editable_length=100"
    payload = {}
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
        'Cookie': '__cf_bm=dnigEGEw3ptS6QERE116noZ8Mzcv771hc15Cgu7juHs-1675446257-0-AQlXxGDz/f88YhROdXbTNvNJolcFCF4QAWWmZTbtSYLhwu1buou4i8cCreIMjjLP2YF70XVLwkO3/+aG6qIFp5o=; _cfuvid=1wJyCXBCk1G0sB22H8b_BAYEhEgvZrlopXuFMDmygIU-1675324909407-0-604800000; auth=1ssiuqf71r7sethgdi176k8ll6gju5tc8rapffud16sqa5oihdh01s13sjlj7jjb'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    pretty_response = response.json()
    kkm_id = 0
    for i in range(len(pretty_response["data"])):
        if pretty_response["data"][i]["document_id"] == doc_id:
            kkm_id = pretty_response["data"][i]["id"]
    return kkm_id


document = get_document(764917, 572948924)
kkm_id = get_kkm_id(764917,document[0],document[1])

print(f"UPDATE documents SET bill_print_status = 1 WHERE id = {document[0]};")
print(f"UPDATE kkm_transactions SET status = 3 WHERE id = {kkm_id};")
