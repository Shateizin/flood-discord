import requests
import time
print('''
  \033[1;32m _____ __  _____  ______________  __
  / ___// / / /   |/_  __/ ____/ / / /
  \__ \/ /_/ / /| | / / / __/ / / / / 
 ___/ / __  / ___ |/ / / /___/ /_/ /  
/____/_/ /_/_/  |_/_/ /_____/\____/\033[m
                                      ''')
                                      
print("  \033[36mCOLE O TOKEN SE N NAO IRA FUNCIONAR\033m")
print("   A FERRAMENTA N RECONHECE SE ESTA CERTO O TOKEN")
id =	str(input("ID DO CHAT: "))
token = str(input("TOKEN: "))
msg = str(input("MENSAGEM: "))
def spam():
	payload = {
		'content': msg
	}
	
	header = {
	'authorization': token
	}
	
	r =	requests.post("https://discord.com/api/v8/channels/" + id + "/messages", data=payload, headers=header)
	
while True:
		spam()
	
