import requests
import time

print("! Type: https://Url Anda")
url = input("? Masukan URL: ")

def cek(url):
    try:
        reqet = requests.get(url)
        print("• Mengambil Data...\n");time.sleep(1)
        print(f"! Status Code: {reqet}")
    except (KeyError,IOError):
        exit("! URL Tidak Di Temukan")
    print(f"\n* Jika Status Code: <Response [200]> Anda Dapat Lansung Scrap Website {url} tanpa Headers ")
    print("\n* Jika Status Code: ±<Response [404]> Tandanya %s Harus memasukan Headers\n* Contoh:\n  headers= {'user-agent':'masukan User agent Anda'}\n  req = requests.get('%s', headers = headers)\n* Coba Print Lagi: print(req)\n* Jika <Response [200]> Berarti Website %s Sudah Bisa Di scrap"%(url,url,url)) 

if __name__ == '__main__':
    cek(url)
