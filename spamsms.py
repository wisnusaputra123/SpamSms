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
\033[37;1m┃   \033[33;1m○  \033[37;1m ┃ \033[35;1m |\033[37;1m Github\033[31;1m :\033[32;1m github.com/wisnusaputra123 \033[35;1m|
\033[37;1m╰━━━━━━━╯ \033[35;1m +-----------------------------+
\033[31;1m+==========================================+"""

def tik():
    animation = '|/-\\'
    for i in range(100):
        time.sleep(0.1)
        sys.stdout.write('\r\033[32;1m[=]\033[37;1m Sedang Transfer \033[31;1m' + animation[(i % len(animation))])
        sys.stdout.flush()


def rog():
    try:
        os.system('clear')
        print logo
        print '\033[35;1m==[\033[31;1m Note :\033[37;1m Jangan Menggunakan Titik Atau Koma\n           \033[37;1mUntuk Memasukan Jumlah Spam\n\033[35;1m==[\033[31;1m Ex   :\033[37;1m 50000'
        print "\033[31;1m+==========================================+"
        nomor = raw_input('\033[32;1m[✓]\033[37;1m Masukan Nomor Hp Korban\033[35;1m =>\033[32;1m ')
        jumlh = raw_input('\033[32;1m[✓]\033[37;1m Masukan Jumlah Spam \033[35;1m =>\033[32;1m ')
        tik()
        urllib2.urlopen('https://sinafipika.000webhostapp.com/sms.php/sms.php?nomor=' + nomor + '&paket=' + jumlh)
        cek = open('bukti.txt','w')
        cek.write('Spam Sudah Dikirim Ke Target Follow Instagram wisnu_as123\n\n')
        cek.write('Nomor Hp Korban : '+nomor)
        cek.write('\nJumlah Spam : '+jumlh)
        cek.write('\n\nTerima Kasih Sudah Memakai Tools Saya Follow Instagram wisnu_as123')
        cek.write('\n\n===[ THX : Wisnu Saputra && CyberTCA ]===')
        cek.close()
        os.system('mv -f bukti.txt /storage/emulated/0')
        print "\n\033[31;1m+==========================================+"
        print '\033[32;1m[✓]\033[37;1m Spam Berhasil Di Kirim'
        print '\033[32;1m[✓]\033[37;1m Bukti Pengiriman\033[31;1m :\033[36;1m /storage/emulated/0/bukti.txt\n\n'
    except:
    	print "\n\033[31;1m+==========================================+"
        print '\033[31;1m[×]\033[37;1m Server Operator Sedang Bermasalah\n    Cobalah Untuk Sesaat Lagi\n\n'
        sys.exit()

rog()

