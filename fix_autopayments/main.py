from flask import Flask, render_template, request
import requests
import json
import datetime
import schedule

app = Flask(__name__)
#
# salon_id = 780413
# cnt = -1
# # now = datetime.date.today()
# now = '2023-03-05'
# data_list = [{}]
#
#
# def findrecord(salon_id):
#     url = f"https://api.yclients.com/api/v1/records/{salon_id}?start_date={now}&end_date={now}"
#     payload = {}
#     headers = {
#         'Accept': 'application/vnd.yclients.v2+json',
#         'Content-Type': 'application/json',
#         'Authorization': 'u8xzkdpkgfc73uektn64, 4f4db9e8b405fa6364ec9ef432ee3640',
#         'Cookie': '__cf_bm=svwy2HlzMjh_wjivEZLRgPN5PGBnJMU81DXZBHjdXQM-1677687164-0-ASBEcTxUD/GSpWUm0MARctGc8TQWeC51zFALDTLo+tNjNk6d42u2da2l3Xqu2MJ0w9EEwIIqk0U6ur3qGrfCjGk=; _cfuvid=aJ8GUKgCMcOSsWNylbPwNUHkPSmllZfcmQW_sLi20SA-1677681577317-0-604800000; auth=f5h1qav8jbiepmlvjd17hnplesoeb95mt4g9luq1m645ns8u2ld279k75sntonqm'
#     }
#
#     response = requests.request("GET", url, headers=headers, data=payload)
#     response_json = response.json()
#     print(response_json)
#     return response_json["data"]
#
#
# def getnotpaid(data):
#     for i in range(len(data)):
#         if data[i]["paid_full"] == 0:
#             data_list[cnt]["id"] = data[i]["id"]
#             data_list[cnt]["phones"] = data[i]["client"]["phone"]
#             data_list[cnt]["services"] = data[i]["services"][0]["id"]
#             data_list[cnt]["doc_id"] = data[i]["documents"][0]["id"]
#
#
# def payment(doc_id, abon_id, abon_num):
#     url = f"https://api.yclients.com/api/v1/company/{salon_id}/sale/{doc_id}/payment"
#     print(url)
#     print(abon_id)
#     print(abon_num)
#     payload = json.dumps({
#         "payment": {
#             "method": {
#                 "slug": "loyalty_abonement",
#                 "loyalty_abonement_id": abon_id
#             },
#             "number": f"{abon_num}"
#         }
#     })
#     headers = {
#         'Accept': 'application/vnd.yclients.v2+json',
#         'Content-Type': 'application/json',
#         'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
#         'Cookie': '__cf_bm=WccQSfRo09Q1U24OCQbqsi390WQU92awGiLH_IdG2KU-1677683504-0-AZff+Er3FCCdAFDjeWg/novb0Whm3GcrkM5re4wYA4rhXfZ2TfFFE7lDpJcZi+Jpkh8Hz/Rdu8DXQhBsqq+6a3Y=; _cfuvid=aJ8GUKgCMcOSsWNylbPwNUHkPSmllZfcmQW_sLi20SA-1677681577317-0-604800000; auth=f5h1qav8jbiepmlvjd17hnplesoeb95mt4g9luq1m645ns8u2ld279k75sntonqm'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#     pr_response = response.json()
#     print(response.text)
#     print(pr_response["meta"]["message"])
#     data_list[cnt]["pay_res"] = pr_response["meta"]["message"]
#
#
# def findmatch(services, cnt, serv):
#     service_ids = []
#     cat_ids = []
#     for i in range(len(services)):
#         if "service" in services[0]:
#             service_ids.append(services[i]["service"]["id"])
#         if "category" in services[0]:
#             cat_ids.append(services[i]["category"]["id"])
#     if serv[cnt] in service_ids:
#         print("Есть пробитие, надо попробовать списать")
#         data_list[cnt]["check_res"] = "Есть абонемент, с которого можно списать занятие"
#         return cnt
#         # payment()
#     else:
#         data_list[cnt]["check_res"] = "Нет услуг в абонементе для списания"
#         print("Нет услуг в абонементе для списания")
#     # print(service_ids, cat_ids)
#     # print(serv[cnt])
#
#
# def checkloyalty(phones):
#     url = f"https://api.yclients.com/api/v1/loyalty/abonements/?company_id={salon_id}&phone={phones}"
#     payload = {}
#     ids = []
#     numn = -1
#     services = []
#     abon_num = []
#     headers = {
#         'Accept': 'application/vnd.yclients.v2+json',
#         'Content-Type': 'application/json',
#         'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
#         'Cookie': '__cf_bm=.Tc.JoI.6iOxv3Lazu_LqExKCWsfylisKCkLbNTZ.jg-1677690848-0-AR+mSySeru7wWpjIOkfIfIVpfxUvRlarOjF9Ms1g2WODm3dRIH8Nv1UpqZSFwie3zLN6PwJU/1ryRKWysi2nsDw=; _cfuvid=aJ8GUKgCMcOSsWNylbPwNUHkPSmllZfcmQW_sLi20SA-1677681577317-0-604800000; auth=f5h1qav8jbiepmlvjd17hnplesoeb95mt4g9luq1m645ns8u2ld279k75sntonqm'
#     }
#     response = requests.request("GET", url, headers=headers, data=payload)
#     response_json = response.json()
#     print(response_json)
#     # print(f'{cnt}: {response_json["data"]}')
#     if phones == '':
#         print('Запись без клиента')
#         data_list[cnt]["name"] = "Запись без клиента"
#         data_list[cnt]["check_res"] = "Проверка невозможна, нет клиента"
#         # loger(1)
#     else:
#         data_list[cnt]["name"] = start[cnt]["client"]["name"]
#         if len(response_json["data"]) == 0:
#             print(f'Абонемента нет у клиента {phones} ')
#             data_list[cnt]["check_res"] = "У клиента нет абонемента"
#             # loger(2)
#         elif len(response_json["data"]) > 0:
#             # loger(3)
#             for i in range(len(response_json["data"])):
#                 if response_json["data"][i]["status"]["id"] == 2:
#                     print(f'ВАЖНАЯ ХЕРЬ - НАЙДИ НОМЕР АБИКА у клиента {phones}: {response_json["data"][i]}')
#                     ids.append(response_json["data"][i]["id"])
#                     abon_num.append(response_json["data"][i]["number"])
#                     services.append(response_json["data"][i]["balance_container"]["links"])
#             # print(f"Собрали услуги и id абиков: {services} / {ids}")
#             numn = findmatch(services[0], cnt, serv)
#     return ids, numn, abon_num
#
#
# # print(phones)
#
#
# db = []
#
# start = findrecord(salon_id)
# ids, phones, serv, docid = getnotpaid(start)
#
#
#
#
#
# for i in range(len(phones)):
#     cnt += 1
#     print("================")
#     # print(checkloyalty(phones[i]))
#     data_list[cnt]["id"] = cnt
#     data_list[cnt]["name"] = start[cnt]["client"]["name"]
#     data_list[cnt]["phone"] = start[cnt]["client"]["phone"]
#     data_list[cnt]["master"] = start[cnt]["staff"]["position"]["title"]
#     data_list[cnt]["time"] = start[cnt]["date"]
#     data_list[cnt]["pay_res"] = "Запрос на списание не выполнялся"
#     data_list[cnt][
#         "link"] = f"https://yclients.com/timetable/{salon_id}#main_date={now}&open_modal_by_record_id={start[cnt]['id']}"
#     data_list[cnt]["doc_id"] = docid[cnt]
#
#     abiks, counter, abik_num = checkloyalty(phones[i])
#
#     data_list[cnt]["ab_id"] = abik_num[cnt]
#
#     print(f"result: {abiks, counter, abik_num}")
#     if counter != -1 and counter:
#         print(f'doc_num: {docid[counter]}')
#         print(f'phone: {phones[counter]}')
#         data_list[cnt]["pay_res"] = "Результат выполнения"
#
#         # payment(docid[counter],abiks[0],abik_num[0])
#         # print(start[counter])
#     print(data_list[cnt])
#     data_list.append({})
# data_list.pop(-1)
#
#
# @app.route('/autopayments')
# def ap():
#     return render_template('logs.html', data_list=data_list, now=now)
#

# совсем другая страница и прога

database = []
database_resp = []


@app.route('/findkkm', methods=['GET', 'POST'])
def findkkm():
    if request.method == 'POST':
        inputdata = request.form.get('URL')
        database.append(inputdata)
        if 'https://yclients.com/timetable/' not in inputdata:
            sale = "Введите корректную ссылку в виде https://yclients.com/timetable/331981#main_date=2023-03-06&open_modal_by_record_id=580873343"
        else:
            salon_and_rec = clearurl(inputdata)
            document = get_document(salon_and_rec[0], salon_and_rec[1])
            sale, full = get_sale(salon_and_rec[0], document)
            database_resp.append(sale)
        return render_template('kkm.html', data=sale, full=full)
    return render_template('kkm.html')


def clearurl(data):
    # print("URL IS: ", data)
    newstr = data.split("/")
    newstr[-1] = newstr[-1].split("#")
    salon_id = int(newstr[-1][0])
    rec_id_dirt = newstr[-1][-1].split("=")
    rec_id = int(rec_id_dirt[-1])
    return salon_id, rec_id


def get_document(salon_id, record_id):
    url = f"https://api.yclients.com/api/v1/record/{salon_id}/{record_id}"
    payload = {}
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
        'Cookie': '__cf_bm=XJh1nHzmXsYGjnQVQ896rpGR98i2yZ8lQpqbCIi2r5g-1675442726-0-Aclx8cPxOzPDH5VCxvO8OCD6yTMAYXkAr/oSSy8RUfAnak8JpLFFsGaDn5RheuH5NfOKHz8r6/tkf+U2Zzl+5J4=; _cfuvid=1wJyCXBCk1G0sB22H8b_BAYEhEgvZrlopXuFMDmygIU-1675324909407-0-604800000; auth=1ssiuqf71r7sethgdi176k8ll6gju5tc8rapffud16sqa5oihdh01s13sjlj7jjb'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_clean = response.json()

    document = response_clean["data"]["documents"][0]["id"]
    return document


def get_sale(salon_id, doc_id):
    url = f"https://api.yclients.com/api/v1/company/{salon_id}/sale/{doc_id}"
    payload = {}
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
        'Cookie': '__cf_bm=XJh1nHzmXsYGjnQVQ896rpGR98i2yZ8lQpqbCIi2r5g-1675442726-0-Aclx8cPxOzPDH5VCxvO8OCD6yTMAYXkAr/oSSy8RUfAnak8JpLFFsGaDn5RheuH5NfOKHz8r6/tkf+U2Zzl+5J4=; _cfuvid=1wJyCXBCk1G0sB22H8b_BAYEhEgvZrlopXuFMDmygIU-1675324909407-0-604800000; auth=1ssiuqf71r7sethgdi176k8ll6gju5tc8rapffud16sqa5oihdh01s13sjlj7jjb'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_clean = response.json()

    dataset = response_clean["data"]["kkm_state"]["transactions"]
    full_resp = response_clean["data"]
    return dataset, full_resp


@app.route('/findkkmlog')
def kkmlog():
    return f'''все запросы: {database}


ответы по продаже: {database_resp}
'''


if __name__ == '__main__':
    app.run()
