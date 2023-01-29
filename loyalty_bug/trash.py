import requests
import json

import json

with open("file.json", "r") as f:
    indata = f.read()

pretty_data = json.loads(indata)
data = pretty_data["data"]

kkm_array = []
doc_array = []

for i in range(0, len(data)):
    kkm_id = data[i]["id"]
    doc_id = data[i]["document_id"]
    kkm_array.append(kkm_id)
    doc_array.append(doc_id)

print(f"UPDATE documents SET bill_print_status = 1 WHERE id in {doc_array};")
print(f"UPDATE kkm_transactions SET status = 3 WHERE id in {kkm_array};")
#
# with open('sql_line.csv', 'a') as outfile:
#     json.dump(new_return, outfile)
# f = open('sql_line.csv', 'a')
# f.write('\n')
# f.close()
