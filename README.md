# Güvenli ve Zaafiyetli Flask Kullanıcı Yönetimi Uygulaması

Bu proje, Flask kullanarak basit bir kullanıcı yönetimi uygulamasını oluşturmayı amaçlamaktadır. İki farklı sürümü içerir: biri güvenli, diğeri ise SQL enjeksiyonlarına açık (zaafiyetli).

## Güvenli Kod Sürümü

### Özellikler

- Kullanıcı adı ve şifreleri veritabanında güvenli bir şekilde saklar (SHA-256 hash kullanımı).
- Kullanıcı girişi ve kaydı için parametreli SQL sorguları kullanılarak SQL enjeksiyonlarına karşı koruma sağlar.
- Flask Session kullanılarak güvenli oturum yönetimi.

### Kurulum

1. Python'u yükleyin (eğer yüklü değilse): [Python İndirme Sayfası](https://www.python.org/downloads/)
2. Proje dosyalarını bilgisayarınıza indirin.
3. Terminal veya Komut İstemi'ni açın ve proje dizinine gidin.
4. Gerekli bağımlılıkları yüklemek için terminalde aşağıdaki komutu çalıştırın:

    ```bash
    pip install -r requirements.txt
    ```

5. Uygulamayı başlatmak için terminalde aşağıdaki komutu çalıştırın:

    ```bash
    python secure_app.py
    ```

6. Tarayıcınızda `http://127.0.0.1:5000/` adresine gidin.

### Güvenlik Önlemleri

- Kullanıcıdan alınan veriler güvenlik açısından temizlenir (Bleach kullanımı).
- Şifreler güvenli bir şekilde hashlenir (SHA-256).

## Zaafiyetli Kod Sürümü

### Özellikler

- SQL enjeksiyonlarına karşı savunmasızdır.
- Kullanıcı girişi ve kaydı için güvensiz SQL sorguları kullanır.
- Şifreler düz metin olarak saklanır, güvenli bir hash kullanılmaz.

### Uyarı

Bu sürüm, güvenlik açısından ciddi riskler içerir ve gerçek bir projede kullanılmamalıdır.

## Katkıda Bulunma

Eğer bu projeye katkıda bulunmak istiyorsanız, lütfen forklayın ve pull request gönderin. Her türlü katkı ve öneriye açığız.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.
