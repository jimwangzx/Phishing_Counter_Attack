import random
import requests
import json



spam_count= int(input("How many logins should I send?   "))

first_names='first_names.txt'
last_names = 'last_names.txt'
first_name_list = []
last_name_list = []
email_list = []
password_list = []
email_extension = 'email_extensions.txt'
password_file = 'rockyou.txt'
username = ""
password = ""
url = 'https://diaztreeandlawnservice.com/4333/log.php'
headers = {
    "Accept-Encoding": "gzip,deflate,br",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "diaztreeandlawnservice.com",
    "Origin": "https://copper-diagnostic-pony.glitch.me",
    "Refer": "https://copper-diagnostic-pony.glitch.me",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
    "Accept": "text/html, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Length": "12",
}
def post_spammer():

    with open(first_names, "r") as f:
        lines = f.readlines()
        for i in range(spam_count):
            firstname = random.choice(lines)
            firstname=firstname.rstrip()
            first_name_list.append(firstname)

    with open(last_names,encoding = "ISO-8859-1") as f:
        lines = f.readlines()
        for i in range(spam_count):
            lastname = random.choice(lines)
            lastname = lastname.rstrip()
            lastname = lastname.title()
            last_name_list.append(lastname)

    with open(email_extension) as f:
        lines = f.readlines()
        for i in range(spam_count):
            email = random.choice(lines)
            email = email.rstrip()
            email_list.append(email)

    with open(password_file,encoding = "ISO-8859-1") as f:
        lines = f.readlines()
        for i in range(spam_count):
            password = random.choice(lines)
            password = password.rstrip()
            password_list.append(password)

    for i in range(spam_count):        
        username = first_name_list[i] + last_name_list[i] +str(random.randint(0, 99))+ email_list[i]
        password = password_list[i]

        payload = {"u":username,"p":password}

        #r = requests.post(url, data=json.dumps(payload), headers=headers)
        requests.post(url, data=json.dumps(payload), headers=headers)
        print("Login ", i)
        print("Username: ", username)
        print("Password: ", password,"\n")
        #print(r.content)

post_spammer()
