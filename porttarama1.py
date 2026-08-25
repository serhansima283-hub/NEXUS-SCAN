import socket
import subprocess
from datetime import datetime

def ping(hedef):
    sonuc = subprocess.run(
        ["ping", "-c", "1", "-W", "0.5", hedef],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return sonuc.returncode == 0

versiyon_modu = False

while True:
    
    hedef = input("Yardım Menüsü (--help veya -h) , Hedef IP Adresi >> ")

    if hedef.lower() == "exit":
        print("Programdan Çıkılıyor...")
        break

    if hedef == "-vs":
        versiyon_modu = True
        print("[+] Versiyon Modu Aktif")
        continue

    if hedef == "--help" or hedef == "-h":
        print("""
            
              ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
              ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
              ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
              ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║
              ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║
              ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝

                       N E X U S - S C A N
                    AĞ TARAMA VE ANALİZ ARACI

    ╭────────────────────────────────────────────────────────╮
    │                    SİSTEM BİLGİSİ                      │
    │                                                        │
    │  Sürüm       : 1.0.0                                   │
    │  Motor       : Python Socket                           │
    │  Protokol    : TCP / IPv4                              │
    │  Durum       : ● HAZIR                                 │
    ╰────────────────────────────────────────────────────────╯

    ╭────────────────────────────────────────────────────────╮
    │                       KOMUTLAR                         │
    │                                                        │
    │  [ -h ]       Yardım menüsü                            │
    │  [ -vs ]      Servis / sürüm bilgisi                   │                     
    │  [ exit ]     Programdan çıkış                         │
    ╰────────────────────────────────────────────────────────╯

    ╭────────────────────────────────────────────────────────╮
    │                       TARAMA                           │
    │                                                        │
    │  Hedef IP    →  Hedef IP adresini gir                  │
    │  Port        →  Port numarası gir                      │
    │  Boş Port    →  Tüm portları tara                      │
    │  Timeout     →  Varsayılan: 1 saniye                   │
    ╰────────────────────────────────────────────────────────╯

                    NEXUS-SCAN  >  HAZIR
        """)
        continue
    if not ping(hedef):
        print("[-] Hedef aktif değil veya erişilemiyor.")
        continue
    
    print("[+] Hedef aktif. Tarama başlatılıyor...")

    port_girdisi = input(
        "Taramak istediğiniz portu giriniz. "
        "Tüm portları taramak için boş geç >> "
    )

    # Kullanıcı boş bıraktıysa
    if port_girdisi == "":
        for port in range(1, 65536):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.002)
            tarih = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"[{tarih}] {port} numaralı porta bağlanılıyor...")
            baglanti = s.connect_ex((hedef, port))

            if baglanti == 0:
                print(f"{port} Açık")

                if versiyon_modu:
                    try:
                        bilgi = s.recv(1024)
                        print("[+] Servis:", bilgi.decode(errors="ignore").strip())
                    except:
                        print("[-] Versiyon bilgisi alınamadı.")

            s.close()

    # Kullanıcı bir port numarası girdiyse
    else:
        port = int(port_girdisi)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        baglanti = s.connect_ex((hedef, port))

        if baglanti == 0:
            print(f"{port} Açık")

            if versiyon_modu:
                try:
                    bilgi = s.recv(1024)
                    print("[+] Servis:", bilgi.decode(errors="ignore").strip())
                except:
                    print("[-] Versiyon bilgisi alınamadı.")
        else:
            print(f"[+] {port} Kapalı")

        s.close()
