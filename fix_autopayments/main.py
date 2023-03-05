from flask import Flask
from flask import request
import requests
import json
import datetime

app = Flask(__name__)

salon_id = 780413
cnt = -1

def findrecord(salon_id):
    now = datetime.date.today()
    # now = '2023-03-04'
    url = f"https://api.yclients.com/api/v1/records/{salon_id}?start_date={now}&end_date={now}"
    payload = {}
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'u8xzkdpkgfc73uektn64, 4f4db9e8b405fa6364ec9ef432ee3640',
        'Cookie': '__cf_bm=svwy2HlzMjh_wjivEZLRgPN5PGBnJMU81DXZBHjdXQM-1677687164-0-ASBEcTxUD/GSpWUm0MARctGc8TQWeC51zFALDTLo+tNjNk6d42u2da2l3Xqu2MJ0w9EEwIIqk0U6ur3qGrfCjGk=; _cfuvid=aJ8GUKgCMcOSsWNylbPwNUHkPSmllZfcmQW_sLi20SA-1677681577317-0-604800000; auth=f5h1qav8jbiepmlvjd17hnplesoeb95mt4g9luq1m645ns8u2ld279k75sntonqm'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.json()
    return response_json["data"]

def getnotpaid(data):
    ids = []
    phones = []
    services = []
    doc_id = []
    for i in range(len(data)):
        if data[i]["paid_full"] == 0:
            ids.append(data[i]["id"])
            phones.append(data[i]["client"]["phone"])
            services.append(data[i]["services"][0]["id"])
            doc_id.append(data[i]["documents"][0]["id"])
    return ids, phones, services, doc_id


def payment(doc_id,abon_id,abon_num):
    url = f"https://api.yclients.com/api/v1/company/{salon_id}/sale/{doc_id}/payment"
    print(url)
    print(abon_id)
    print(abon_num)
    payload = json.dumps({
        "payment": {
            "method": {
                "slug": "loyalty_abonement",
                "loyalty_abonement_id": abon_id
            },
            "number": f"{abon_num}"
        }
    })
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
        'Cookie': '__cf_bm=WccQSfRo09Q1U24OCQbqsi390WQU92awGiLH_IdG2KU-1677683504-0-AZff+Er3FCCdAFDjeWg/novb0Whm3GcrkM5re4wYA4rhXfZ2TfFFE7lDpJcZi+Jpkh8Hz/Rdu8DXQhBsqq+6a3Y=; _cfuvid=aJ8GUKgCMcOSsWNylbPwNUHkPSmllZfcmQW_sLi20SA-1677681577317-0-604800000; auth=f5h1qav8jbiepmlvjd17hnplesoeb95mt4g9luq1m645ns8u2ld279k75sntonqm'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def findmatch(services,cnt,serv):
    service_ids = []
    cat_ids = []
    for i in range(len(services)):
        if "service" in services[0]:
            service_ids.append(services[i]["service"]["id"])
        if "category" in services[0]:
            cat_ids.append(services[i]["category"]["id"])
    if serv[cnt] in service_ids:
        print("Есть пробитие, надо попробовать списать")
        return cnt
        # payment()
    else:
        print("Нет услуг в абонементе для списания")
    # print(service_ids, cat_ids)
    # print(serv[cnt])

def checkloyalty(phones):
    url = f"https://api.yclients.com/api/v1/loyalty/abonements/?company_id={salon_id}&phone={phones}"
    payload = {}
    ids = []
    numn = -1
    services = []
    abon_num = []
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
        'Cookie': '__cf_bm=.Tc.JoI.6iOxv3Lazu_LqExKCWsfylisKCkLbNTZ.jg-1677690848-0-AR+mSySeru7wWpjIOkfIfIVpfxUvRlarOjF9Ms1g2WODm3dRIH8Nv1UpqZSFwie3zLN6PwJU/1ryRKWysi2nsDw=; _cfuvid=aJ8GUKgCMcOSsWNylbPwNUHkPSmllZfcmQW_sLi20SA-1677681577317-0-604800000; auth=f5h1qav8jbiepmlvjd17hnplesoeb95mt4g9luq1m645ns8u2ld279k75sntonqm'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.json()
    # print(f'{cnt}: {response_json["data"]}')
    if phones == '':
        print('Запись без клиента')
        # loger(1)
    else:
        if len(response_json["data"]) == 0:
            print(f'Абонемента нет у клиента {phones}')
            # loger(2)
        elif len(response_json["data"]) > 0:
            # loger(3)
            for i in range(len(response_json["data"])):
                if response_json["data"][i]["status"]["id"] == 2:
                    # print(f'ВАЖНАЯ ХЕРЬ - НАЙДИ НОМЕР АБИКА: {response_json["data"][i]}')
                    ids.append(response_json["data"][i]["id"])
                    abon_num.append(response_json["data"][i]["number"])
                    services.append(response_json["data"][i]["balance_container"]["links"])

            # print(f"Собрали услуги и id абиков: {services} / {ids}")
            numn = findmatch(services[0],cnt,serv)
    return ids,numn,abon_num



start = findrecord(salon_id)
print(start)

ids, phones,serv, docid = getnotpaid(start)
print(ids)
print(phones)

for i in range(len(phones)):
    cnt += 1
    print("================")
    # print(checkloyalty(phones[i]))
    abiks,counter,abik_num = checkloyalty(phones[i])
    print(f"result: {abiks,counter,abik_num}")
    if counter != -1 and counter:
        print(f'doc_num: {docid[counter]}')
        print(f'phone: {phones[counter]}')
        # payment(docid[counter],abiks[0],abik_num[0])
        # print(start[counter])

@app.route('/log')
def log():
    # print(request)
    f = open('log.txt', 'r')
    text = f.read()
    # print(text)
    # print(text)

    # with open('log.txt',"r") as f:
    #     for line in f.readlines():
    #         print(line)

    return


if __name__ == '__main__':
    app.run()