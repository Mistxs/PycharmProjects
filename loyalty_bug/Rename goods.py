import requests
import json

g_id, cat_id, sale_unit_id, service_unit_id = [], [], [], []


def get_data(goods):
    url = f"https://api.yclients.com/api/v1/goods/314673/{goods}"

    payload = {}

    headers = {
        'Accept': 'application/vnd.yclients.v2+json',
        'Content-Type': 'application/json',
        'Authorization': 'rj257pguzmdk9fgaz8cr, e69793634796c00b57cb4bfd34f361d8',
        'Cookie': '__cf_bm=zaTwvi9WHHYhDHt5E2_oFZAD1b3FCK8dsCIrNTOXgPs-1675077839-0-AQ898KarWIlZNayh+rTxqOmGs33mm6R4GSq5FatqQBl3bzoyfsklMcEoF5Cb1s2GkGwh7NlUdd82eW7mZKM7Tao=; _cfuvid=Wu9M0SCc01UFqhdTxC_lp3g.uUfS4pLrtyuzXs6e0tI-1675065535469-0-604800000; auth=1ssiuqf71r7sethgdi176k8ll6gju5tc8rapffud16sqa5oihdh01s13sjlj7jjb'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    request_data = response.json()
    # print(request_data)
    # g_id.append(request_data["data"]["id"])
    cat_id.append(request_data["data"]["category_id"])
    sale_unit_id.append(request_data["data"]["unit_id"])
    service_unit_id.append(request_data["data"]["service_unit_id"])

    return cat_id, sale_unit_id, service_unit_id


load = [15458306, 16363889, 16363920, 16363924, 16364235, 16364591, 16364737, 16479703, 18514155, 18514197, 18514467,
        18514479, 18558192, 18558227, 18558259, 18558285, 18558358, 18558395, 18558450, 18558472, 18558567, 18558612,
        18558805, 18558930, 18558989, 18559038, 18560606, 18562156, 18562184, 18562231, 18676920, 20530898, 20533644,
        20591905, 20591910, 20592024, 20680170, 20705859, 20889978, 20932633, 21198762, 21198763, 21198789, 21198792,
        21199271, 21199272, 21199274, 21199275, 21199276, 21199277, 21199278, 21199279, 21199280, 21199281, 21199282,
        21199283, 21199284, 21199285, 21199286, 21199287, 21199288, 21199289, 21199290, 21199291, 21199292, 21199293,
        21199294, 21199295, 21199296, 21199297, 21199298, 21199299, 21199300, 21199301, 21199302, 21199303, 21199304,
        21199305, 21199306, 21199307, 21199308, 21199309, 21199310, 21199311, 21199312, 21199313, 21199314, 21199315,
        21199316, 21199317, 21199318, 21199319, 21199320, 21199321, 21199322, 21199323, 21199324, 21199325, 21281319,
        21281321, 21440666, 21638810, 22327851, 22327855, 22327863, 22327887, 22327898, 23209770, 23604839, 23692410,
        23902128, 20984615]
# load = [15458306]
# print(load[0])
#
# get_data(16363889)
for i in range(len(load)):
    get_data(load[i])
    # print(cat_id)
# print(cat_id)
for i in range(len(cat_id)):
    print(cat_id[i], sale_unit_id[i], service_unit_id[i])
# print(g_id, cat_id, sale_unit_id, service_unit_id)
