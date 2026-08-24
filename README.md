# NEXUS-SCAN

### Python TCP Ağ Tarama ve Analiz Aracı

NEXUS-SCAN, Python kullanılarak geliştirilmiş temel bir TCP ağ tarama ve analiz aracıdır.

Proje; Python socket programlama, TCP bağlantıları, IP adresleri, portlar, timeout yönetimi ve temel ağ güvenliği konularını öğrenmek amacıyla geliştirilmiştir.

---

## 🚀 Özellikler

- TCP port taraması
- Tek port taraması
- 1-65535 arasındaki TCP portlarını tarama
- Hedef IP adresinin erişilebilirlik kontrolü
- Açık ve kapalı portları gösterme
- Tarama sırasında tarih ve saat bilgisi gösterme
- Servis/banner bilgisi alma modu
- Yardım menüsü
- `exit` komutu ile programdan çıkış
- TCP bağlantılarında timeout kullanımı

---

## 🛠️ Kullanılan Teknolojiler

- Python 3
- `socket`
- `subprocess`
- `datetime`

---

## 📂 Proje Yapısı

NEXUS-SCAN/
│
├── porttarama1.py
└── README.md

---

## ⚙️ Kurulum

Python 3 kurulu olduğundan emin olun.

Projeyi GitHub üzerinden indirin:

git clone https://github.com/serhansima283-hub/NEXUS-SCAN.git

Proje klasörüne girin:

cd NEXUS-SCAN

Programı çalıştırın:

python porttarama1.py

---

## ▶️ Kullanım

Program başlatıldığında hedef IP adresi girilir.

Örnek:

Hedef IP Adresi >> 192.168.1.1

Hedef erişilebilir durumdaysa port taraması başlatılır.

Belirli bir portu taramak için port numarasını girin:

Taramak istediğiniz portu giriniz >> 80

Tüm TCP portlarını taramak için port girişini boş bırakabilirsiniz.

Program 1 ile 65535 arasındaki portları kontrol eder.

---

## 🧰 Komutlar

- `-h` veya `--help` → Yardım menüsünü gösterir.
- `-vs` → Servis/banner bilgisi alma modunu etkinleştirir.
- `exit` → Programdan çıkar.

---

## 🔎 Servis / Banner Modu

`-vs` komutu etkinleştirildiğinde NEXUS-SCAN, açık portlardan mümkün
olduğu durumlarda servis/banner bilgisi almaya çalışır.

Her servis banner bilgisi göndermediğinden bazı açık portlarda servis
bilgisi alınamayabilir.

---

## 🕐 Timeout

NEXUS-SCAN TCP bağlantıları için varsayılan olarak 1 saniyelik timeout
kullanmaktadır.

Bu değer, bağlantı kurulamadığında programın ne kadar bekleyeceğini
belirler.

---

## 📚 Öğrenme Amaçları

Bu proje geliştirilirken aşağıdaki konular üzerinde çalışılmıştır:

- Python socket programlama
- TCP bağlantıları
- IP adresleri
- Port kavramı
- `connect_ex()` kullanımı
- `subprocess` kullanımı
- `datetime` kullanımı
- Fonksiyonlar
- Döngüler
- Koşullu ifadeler
- Timeout mantığı
- Terminal tabanlı program geliştirme

---

# ⚠️ YASAL VE ETİK KULLANIM

NEXUS-SCAN yalnızca eğitim, araştırma ve yetkili güvenlik testleri
amacıyla kullanılmalıdır.

Yalnızca sahibi olduğunuz veya tarama yapmak için açıkça izin aldığınız
sistemlerde kullanın.

İzinsiz şekilde başkalarının bilgisayarlarını, sunucularını veya
ağlarını taramayın. Elde edilen bilgileri kötüye kullanmayın ve
sistemlere zarar vermeye veya yetkisiz erişim sağlamaya çalışmayın.

Programın izinsiz, yasa dışı veya kötü amaçlı kullanımından doğabilecek
sonuçlardan geliştirici sorumlu değildir.

Programı kullanan kişi, gerçekleştirdiği işlemlerden ve bu işlemlerin
yasal sonuçlarından kendisi sorumludur.

---

## 📌 Sürüm

NEXUS-SCAN v1.0.0

İlk sürüm.

---

## 🔮 Gelecek Geliştirmeler

- Daha gelişmiş timeout seçenekleri
- Geliştirilmiş servis tespiti
- Daha gelişmiş hata yönetimi
- Tarama sonuçlarını dosyaya kaydetme
- Gelişmiş terminal arayüzü
- Yeni tarama seçenekleri

---

## 👨‍💻 Proje

NEXUS-SCAN

Python ile geliştirilmiş eğitim amaçlı TCP ağ tarama ve analiz aracıdır.
