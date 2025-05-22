# 📹 Video Ön İşleme Scripti README 🚀

**Video Ön İşleme Scripti**ne hoş geldiniz! Bu Python scripti, bir video dosyasından kareleri çıkarır, belirtilen bir çözünürlüğe yeniden boyutlandırır ve her birini ayrı görüntüler olarak kaydeder. Veri analizi, makine öğrenimi veya yaratıcı projeler için mükemmel! 🎥✨

## 📋 Genel Bakış

Bu script, bir video dosyasını (örneğin, `.mp4`) alır, her kareyi işler, hedef çözünürlüğe (varsayılan: 1920x1080) yeniden boyutlandırır ve PNG görüntüleri olarak belirtilen bir klasöre kaydeder. `imageio`, `Pillow` (PIL) ve `numpy` kütüphanelerini kullanır. 🖼️

## 🛠️ Özellikler

- **📂 Girdi Doğrulama**: Video dosyasının ve çıktı klasörünün varlığını kontrol eder.
- **🖼️ Kare Çıkarma**: Videodan her kareyi çıkarır.
- **📏 Yeniden Boyutlandırma**: Kareleri yüksek kaliteli Lanczos yöntemiyle hedef boyuta getirir.
- **💾 Kare Kaydetme**: Kareleri numaralandırılmış PNG dosyaları olarak kaydeder (örneğin, `frame_000.png`).
- **🚨 Hata Yönetimi**: İşlem sırasında hataları yakalar ve bildirir.

## 📦 Gereksinimler

Gerekli Python kütüphaneleri:
- `imageio` 📽️
- `Pillow` (PIL) 🖼️
- `numpy` 🔢
- `os` 🗂️

Kurulum:
pip install imageio pillow numpy imageio-ffmpeg

📜 Kullanım
Ortamı Hazırlayın : Gerekli turnuvalara katılın.
Scripti çalıştırın : video_path ve Output_dir değişkenlerini güncelleyin:

video_path = "ornek_video.mp4"  # Video dosyanızın yolu
output_dir = "kareler"          # Çıktı klasörü
preprocess_video(video_path, output_dir)

Çıktıyı Kontrol Edin : Kareler kareler bölümlerinde Frame_000.png gibi saklandı. ✅

⚠️ Noterler
Video formatının imageio tarafından desteklendiğinden emin olun (örneğin, .mp4 , .avi ). 📽️
Büyük videolar için yeterli disk alanında olduğundan emin olun. 💽
Hatalar için konsol çıkışını kontrol edin. 🕵️‍♂️

🌟 Katkıda Bulunma
Senaryonun yayılması için önerileriniz varsa, fork edin ve pull request gönderin! 🤝

Mutlu video işleme! 🎥🚀
