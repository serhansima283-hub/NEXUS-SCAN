import socket
import subprocess
import platform
from datetime import datetime

def ping(hedef):
    parametre = "-n" if platform.system().lower() == "windows" else "-c"
    timeout_parametre = "-w" if platform.system().lower() == "windows" else "-W"
    timeout_deger = "500" if platform.system().lower() == "windows" else "0.5"
    
    sonuc = subprocess.run(
        ["ping", parametre, "1", timeout_parametre, timeout_deger, hedef],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return sonuc.returncode == 0

versiyon_modu = False

while True:
    hedef = input("\nYardım Menüsü (--help veya -h) , Hedef IP Adresi >> ").strip()

    if not hedef:
        continue

    if hedef.lower() == "exit":
        print("Programdan Çıkılıyor...")
        break

    if hedef == "-vs":
        versiyon_modu = True
        print("[+] Versiyon Modu Aktif")
        continue

    if hedef in ("--help", "-h"):
        print("""
            ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
            ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
            ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
            ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚══██╔╝
            ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║
            ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝

                        N E X U S - S C A N
                     AĞ TARAMA VE ANALİZ ARACI

        ╭────────────────────────────────────────────────────────╮
        │                    SİSTEM BİLGİSİ                      │
        │                                                        │
        │  Sürüm        : 1.0.1 (Stabil)                         │
        │  Motor        : Python Socket                          │
        │  Protokol     : TCP / IPv4                             │
        │  Durum        : ● HAZIR                                │
        ╰────────────────────────────────────────────────────────╯

        ╭────────────────────────────────────────────────────────╮
        │                        KOMUTLAR                        │
        │                                                        │
        │  [ -h ]       Yardım menüsü                            │
        │  [ -vs ]      Servis / sürüm bilgisi                   │
        │  [ exit ]     Programdan çıkış                         │
        ╰────────────────────────────────────────────────────────╯

        ╭────────────────────────────────────────────────────────╮
        │                         TARAMA                         │
        │                                                        │
        │  Hedef IP     → Hedef IP adresini gir                  │
        │  Port         → Port numarası gir                      │
        │  Boş Port     → Tüm portları tara                      │
        │  Timeout      → Varsayılan: 0.5 saniye                 │
        ╰────────────────────────────────────────────────────────╯

                    NEXUS-SCAN  >  HAZIR
        """)
        continue

    print(f"[*] {hedef} adresi kontrol ediliyor...")
    if not ping(hedef):
        print("[-] Hedef aktif değil veya erişilemiyor.")
        continue
    
    print("[+] Hedef aktif. Tarama başlatılıyor...")

    port_girdisi = input("Taramak istediğiniz portu giriniz (Tümü için boş bırakın) >> ").strip()
    acik_portlar = []
    baslangic_zamani = datetime.now()

    if port_girdisi == "":
        print("[*] 1 - 65535 aralığındaki portlar taranıyor. Lütfen bekleyin...")
        for port in range(1, 65536):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.1) # Daha gerçekçi bir zaman aşımı
                baglanti = s.connect_ex((hedef, port))

                if baglanti == 0:
                    print(f"[+] Port {port}: Açık")
                    acik_portlar.append(port)

                    if versiyon_modu:
                        try:
                            s.settimeout(1.0)
                            bilgi = s.recv(1024)
                            if bilgi:
                                print(f"    └── Servis: {bilgi.decode(errors='ignore').strip()}")
                        except:
                            pass
                s.close()
            except KeyboardInterrupt:
                print("\n[-] Tarama kullanıcı tarafından durduruldu.")
                break
            except Exception:
                pass

        bitis_zamani = datetime.now()
        print("\n========== TARAMA RAPORU ==========")
        print(f"Tarama Süresi   : {bitis_zamani - baslangic_zamani}")
        print(f"Açık port sayısı: {len(acik_portlar)}")
        print(f"Açık portlar    : {acik_portlar}")

    else:
        try:
            port = int(port_girdisi)
            if not (1 <= port <= 65535):
                print("[-] Geçersiz port aralığı (1-65535 arasında olmalıdır).")
                continue

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            baglanti = s.connect_ex((hedef, port))

            if baglanti == 0:
                print(f"[+] Port {port} Açık")
                if versiyon_modu:
                    try:
                        s.settimeout(1.0)
                        bilgi = s.recv(1024)
                        if bilgi:
                            print(f"[+] Servis: {bilgi.decode(errors='ignore').strip()}")
                        else:
                            print("[-] Servis yanıt vermedi (Banner yok).")
                    except:
                        print("[-] Versiyon bilgisi alınamadı.")
            else:
                print(f"[-] Port {port} Kapalı")

            s.close()
        except ValueError:
            print("[-] Hatalı giriş! Lütfen geçerli bir sayı girin.")
