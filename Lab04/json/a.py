import json
with open('/Users/esrarustemoglu/Desktop/Labs/Lab04/json/sample-data.json', 'r') as file:
    a = json.load(file)

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")

for x in a["imdata"]:
    print(f"{x['l1PhysIf']['attributes']['dn']:<50} {x['l1PhysIf']['attributes']['descr']:<20} {x['l1PhysIf']['attributes']['speed']:<9} {x['l1PhysIf']['attributes']['mtu']}")

