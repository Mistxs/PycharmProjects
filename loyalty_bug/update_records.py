import requests
import json
import pprint


salon_id = input("Введите salon id ", )
stdate = input("Введите Начальную дату визитов (формат YYYY-MM-DD) ", )
enddate = input("Введите Конечную дату визитов (формат YYYY-MM-DD) ", )
c_stdate = input("Введите Начальную дату создания визитов (формат YYYY-MM-DD) ", )
c_enddate = input("Введите Конечную дату создания визитов (формат YYYY-MM-DD) ", )
page = input("Введите страницу (в api запросе на получение записей максимум 1000 результатов на страницу, если записей меньше, просто оставьте 1 ", )



url = f"https://api.yclients.com/api/v1/records/{salon_id}?start_date={stdate}&end_date={enddate}&c_start_date={c_stdate}&c_end_date={c_enddate}&page={page}&count=1000"

payload = ""
headers = {
    'Accept': 'application/vnd.yclients.v2+json',
    'Content-Type': 'application/json',
    'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
    'Cookie': '__cf_bm=SRoFlSyUb8pCm_Hy6teKbZSVP0RvifVqk_U5L1yhbPY-1672310753-0-ASpA43kPIrIv6YwW/UwhZptVR9zXq7fJ76HU4yXJ35SavwZOW89gSTDFeSiN6VRjSMGSwWNbqGemyCrN6T19heQ=; _cfuvid=p7nUXL8oIvXY2lDDmXMQABeybXrWwPcphBL1X4PPq6I-1672310753861-0-604800000; auth=1ssiuqf71r7sethgdi176k8ll6gju5tc8rapffud16sqa5oihdh01s13sjlj7jjb'
}

response = requests.request("GET", url, headers=headers, data=payload)
request_data = response.json()
rec_id = []
for i in range(0, len(request_data["data"])):
    rec_id.append(request_data["data"][i]["id"])
print(rec_id)
#

def put_record(rec_id, data):
    url3 = f"https://api.yclients.com/api/v1/record/{salon_id}/{rec_id}"
    payload = json.dumps(data)
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
        'Cookie': '__cf_bm=7U9A9XA22HiCfsgeV5.7CEWM2ZO05_FpxXCoLZf6zZU-1672309174-0-AW4GWNaYZ9lJc86eOJ2WNGqYj2RrATN2R9QjSGHLxt72J9O48Ho0GR6LhnGUfboA1IOlPXJ4YCY0sQlv4/GLoFc=; _cfuvid=1N8l_emLiaoDXvgjX8IezQBDkgTiU8HSS5sHnIN9LpQ-1672309174478-0-604800000; auth=1ssiuqf71r7sethgdi176k8ll6gju5tc8rapffud16sqa5oihdh01s13sjlj7jjb'
    }

    response3 = requests.request("PUT", url3, headers=headers, data=payload)
    pprint.pprint(response3.text)


def read_record(rec_id):
    url2 = f"https://api.yclients.com/api/v1/record/{salon_id}/{rec_id}"

    payload = {}
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
        'Cookie': '__cf_bm=7U9A9XA22HiCfsgeV5.7CEWM2ZO05_FpxXCoLZf6zZU-1672309174-0-AW4GWNaYZ9lJc86eOJ2WNGqYj2RrATN2R9QjSGHLxt72J9O48Ho0GR6LhnGUfboA1IOlPXJ4YCY0sQlv4/GLoFc=; _cfuvid=1N8l_emLiaoDXvgjX8IezQBDkgTiU8HSS5sHnIN9LpQ-1672309174478-0-604800000; auth=1ssiuqf71r7sethgdi176k8ll6gju5tc8rapffud16sqa5oihdh01s13sjlj7jjb'
    }

    response2 = requests.request("GET", url2, headers=headers, data=payload)
    request_data2 = response2.json()
    ret = request_data2["data"]
    print("Проверяем детали записи")
    pprint.pprint(ret)
    # сохраняем значение по умолчанию
    true_attendance = request_data2["data"]["attendance"]

    # меняем статус визита на клиент пришел
    ret["attendance"] = 1
    # запускаем функцию с пут запросом
    put_record(rec_id, ret)

    # проверяем че натворили
    print("Проверяем что изменилось в записи")
    response2 = requests.request("GET", url2, headers=headers, data=payload)
    request_data2 = response2.json()
    pprint.pprint(request_data2)

    # меняем статус визита на ожидание
    ret["attendance"] = 0
    # запускаем функцию с пут запросом
    put_record(rec_id, ret)

    # меняем статус визита на изначальный
    ret["attendance"] = true_attendance
    # запускаем функцию с пут запросом
    put_record(rec_id, ret)

    print("Проверяем изменения обратно")
    response2 = requests.request("GET", url2, headers=headers, data=payload)
    request_data2 = response2.json()
    pprint.pprint(request_data2)



for j in range(0, len(rec_id)):
   read_record(rec_id[j])
