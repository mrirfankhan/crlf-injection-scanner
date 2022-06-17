from logging import exception
import re
import requests
from colorama import Fore,Back,Style
import pyfiglet
  



def urlcheak(url):
	regex = ("((http|https)://)(www.)?" +
			"[a-zA-Z0-9@:%._\\+~#?&//=]" +
			"{2,256}\\.[a-z]" +
			"{2,6}\\b([-a-zA-Z0-9@:%" +
			"._\\+~#?&//=]*)")

	comp = re.compile(regex)

	if(re.search(comp, url)):
		return True
	else:
		return False

if __name__=="__main__":
    result = pyfiglet.figlet_format("CRLF injection Scanner ", font = "slant" )
    print(result)
    print(Fore.MAGENTA+"Author :Mrirfan ")
    print(Fore.MAGENTA+"twitter: https://twitter.com/python073")
    print()
    print(Fore.LIGHTYELLOW_EX+"[Note]",Fore.GREEN+'''Enter url example this format: https://google.com/''')
    try:
        url = input("")


        if(urlcheak(url) == True):
            file=open("crlfpayload.txt")
            for payload in file.readlines():
                main=url+payload
                req=requests.get(main)
                if req.status_code==200:
                    if "Hacker-Test" in req.headers:
                        print(Fore.RED+f"Vulnerable url Find {main}")
                else:
                    print(Fore.YELLOW+f"[NOT Vulnerable] {Fore.LIGHTCYAN_EX} {main}")
    except:
        print("reason url endwith '/' ex: https://google.com/")
        print("reson second invalid url")
            

