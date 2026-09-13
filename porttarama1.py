import socket
import subprocess
import platform
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

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

def port_tara(hedef, port, versiyon_modu):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)  # Eşzamanlı tarama için ideal ve güvenli timeout
        baglanti = s.connect_ex((hedef, port))
        
        if baglanti == 0:
            servis_mesaji = ""
            if versiyon_modu:
                try:
                    s.settimeout(0.5)
                    bilgi = s.recv(1024)
                    if bilgi:
                        servis_mesaji = f" ── Servis: {bilgi.decode(errors='ignore').strip()}"
                except:
                    pass
            s.close()
            print(f"[+] Port {port}: Açık{servis_mesaji}")
            return port
        s.close()
    except:
        pass
    return None

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
                     AĞ TARAMA VE ANALİZ ARACI (HIZLI MOD)
        """)
        continue

    print(f"[*] {hedef} adresi kontrol ediliyor...")
    if not ping(hedef):
        print("[-] Hedef aktif değil veya erişilemiyor.")
        continue
    
    print("[+] Hedef aktif. Hızlı tarama başlatılıyor...")

    port_girdisi = input("Taramak istediğiniz portu giriniz. Tüm portları taramak için boş geç >> ")
    acik_portlar = []
    baslangic_zamani = datetime.now()

    if port_girdisi == "":
        print("[*] 1 - 65535 aralığı çoklu iş parçacığı (Threads) ile taranıyor...")
        
        # Aynı anda 200 bağlantı açarak hızı maksimuma çıkarıyoruz
        with ThreadPoolExecutor(max_workers=200) as executor:
            futures = {executor.submit(port_tara, hedef, port, versiyon_modu): port for port in range(1, 65536)}
            
            for future in as_completed(futures):
                sonuc = future.result()
                if sonuc:
                    acik_portlar.append(sonuc)

        bitis_zamani = datetime.now()
        acik_portlar.sort()
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
            print("[-] Hatalı giriş! Lütfen geçerli bir sayı girin veya tümü için boş bırakın.")
