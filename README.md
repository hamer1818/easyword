# Wordlist Oluşturucu

Python ve PyQt6 kullanarak geliştirilmiş bir **Wordlist Oluşturma** uygulaması.

## Özellikler

- Kullanıcı dostu arayüz ile kolay kullanım
- İstenilen karakter uzunluğunda wordlist oluşturma
- Özel dosya adı belirleyebilme
- Otomatik `.txt` uzantısı ekleme
- Çoklu işlem desteği ile hızlı wordlist oluşturma
- Geliştirici bilgisi ve proje GitHub bağlantısı

## Gereksinimler

- Python 3.x
- PyQt6

## Kurulum

1. **Projeyi klonlayın** veya indirin:

   ```bash
   git clone https://github.com/hamer1818/easyword.git
   ```

2. **Sanal ortam oluşturun** ve aktif edin:
    1. Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    2. Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. **Gerekli kütüphaneleri yükleyin**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Uygulamayı çalıştırın**:
    ```bash
    python main.py
    ```

5. **Kullanın**:
    - İstenilen karakter uzunluğunu girin
    - Dosya adını belirleyin
    - Oluştur'a tıklayın
    - İşlem tamamlandığında `Wordlist oluşturuldu!` uyarısını alacaksınız

## Terminal Kullanımı

Alternatif olarak, terminal üzerinden de wordlist oluşturabilirsiniz:

1. **Terminal'i açın**:

    ```bash
    python terminal.py
    ```

2. **Adımları takip edin**:
    - İstenilen karakter uzunluğunu girin
    - Dosya adını belirleyin
    - Karakter setini seçin
    - İşlem tamamlandığında, `Wordlist oluşturuldu!` uyarısını alacaksınız
