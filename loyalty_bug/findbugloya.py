import pprint

import requests
import json



salon_id = 503759
startdate = '2023-03-05'
enddate = '2023-03-06'
pretty_output = [{}]

nc = [79097697017, 79280062079, 79620000056, 79283038030, 79034465782, 79283615172, 79064605353, 79624475770, 79188810424, 79197342894, 79187479807, 79187506665, 79187506665, 79283100359, 79282515336, 79283108287, 79185817505, 79888564898, 79624417977, 79614986529, 79899749356, 79288114742, 79288114742, 79054693447, 79624454708, 79614969727, 79887363015, 79197332602, 79280131819, 79881028521, 79286360821, 79993798011, 79620161265, 79620043104, 79881171476, 79054461844, 79881150689, 79624039595, 79187872987, 79624409805, 79187856110, 79887678888, 79624499299, 79624010191, 79624131121, 79911120787, 79620194035, 79624017484, 79614975393, 79624288866, 79214003307, 79624005937, 79880941962, 79614470000, 79283424419, 79197460084, 79624011251, 79624445277, 79283146010, 79288242462, 79383162615, 79288202819, 79283031370, 79608999599, 79642265334, 79682684547, 79899802021, 79064689048, 79614429777, 79289680865, 79064707170, 79187879767, 79283986907, 79283214900, 79624503792, 79282303156, 79899936293, 79624343654, 79888606858, 79624029458, 79282627634, 79881150582, 79197302539, 79624486086, 79624553796, 79887511016, 79633822545, 79283502939, 79333304044, 79282643194, 79383030611, 79187803044, 79187994858, 79603460400, 79283566499, 79620006070, 79383064222, 79034189660, 79614470000, 79283100090, 79054601622, 79620002228, 79283240850, 79614705170, 79034165309, 79614705725, 79112695069, 79383005880, 79282509427, 79887319464, 79624942478, 79153465811, 79682678350, 79614838328, 79187535605, 79118080005, 79282628900, 79624462560, 79187929669, 79614555972, 79149296945, 79054905595, 79187904411, 79624415005, 79624478375, 79244896319, 79188675250, 79188665573, 79187663050, 79682684547, 79964172791, 79283124676, 79283352852, 79275050846, 79624919749, 79283086877, 79620218123, 79624505093, 79624017484, 79211599999, 79614423501, 79187777713, 79633846663, 79054996570, 79097736120, 79097736120, 79873581525, 79064979777, 79288119997, 79064703627, 79188657011, 79283008005, 79620035494, 79624493057, 79188838327, 79620097777, 79188888333, 79950000175, 79181825542, 79614643892, 79282228085, 79620238181, 79188810424, 79624422682, 79185830416, 79054923227, 79614961111, 79614961111, 79620093330, 79293600009, 79624464986, 79286345544, 79286345544, 79188002700, 79187771984, 79187600420, 79676563341, 79614697742, 79624544000, 79129863639, 79624215048, 79282254014, 79097692777, 79624042442, 79624011169, 79383311464, 79187400296, 79614997598, 79624005227, 79614403883, 79182665836, 79624977007, 79994971330, 79624977007, 79187421835, 79624422314, 79804769247, 79160314415, 79624975854, 79280056722, 79682684547, 79280098969, 79994971330, 79620259888, 79054418087, 79999999159, 79097551777, 79187755623, 79280101829, 79187483838, 79999723212, 79188046675, 79964201667, 79288100109, 79624242999, 79197463850, 79881192222, 79064789457, 79887017337, 79624006629, 79113770000, 79187902152, 79184172035, 79614602976, 79624559939, 79624408562, 79181158981, 79624500505, 79283986907, 79283661991, 79283661991, 79850850468, 79871134752, 79620238103, 79624953936, 79887518103, 79624307070, 79283018870, 79614803167, 79632840133, 79197381281, 79647253024, 79887028466, 79869540384, 79682651339, 79272890838, 79633852251, 79064779227, 79283069909, 79620137777, 79280055950, 79187477075, 79620064579, 79034548050, 79187953350, 79280110044, 79187931894, 79624440688, 79624035245, 79887097562, 79624018848, 79682684547, 79682607852, 79880870482, 79624016396, 79282519444, 79620056122, 79964161646, 79624462057, 79624517832, 79283197967, 79188683454, 79054459629, 79197502669, 79054427180, 79283790576, 79034168572, 79188823461, 79288127615, 79283853282, 79064781009, 79188709384, 79624429909, 79620196936, 79632828700, 79887300860, 79614914297, 79614914297, 79881112692, 79064127185, 79624410011, 79283216823, 79682606000, 79054996570, 79383029883, 79624441319, 79887156533, 79620008881, 79624004601, 79624219447, 79675217460, 79064799934, 79187994858, 79624405999, 79620161265, 79964171337, 79633826519, 79624020126, 79887678888, 79624520403, 79614986529, 79614433107, 79283396058, 79624380964, 79614409999, 79064708000, 79880988222, 79682643905, 79614905666, 79283030000, 79624014014, 79288219184, 79286518383, 79624517832, 79383030020, 79283424419, 79288202819, 79624410441, 79288128635, 79682723366, 79880884227, 79624000975, 79624454061, 79034459472, 79034459472, 79887331408, 79280126062, 79283350407, 79682794671, 79624003350, 79682684547, 79614908276, 79197394283, 79624004797, 79682673711, 79188790550, 79624478377, 79624408180, 79188002700, 79624018945, 79034165309, 79880964252, 79624492485, 79624977007, 79620000213, 79615296555, 79660170006, 79887519957, 79054125812, 79054415353, 79614470000, 79227731610, 79383563950, 79624023294, 79682698970, 79187519474, 79624002666, 79054661428, 79885715602, 79624499088, 79624499088, 79899866831, 79283218080, 79283394181, 79964171770, 79283100090, 79887480813, 79054161090, 79064131238, 79614905666, 79624493954, 79911514878, 79620136663, 79624901554, 79064421000, 79283283133, 79187777792, 79614777776, 79899747454, 79660650896, 79624996460, 79899847966, 79620060030, 79064124158, 79682684547, 79911119343, 79283210203, 79280062079, 79283210207, 79064711688, 79187810164, 79624445277, 79280131819, 79899879199, 79624473909, 79887323913, 79110987187, 79283285879, 79097551777, 79899986197, 79197569244, 79161867801, 79286360821, 79195393476, 79197499184, 79883862222, 79964177797, 79624211520, 79887526110, 79188653868, 79187477075, 79383030611, 79187808348, 79187808348, 79187808348, 79881073007, 79624239977, 79288101000, 79187481974, 79093199116, 79624495550, 79101762869, 79280082060, 79614643892, 79682663664, 79624039595, 79624466211, 79057300360, 79197406052, 79034165309, 79887080383, 79216110811, 79150345994, 79624499299, 79282509427, 79187470237, 79187470237, 79188810424, 79320965002, 79614756005, 79881150689, 79604955149, 79187771984, 79280704220, 79624242999, 79887418103, 79887017337, 79181494998, 79964160026, 79964160026, 79624003880, 79624454708, 79614715186, 79283087302, 79624977007, 79187856110, 79884640880, 79624489500, 79187447911, 79624450457, 79286338099, 79624447722, 79624417977, 79624558022, 79632840133, 79624205555, 79064684054, 79633854195, 79887058085, 79624205555, 79887649532, 79283140555, 79620218648, 79187473497, 79097600539, 79614561649, 79889584862, 79064769155, 79880866206, 79620100192, 79620100192, 79682607852, 79614403883, 79682684547, 79383029883, 79887678888, 79620299060, 79682607852, 79272890838, 79283128933, 79187676764, 79614961111, 79624071271, 79034454168, 79054999908, 79624478375, 79258412903, 79624017484, 79624977007, 79187662583, 79283030000, 79880983312, 79187922621, 79887685391, 79287888819, 79614466273, 79287888819, 79283585165, 79384612040, 79682684547, 79624415005, 79054421111, 79282934304, 79660170006, 79034082666, 78612047440, 79880872222, 79887505076, 79064710521, 79282222023, 79614550005, 79994888802, 79998003553, 79674167612, 79887156533, 79899899601, 79097697017, 79280062079, 79620000056, 79283038030, 79034465782, 79283615172, 79064605353, 79624475770, 79188810424, 79197342894, 79187479807, 79187506665, 79187506665, 79283100359, 79282515336, 79283108287, 79185817505, 79888564898, 79624417977, 79614986529, 79899749356, 79288114742, 79288114742, 79054693447, 79624454708, 79614969727]

newcardclients = ['79282222023', '78612047440', '79624433222', '79887505076', '79097697017', '79899749356', '79881028521', '79214003307', '79383162615', '79887511016', '79333304044', '79054171001', '79283566499', '79187803044', '79283232639', '79185830416', '79293600009', '79129863639', '79624215048', '79624011169', '79182665836', '79187421835', '79804769247', '79999999159', '79614602976', '79618175840', '79871134752', '79280055950', '79187953350', '79054459629', '79188823461', '79181158981', '79632828700', '79188709384', '79283069909', '79288202819', '79687878788', '79682643905', '79054661428', '79899866831', '79911514878', '79614777776', '79187777792', '79660650896', '79064711688', '79883862222', '79624466211', '79320965002', '79604955149', '79150345994', '79161867801', '79286360821', '79181494998', '79101762869', '79216110811', '79964177797', '79624205555', '79624447722', '79624417977', '79187856110', '79880866206', '79620075955', '79881092013', '79286393162', '79624421700', '79054691934', '79054999908', '79258412903', '79887685391', '79614466273', '79287888819', '79241492601', '79887589217', '79064669999', '79288106984', '79034459164', '79283453125', '79283502939', '79624600158']

nm = ['79964177797', '79624011169', '79660650896', '79129863639', '79187803044', '79150345994', '79064711688', '79624466211', '79333304044', '79624417977', '79286360821', '79804769247', '79624215048', '79054459629', '79887685391', '79899749356', '79624447722', '79604955149', '79682643905', '79054661428', '79283502939', '79258412903', '79614466273', '79187953350', '79287888819', '79054999908', '79181158981', '79187421835', '79880866206', '79624205555', '79280055950', '79899866831', '79887511016', '79881028521', '79161867801', '79216110811', '79188709384', '79293600009', '79911514878', '79181494998', '79187856110', '79188823461', '79288202819', '79871134752', '79320965002', '79999999159', '79283566499', '79187777792', '79383162615', '79097697017', '79632828700', '79101762869', '79883862222', '79182665836', '79185830416', '79214003307', '79283069909', '79614777776', '79614602976']
def findallrec():

    url = f"https://api.yclients.com/api/v1/records/{salon_id}?start_date={startdate}&end_date={enddate}&include_finance_transactions=1&page=1&count=1000"

    payload = ""
    headers = {
      'Accept': 'application/vnd.yclients.v2+json',
      'Content-Type': 'application/json',
      'Authorization': 'u8xzkdpkgfc73uektn64, 85b4c66c5bf1954d3f4bc70e83aee91e',
      'Cookie': '__cf_bm=ZcwFYV34ZTN04vK242kNJkICexS16nuSunXoLrdbk_A-1678098711-0-AXTj07BANS+/snfjkXzaKBc2cykDSpYkXLcEei51V5nHFux6tvFsVxcIQcYZscCDCosmA0YOfINcF++c2TTPYT0=; _cfuvid=NkVUQHwY3JPI7H08gs2Xtqf6evkQf.YaTMBK4LLV0CY-1678098711597-0-604800000; auth=f5h1qav8jbiepmlvjd17hnplesoeb95mt4g9luq1m645ns8u2ld279k75sntonqm'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_pretty = response.json()
    return response_pretty



def parserdata(data):
    visit_ids = []
    clients = []
    phones = []
    for i in range(len(data)):
        print(data[i]["client"])
        if len(data[i]["client"]["phone"]) != 0:
            clients.append(data[i]["client"]["id"])
            visit_ids.append(data[i]["visit_id"])
            phones.append(data[i]["client"]["phone"])
    print(visit_ids)
    print(clients)
    print(phones)
    print(len(visit_ids))
    return visit_ids

def checkcart(clients, counter):
    url = f"https://api.yclients.com/api/v1/loyalty/cards/{clients}/485903/{salon_id}"
    payload = {}
    ids = []
    numn = -1
    services = []
    abon_num = []
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'u8xzkdpkgfc73uektn64, 85b4c66c5bf1954d3f4bc70e83aee91e',
        'Cookie': '__cf_bm=ZcwFYV34ZTN04vK242kNJkICexS16nuSunXoLrdbk_A-1678098711-0-AXTj07BANS+/snfjkXzaKBc2cykDSpYkXLcEei51V5nHFux6tvFsVxcIQcYZscCDCosmA0YOfINcF++c2TTPYT0=; _cfuvid=NkVUQHwY3JPI7H08gs2Xtqf6evkQf.YaTMBK4LLV0CY-1678098711597-0-604800000; auth=f5h1qav8jbiepmlvjd17hnplesoeb95mt4g9luq1m645ns8u2ld279k75sntonqm'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.json()
    if len(response_json['data']) == 0:
        return False
    else:
        pretty_output[counter]["client"] = clients
        pretty_output[counter]["card_id"] = response_json["data"][0]["id"]
        return True


def findalltrans():

    url = "https://api.yclients.com/api/v1/chain/485903/loyalty/transactions"

    payload = json.dumps({
        "created_after": f"{startdate}",
        "created_before": f"{enddate}",
        "type": 2,
        "count":1000
    })
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'u8xzkdpkgfc73uektn64, 85b4c66c5bf1954d3f4bc70e83aee91e',
        'Cookie': '__cf_bm=Uhr3hUKt2fLD3w33eJfH3oXNhOmKr4SzQMRbIX8.Xq4-1678099716-0-AVTa9w1EOruqyWtg+mEg2yq7fy28m9SZ3LGhk4YXIpdWNHnmkHoVDjtGH4vaHJrlC54cIqjn8weeFNw2hVINa1w=; _cfuvid=ktsinGSW.fAW70LLRyR92gyL7nWXM_SGcGFVgUmh_AM-1678099716152-0-604800000; auth=f5h1qav8jbiepmlvjd17hnplesoeb95mt4g9luq1m645ns8u2ld279k75sntonqm'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    pr_response = response.json()
    return pr_response

def parserloyal(data):
    visit_ids = []
    for i in range(len(data)):
        visit_ids.append(data[i]["visit_id"])
    # print(visit_ids)
    return visit_ids

# dataset = findallrec()
# transaction_data = findalltrans()

# visits = parserdata(dataset["data"])
# print(f"Получено визитов: {len(visits)}")

# loyalty_visits = parserloyal(transaction_data["data"])
# print(f"Получено визитов из лояльности: {len(loyalty_visits)}")

# visits = [x for x in visits if x not in loyalty_visits]

# print(f"Визиты ({len(visits)})шт, в которых нет по какой то причине начисления кэшбека: \n {visits}")

for i in range(len(nc)):
    checkcart(nc[i], i)
    pretty_output.append({})

def calcpayment(docid,counter):
    url = f"https://api.yclients.com/api/v1/company/{salon_id}/sale/{docid}"
    payload = {}
    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'u8xzkdpkgfc73uektn64, 85b4c66c5bf1954d3f4bc70e83aee91e',
        'Cookie': '__cf_bm=Uhr3hUKt2fLD3w33eJfH3oXNhOmKr4SzQMRbIX8.Xq4-1678099716-0-AVTa9w1EOruqyWtg+mEg2yq7fy28m9SZ3LGhk4YXIpdWNHnmkHoVDjtGH4vaHJrlC54cIqjn8weeFNw2hVINa1w=; _cfuvid=ktsinGSW.fAW70LLRyR92gyL7nWXM_SGcGFVgUmh_AM-1678099716152-0-604800000; auth=f5h1qav8jbiepmlvjd17hnplesoeb95mt4g9luq1m645ns8u2ld279k75sntonqm'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    pr_response = response.json()
    paydata = pr_response["data"]["state"]["payment_transactions"]
    print(f'принт новый: {paydata}')
    summ = 0
    allsumm = 0
    for i in range(len(paydata)):
        if paydata[i]["sale_item_type"] == "service":
            summ += paydata[i]["amount"]
        allsumm += paydata[i]["amount"]

    print(f'Сумма оплаты: {summ}')
    print(f'Общая сумма: {allsumm}')
    print(counter)
    pretty_output[counter]["summ"] = summ
    pretty_output[counter]["cashback"] = summ*0.05
    return pr_response



def parsernew(data):
    doc_id = []
    clphone = []
    # pprint.pprint(data[1])
    for i in range(len(data)):
        print(i)
        if data[i]["visit_id"] in visits:
            # print(data[i]["client"])
            pretty_output[i]["client"] = data[i]["client"]["name"]
            pretty_output[i]["phone"] = data[i]["client"]["phone"]
            pretty_output[i]["doc_id"] = data[i]["documents"][0]["id"]
            pretty_output[i]["url"] = f"https://yclients.com/timetable/{salon_id}#main_date=2023-03-02&open_modal_by_record_id={data[i]['id']}"
            if checkcart(data[i]["client"]["phone"]):
                print(f'Карта есть, думаем че дальше, клиент {data[i]["client"]["phone"]}')
                pretty_output[i]["status"] = "Карта есть, будем начислять"
                calcpayment(data[i]["documents"][0]["id"], i) # вызов функции (важно)
                doc_id.append(data[i]["documents"][0]["id"])
                clphone.append(data[i]["client"]["phone"])
            elif checkcart(data[i]["client"]["phone"]) == False:
                print("Карты у клиента нет")
                pretty_output[i]["status"] = "Карты нет"
            # print(pretty_output)
        pretty_output.append({})


    return doc_id, clphone





# doc_set, ph_set = parsernew(dataset["data"])
# print(doc_set)
# print(len(doc_set))

#
# calcpayment(doc_set[1])
# for i in range(len(doc_set)):
#     calcpayment(doc_set[i])


#
# print(ph_set)
# print(len(ph_set))
#
# common_elements = list(set(ph_set) & set(newcardclients))
# print("Клиенты, на которых надо обратить ввнимание: ")
# print(common_elements)

# print(pretty_output)
final = json.dumps(pretty_output, ensure_ascii=False)
f = open('newlog.txt', 'a')
f.write("\n")
f.write(final)
f.close()