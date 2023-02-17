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
    v_date = response_clean["data"]["datetime"]
    c_date_pretty = c_date.split("T")
    v_date_pretty = v_date.split("T")
    new_date = c_date_pretty[0]
    end_date = v_date_pretty[0]
    # print(document, new_date)
    return document, new_date, end_date

def get_kkm_id(salon_id, doc_id, date, enddate):
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
    kkm_id = 1
    cnt = 0
    listofid = []
    for i in range(len(pretty_response["data"])):
        if pretty_response["data"][i]["document_id"] == doc_id:
            # print("Step ", i)
            # print(cnt, kkm_id, listofid)
            cnt += 1
            if cnt > 1:
                listofid.append(pretty_response["data"][i]["id"])
            else:
                kkm_id = pretty_response["data"][i]["id"]
    listofid.append(kkm_id)
    max_kkm = max(listofid)
    return max_kkm


document = get_document(764917, 572948924)
kkm_id = get_kkm_id(764917,document[0],document[1],document[2])

def check_record(salon_id,date,doc_id):
    url = f"https://api.yclients.com/api/v1/records/{salon_id}?c_start_date={date}&c_end_date={date}"

    payload = ""
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
        'Cookie': '__cf_bm=j28qd_0gWsq8tDnlbho_8Ws2ejwXXpV12lVmxqVnho0-1676648874-0-AbtSyJJNcNVe5MBzCepK9FK0SeYj6zUOZOXImY5knt3wDYnY4EicUCasyw7YbAzjqM8kdCMy5LWW930E3KRsGu8=; _cfuvid=9cQUbYnLwvNyv035C3qkAXZChlAylSu.eOSEjgzzO6Y-1676644402973-0-604800000; auth=1ssiuqf71r7sethgdi176k8ll6gju5tc8rapffud16sqa5oihdh01s13sjlj7jjb'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    pretty_respone = response.json()
    isprint = "none"
    for i in range(len(pretty_respone["data"])):
        # print(pretty_respone["data"][i]["documents"][0])
        if pretty_respone["data"][i]["documents"][0]["id"] == doc_id:
            isprint = pretty_respone["data"][i]["is_sale_bill_printed"]
    return isprint

def check_kkm(salon_id, date, enddate, doc_id):
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
    kkm_status = "none"
    cnt = 0
    trans_type = -1
    for i in range(len(pretty_response["data"])):
        if pretty_response["data"][i]["document_id"] == doc_id:
            cnt += 1
            trans_type = pretty_response["data"][i]["type"]["id"]
            kkm_pre_status = pretty_response["data"][i]["status"]["id"]
            # print(trans_type, kkm_pre_status)
    if cnt == 1 and trans_type == 0:
        kkm_status = "True"
    else:
        kkm_status = "False"
    return kkm_status

print(f"UPDATE documents SET bill_print_status = 1 WHERE id = {document[0]};")
print(f"UPDATE kkm_transactions SET status = 3 WHERE id = {kkm_id};")

print(check_record(543449,"2023-01-23",653941116))
print(check_kkm(543449,"2023-01-23","2023-02-17",653941116))

def unblock():
    import requests

    url = "https://yclients.com/tester/unlock_record/579809323"

    payload = {}
    headers = {
        'Cookie': 'auth=u-11946640-e76d93a1473746138eee5; __cf_bm=4dMNr2uHkbT9DFcrK4jWQJc0FjKbC5.y2QSBRH4BYqM-1676655587-0-AQodyx+YbP2/gaVZiDgnqHKrQkthjuL3SZHGNMIlL5l7xD8+uR/hPHDbj+kbLxvvGNIFUsWd94XVHgIxzd+jqhM=; _cfuvid=S2mcafmZTl.ESleaxwuNMZuhlR5SZ4ZgTc6coohIAMo-1676652662027-0-604800000; auth=f5h1qav8jbiepmlvjd17hnplesoeb95mt4g9luq1m645ns8u2ld279k75sntonqm; ycl_language_id=1',
        'Authorization': 'Basic YS5maWxpcHBvdkB5Y2xpZW50cy50ZWNoOk9zZTd2Z3Q1'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)