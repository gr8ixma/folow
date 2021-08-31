import requests
import random
import faker

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
print(R+'''
           Followers
/---------------------------------\\

code by : ABDULLAH AL-RUQAISHI
Telegram : @EDISONpy

\---------------------------------/
''')
def Folowers(user, time):
    username = user
    obj = faker.Factory().create()
    email =  obj.email()
    url = 'https://core.poprey.com/api/create_test_order.php'
    headers = {
	    'accept': 'application/json, text/plain, */*',
	    'accept-encoding': 'gzip, deflate, br',
	    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	    'content-length': '105',
	    'content-type': 'application/x-www-form-urlencoded',
	    'dnt': '1',
	    'origin': 'https://poprey.com',
	    'referer': 'https://poprey.com/',
	    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
	    'x-auth-token': 'null',
	    'x-target-lang': 'en'
    }
    data = {
	    'service': 'Followers',
	    'email': email,
	    'username': username,
	    'system': 'Instagram',
	    'plan': '10',
	    'tariff': 'normal',
	    'csrf':''
    }
    req = requests.post(url,headers=headers,data=data)
    if req.status_code == 200:
	    print(G+f'Request {time} sent ✅. ')
    else:
	    print(G+f'Request {time} not sent ❌. ')

username = input('[+] Username : ')
times = int(input('[+] How many : '))

for i in range(1, times):
	Folowers(username, i)