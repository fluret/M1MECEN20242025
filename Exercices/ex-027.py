# 1
mon_dic = {}
print(mon_dic)
# 2
mon_dic["yes"] = "oui"
mon_dic["no"] = "non"
mon_dic["why"] = "pourquoi"
print(mon_dic)
# 3
mon_dic2 = dict(si='oui', no='non', porque='pourquoi')
print(mon_dic2)
# 4
mon_dic3 = dict([("si", "oui"), ("no", "non"), ("porque", "pourquoi")])
print(mon_dic3)
# 5
for val in mon_dic3.values():
    print(val)
# 6
for key in mon_dic3.keys():
    print(key)
# 7
for key, val in mon_dic3.items():
    print(f'A la clé "{key:<12}" correspond la valeur : "{val}"')
# 8
print(mon_dic["why"])
print(mon_dic.get("why"))
# 9
# print(mon_dic["how"])
print(mon_dic.get("how"))
# 10
print(mon_dic["yes"])
mon_dic["yes"] = "affirmatif"
print(mon_dic["yes"])
# 11
print(mon_dic2)
del mon_dic2["si"]
print(mon_dic2)
# 12
mon_dic3.clear()
print(mon_dic3)
