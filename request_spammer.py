from os import system, name
from time import sleep
import random
import requests
import json



class return_fire():
    
    def __init__(self):

        self.clear()
        self.count = int(input("\nHow many login credentials should I send?   "))

        self.delay = False
        self.first_name_list = []
        self.last_name_list = []
        self.email_list = []
        self.password_list = []
        self.payload_list = []
        self.first_names = {"field":"first_name", "file":'./wordlist/first_names.txt', "encoding":"UTF-8", "payload":self.first_name_list}
        self.last_names = {"field":"last_name", "file":'./wordlist/last_names.txt', "encoding":"ISO-8859-1", "payload":self.last_name_list}
        self.email_extensions = {"field":"email_extension", "file":'./wordlist/email_extensions.txt', "encoding":"UTF-8", "payload":self.email_list}
        self.passwords = {"field":"password", "file":'./wordlist/rockyou.txt', "encoding":"ISO-8859-1", "payload":self.password_list}
        self.master_dictionary=[self.first_names, self.last_names, self.email_extensions, self.passwords]
        
        self.url = 'https://diaztreeandlawnservice.com/4333/log.php'

        self.headers = {
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

        self.body = {
            "u":'',
            "p":'',
        }

        choice = input("\nDelay between sending logins?   (y/n):  ")
        if choice == 'y':
            self.delay = True
            self.min_sleep = int(input("\nMinimum time to wait (seconds):  "))
            self.max_sleep = int(input("Maximum time to wait (seconds):  "))

        print("\nBuilding Attack Lists....\n")
        self.payload_builder()
        self.post_request_sender()

    

    def clear(self):
        if name == 'nt':
            _=system('cls')
        else:
            _=system('clear')


    def payload_builder(self):
        for item in self.master_dictionary:
            # open file and set the encoding type
            with open(item["file"],encoding = item["encoding"]) as f:
                lines = f.readlines()
                for i in range(self.count):
                    #Creates a name variable dynamically from the current field name by using a dictionary key
                    globals()[item["field"]] = random.choice(lines)
                    #.rstrip() removes line breaks
                    string = globals()[item["field"]].rstrip()
                    #capitilize the string if it is the beginning of a first/last name
                    if item["field"] == "first_name" or item["field"] == "last_name":
                        string = string.title()
                    item["payload"].append(string)

        for i in range(self.count):        
            username = self.first_name_list[i] + self.last_name_list[i] + self.email_list[i]
            password = self.password_list[i]
            self.payload_list.append({'u':username, 'p':password})

    def post_request_sender(self):
        for i in range(self.count):        
            #r = requests.post(url, data=json.dumps(payload), headers=headers)
            requests.post(self.url, data=json.dumps(self.payload_list[i]), headers=self.headers)
            print("\nLogin ", i)
            print("Username: ", self.payload_list[i]['u'])
            print("Password: ", self.payload_list[i]['p'])

            if self.delay == True:
                sleep(random.randint(self.min_sleep,self.max_sleep))
            #print(r.content)

return_fire()