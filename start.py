from requests import get
import json,random
import sys
from time import sleep as s
try:
    from pyfiglet import Figlet
    from colorama import Fore
except:
    import subprocess
    subprocess.call('pip install pyfiglet', shell=True)
    subprocess.call('pip install colorama', shell=True)
    from colorama import Fore
    from pyfiglet import Figlet
f = Figlet(font='slant')
list = ['sina maFia:)','HAcKeR', 'zheneral maFia']
printt = f.renderText(random.choice(list))+'\n'
print (Fore.RED+' ')
for l in printt:
    sys.stdout.write(l)
    sys.stdout.flush()
    s(0.01)
api = 'http://ip-api.com/json/'
ip = str(input(Fore.GREEN+'enter your ip: '))
pnokiyo = get(api+ip).json()
try:
   print (Fore.YELLOW+pnokiyo['org'])
except:
    print('eror...wrong ip')
