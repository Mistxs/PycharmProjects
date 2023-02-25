import requests
from flask import Flask
from flask import request
import datetime
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
    # print(data)
    # print(data["data"]["online"])
    if data["data"]["online"] == True:

        pretty_date = datechanger(data["data"]["create_date"])
        salon_id = data["data"]["company_id"]
        # print(f"Получили хук об онлайн записи, проверим запись через 10 минут. Филиал {salon_id}")
        document = data["data"]["documents"][0]["id"]
        rec_id = data["data"]["id"]
        now = datetime.datetime.now()
        pretty_output_first(salon_id, rec_id, now)
        time.sleep(600)
        recheck(salon_id, pretty_date, document, rec_id, now)

    else:
        print("Не онлайн запись")

def pretty_output_first(salon_id, rec_id, timestamp):

    pretty_output = f'''
    <p style= "color: #384258; font-size: 14px; margin-left:10px">
    {timestamp}</br>Получен хук</br>Ссылка на запись <a href = "https://yclients.com/timetable/{salon_id}#main_date=2023-01-28&open_modal_by_record_id={rec_id}"> 
    https://yclients.com/timetable/{salon_id}#main_date=2023-01-28&open_modal_by_record_id={rec_id}</a></br> Ожидаем запуска речека (10м) Филиал {salon_id}.</p>

    '''
    print(pretty_output)
    f = open('log.txt', 'a')
    f.write(pretty_output)
    f.close()

def pretty_output_second(code, res, doc, kkm, salon_id, rec_id, timestamp):
    colorscheme = "border: 1px solid; padding: 10px; font-size: 14px; width: 80%"
    pretty_output = "none"
    if code == 1:
        pretty_output = f'''
    <p style = "color:#076e1b; {colorscheme}">
    {timestamp}</br>Ссылка на запись <a href = "https://yclients.com/timetable/{salon_id}#main_date=2023-01-28&open_modal_by_record_id={rec_id}"> 
    https://yclients.com/timetable/{salon_id}#main_date=2023-01-28&open_modal_by_record_id={rec_id}</a></br>
    Речек записи выполнен. Необходима разблокировка.</br>
    Ответ от тестера: {res}</p>'''
    elif code == 2:
        pretty_output = f'''
    <p style = "color:#f31717; {colorscheme}">
    {timestamp}</br>Ссылка на запись <a href = "https://yclients.com/timetable/{salon_id}#main_date=2023-01-28&open_modal_by_record_id={rec_id}"> 
    https://yclients.com/timetable/{salon_id}#main_date=2023-01-28&open_modal_by_record_id={rec_id}</a></br>
    Речек записи выполнен. Требуется ручная разблокировка!</br>
    UPDATE documents SET bill_print_status = 1 WHERE id = {doc};</br>
    UPDATE kkm_transactions SET status = 3 WHERE id in {kkm};</p>'''
    elif code == 3:
        pretty_output = f'''
    <p style = "color:#2716a9; {colorscheme}">
    {timestamp}</br>Ссылка на запись <a href = "https://yclients.com/timetable/{salon_id}#main_date=2023-01-28&open_modal_by_record_id={rec_id}"> 
    https://yclients.com/timetable/{salon_id}#main_date=2023-01-28&open_modal_by_record_id={rec_id}</a></br>
    Речек записи выполнен. Анлок не требуется.</br>
    Причина: isblock = {doc} and isprint = {kkm}</p>'''
    print(pretty_output)
    f = open('log.txt', 'a')
    f.write("\n")
    f.write(pretty_output)
    f.write("\n\n")
    f.close()

def recheck(salon_id, pretty_date, document, rec_id, lid):
    # print('Запустился речек записи')
    block = check_record(salon_id, pretty_date, document)
    isprint, kkm = check_kkm(salon_id, pretty_date, document)

    if block == True and isprint == "True":
        result = unblock_rec(rec_id)
        # print(f"Result of unblock: {result}")
        pretty_output_second(1, result, 0, 0,salon_id, rec_id, lid)

    elif block == True and isprint == "False":
        # print(f"Больше одной ккм транзакции! Требуется ручное действие\nisblock = {block} and isprint = {isprint}")
        pretty_output_second(2,0,document,kkm,salon_id, rec_id, lid)

    else:
        # print(f"Анлок не требуется. Причина: isblock = {block} and isprint = {isprint}")
        pretty_output_second(3,0,block,isprint,salon_id, rec_id, lid)

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
    kkm = []
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
            kkm.append(pretty_response["data"][i]["id"])
            kkm_pre_status = pretty_response["data"][i]["status"]["id"]
            # print(trans_type, kkm_pre_status)
    if cnt == 1 and trans_type == 0:
        kkm_status = "True"
    else:
        kkm_status = "False"
    return kkm_status, kkm

def unblock_rec(rec_id):
    url = f"https://yclients.com/tester/unlock_record/{rec_id}"

    payload = {}
    headers = {
        'Cookie': 'auth=u-11946640-e76d93a1473746138eee5; __cf_bm=4dMNr2uHkbT9DFcrK4jWQJc0FjKbC5.y2QSBRH4BYqM-1676655587-0-AQodyx+YbP2/gaVZiDgnqHKrQkthjuL3SZHGNMIlL5l7xD8+uR/hPHDbj+kbLxvvGNIFUsWd94XVHgIxzd+jqhM=; _cfuvid=S2mcafmZTl.ESleaxwuNMZuhlR5SZ4ZgTc6coohIAMo-1676652662027-0-604800000; auth=f5h1qav8jbiepmlvjd17hnplesoeb95mt4g9luq1m645ns8u2ld279k75sntonqm; ycl_language_id=1',
        'Authorization': 'Basic YS5maWxpcHBvdkB5Y2xpZW50cy50ZWNoOk9zZTd2Z3Q1'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


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

    return f'''<h3> Log </h3>{text}
<p style="font-size:12px; color: #49456a"> 
Это актуальные логи. Архив можно посмотреть  <a href="/log_2">здесь</a></p>
'''


@app.route('/log_2')
def log2():
    # print(request)
    f = open('log_2.txt', 'r')
    text = f.read()
    # print(text)
    # print(text)

    # with open('log.txt',"r") as f:
    #     for line in f.readlines():
    #         print(line)

    return f'''<h3> Log </h3>{text}
<p style="font-size:12px; color: #49456a"> 
Это архивная страница с логами. Актуальные можно посмотреть <a href="/log">здесь</a></p>
'''


@app.route('/db')
def db():
    # print(request)
    f = open('salon_db.txt', 'r')
    text = f.read()
    # print(text)
    # print(text)

    # with open('log.txt',"r") as f:
    #     for line in f.readlines():
    #         print(line)

    return f'''<h3> Salons </h3>{text}
<p style="font-size:14px; color: #49456a"> Прямая ссылка на настройку хуков
<a href = "https://yclients.com/settings/web_hook/514463/"> https://yclients.com/settings/web_hook/514463/ </a></p>
'''

if __name__ == '__main__':
    app.run()
