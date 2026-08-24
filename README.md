# NEXUS-SCAN

### Python TCP Ağ Tarama ve Analiz Aracı

**NEXUS-SCAN**, Python kullanılarak geliştirilmiş, TCP bağlantıları üzerinden
ağ üzerindeki portların durumunu kontrol etmeye yarayan basit bir ağ tarama
ve analiz aracıdır.

Bu proje özellikle **Python socket programlama, TCP bağlantıları, ağ
programlama ve temel siber güvenlik konularını öğrenmek** amacıyla
geliştirilmiştir.

---

## 🚀 Özellikler

NEXUS-SCAN aşağıdaki temel özelliklere sahiptir:

- TCP port taraması
- Tek bir portu tarama
- 1-65535 arasındaki portları tarama
- Hedef IP adresinin erişilebilirlik kontrolü
- Açık ve kapalı portları gösterme
- Port taraması sırasında tarih ve saat gösterme
- Servis/banner bilgisi alma modu
- Yardım menüsü
- `exit` komutu ile programdan çıkış
- Bağlantı zaman aşımı (`timeout`) kullanımı

---

## 🛠️ Kullanılan Teknolojiler

Proje Python'un standart kütüphaneleri kullanılarak geliştirilmiştir.

- **Python 3**
- `socket`
- `subprocess`
- `datetime`

---

## 📂 Proje Yapısı

```text
NEXUS-SCAN/
│
├── porttarama1.py
└── README.md
