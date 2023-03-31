import urllib.request, json

for_check_file = open("for_check.txt",'r')
nicknames = []
for i in range(742):
    nick = for_check_file.readline()
    if len(nick)>2:
        nicknames.append(nick[0:-1])
out = open("after_check.txt", 'w')
for nick in nicknames:
    request = f"https://api.wotblitz.ru/wotb/account/list/?application_id=f35eae96ca784b31d1a85c258e31eab9&search={nick}&type=exact"
    data = json.load(urllib.request.urlopen(request))
    out.write(str(data['meta']['count'])+' '+nick+'\n')