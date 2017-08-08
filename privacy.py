import requests
import json

def createCard(name, limit):
	
	addCartURL = "https://privacy.com/api/v1/card"
	
	pay = {
		"panWithSpaces":"XXXX XXXX XXXX XXXX",
		"expMonth":"XX",
		"expYear":"XXXX",
		"CVV":"XXX",
		"reloadable": False,
		"spendLimit": int(limit),
		"spendLimitDuration":"MONTHLY",
		"memo": name
		}
		
	r = s.post(addCartURL, data = json.dumps(pay), headers = headers)
	
	if r.status_code == 200:
		
		card = r.json()
		
		print("")
		print(card["card"]["pan"])
		print(card["card"]["expMonth"] + "/" + card["card"]["expYear"])
		print(card["card"]["cvv"])
	
	

############ Set Up ###############
email = "example@gmail.com" 
password = "password"

fixed_limit = True                  # False: If you want to customize card limits and name otherwise keep True 
my_limit = "100"    				# Set limit: Make sure to keep in " "
card_name = "Card"					# When creating multiple cards Names will appear as card_name0, card_name1 ...

############ Set Up ###############

s = requests.Session()

loginURL = "https://privacy.com/auth/local"

pay = {
	"email": email,
	"password": password,
	"extensionInstalled": False 
}

headers = {
	"Host": "privacy.com",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0",
	"Accept": "application/json, text/plain, */*",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate, br",
	"Referer": "https://privacy.com/login",
	"Content-Type": "application/json;charset=utf-8",
	"Content-Length": "90",
	"DNT": "1",
	"Connection": "keep-alive"
	}

r = s.post(loginURL, data = json.dumps(pay), headers = headers)


if r.status_code == 200:
	
	response = r.json()
	cookies = s.cookies.get_dict()
	sessionID = cookies["sessionID"]
	token = response["token"]
	headers["Authorization"] = "Bearer " + token
	headers["Cookie"] = "sessionID={}; token={}".format(sessionID, token)
		
	print("Logged in\n")
	
	numberOfCards = input("How many cards do you want? ")
	
	for i in range(0, int(numberOfCards)):
		
		if not fixed_limit:
			
			name = input("\n\nEnter card name: ")
			limit = input("Enter card limit: ")
			
		else:
			
			limit = my_limit
			name = card_name + str(i)
			
			
		createCard(name, limit)	
else:
	
	print("Error logging in")