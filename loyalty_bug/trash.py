import requests
from flask import Flask
from flask import request
import time

app = Flask(__name__)


@app.route('/getrec', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        request_data = request.json
        if request_data["resource"] == "record" and request_data["status"] == "create":
            check_hook(request_data)


        return '200'
    else:
        return 'Content-Type not supported!'


def check_hook(data):
    print(data)
    print(data["data"]["online"])
    if data["data"]["online"] == True:
        print("Получили хук об онлайн записи, проверим запись через 10 минут")
        pretty_date = datechanger(data["data"]["create_date"])
        salon_id = data["data"]["company_id"]
        document = data["data"]["documents"][0]["id"]
        rec_id = data["data"]["id"]
        time.sleep(600)
        recheck(salon_id,pretty_date,document,rec_id)


    else:
        print("Не онлайн запись")


def recheck(salon_id, pretty_date, document,rec_id):
    print('Запустился речек записи')
    block = check_record(salon_id, pretty_date, document)
    isprint = check_kkm(salon_id, pretty_date, document)

    if block == True and isprint == "True":
        result = unblock_rec(rec_id)
        print(f"Result of unblock: {result}")
    else:
        print(f"Анблока не было, причина: isblock = {block}, isprint = {isprint}")


def datechanger(string):
    truedate = string.split("T")
    return truedate[0]


def check_record(salon_id, date, doc_id):
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


def check_kkm(salon_id, date, doc_id):
    url = f"https://api.yclients.com/api/v1/kkm_transactions/{salon_id}?start_date={date}&end_date={date}&editable_length=1000"
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


def unblock_rec(rec_id):
    url = f"https://yclients.com/tester/unlock_record/{rec_id}"

    payload = {}
    headers = {
        'Cookie': 'auth=u-11946640-e76d93a1473746138eee5; __cf_bm=4dMNr2uHkbT9DFcrK4jWQJc0FjKbC5.y2QSBRH4BYqM-1676655587-0-AQodyx+YbP2/gaVZiDgnqHKrQkthjuL3SZHGNMIlL5l7xD8+uR/hPHDbj+kbLxvvGNIFUsWd94XVHgIxzd+jqhM=; _cfuvid=S2mcafmZTl.ESleaxwuNMZuhlR5SZ4ZgTc6coohIAMo-1676652662027-0-604800000; auth=f5h1qav8jbiepmlvjd17hnplesoeb95mt4g9luq1m645ns8u2ld279k75sntonqm; ycl_language_id=1',
        'Authorization': 'Basic YS5maWxpcHBvdkB5Y2xpZW50cy50ZWNoOk9zZTd2Z3Q1'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


if __name__ == '__main__':
    app.run()
