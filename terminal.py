import sys
import time
import itertools
import os
import multiprocessing
from tqdm import tqdm

def generate_wordlist_chunk(args):
    """Wordlist'in bir parçasını oluşturan fonksiyon"""
    characters, length, start_idx, chunk_size, output_file = args
    
    # Geçici dosya oluştur
    temp_file = f"{output_file}.part{start_idx}"
    count = 0
    
    with open(temp_file, "w") as file:
        # İlgili parçanın kombinasyonlarını hesapla
        total_combinations = len(characters) ** length
        
        # itertools.product'ı direkt kullanmak yerine, belirli bir aralıktaki kombinasyonları alıyoruz
        for i, combination in enumerate(itertools.product(characters, repeat=length)):
            if i >= start_idx and i < start_idx + chunk_size:
                file.write(''.join(combination) + "\n")
                count += 1
            elif i >= start_idx + chunk_size:
                break
    
    return temp_file, count

def merge_files(temp_files, output_file):
    """Geçici dosyaları birleştiren fonksiyon"""
    with open(output_file, "wb") as outfile:
        for temp_file in temp_files:
            with open(temp_file, "rb") as infile:
                outfile.write(infile.read())
            # İşlem tamamlandıktan sonra geçici dosyayı sil
            os.remove(temp_file)

def calculate_file_size(characters, length):
    """Oluşturulacak dosyanın tahmini boyutunu hesaplar"""
    # Her satır length karakter + newline (\n)
    line_size = length + 1
    total_combinations = len(characters) ** length
    estimated_size_bytes = total_combinations * line_size
    
    # Boyutu daha anlaşılır birimde göster
    if estimated_size_bytes < 1024:
        return f"{estimated_size_bytes} B"
    elif estimated_size_bytes < 1024 * 1024:
        return f"{estimated_size_bytes/1024:.2f} KB"
    elif estimated_size_bytes < 1024 * 1024 * 1024:
        return f"{estimated_size_bytes/(1024*1024):.2f} MB"
    else:
        return f"{estimated_size_bytes/(1024*1024*1024):.2f} GB"

def main():
    print("=== Wordlist Oluşturucu ===")
    print("Hamza ORTATEPE tarafından geliştirildi")
    print("https://github.com/hamer1818/easyword")
    print("==========================\n")
    
    try:
        # Kullanıcı girdilerini al
        while True:
            try:
                length = int(input("Hane sayısını girin (1-10): "))
                if 1 <= length <= 10:
                    break
                else:
                    print("Lütfen 1 ile 10 arasında bir değer girin.")
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
        
        name = input("Wordlist ismini yazın: ")
        if not name.endswith('.txt'):
            name += '.txt'
            
        # Karakter seti seçenekleri
        print("\nKarakter seti seçin:")
        print("1. Sadece küçük harfler (a-z)")
        print("2. Küçük ve büyük harfler (a-z, A-Z)")
        print("3. Alfanümerik (a-z, A-Z, 0-9)")
        print("4. Alfanümerik + özel karakterler (a-z, A-Z, 0-9, !@#$%^&*)")
        print("5. Özel karakter seti girin")
        
        char_choice = input("Seçiminiz (1-5): ")
        
        if char_choice == "1":
            characters = "abcdefghijklmnopqrstuvwxyz"
        elif char_choice == "2":
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif char_choice == "3":
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        elif char_choice == "4":
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        elif char_choice == "5":
            characters = input("Kullanılacak karakterleri girin: ")
        else:
            print("Geçersiz seçim, varsayılan karakter seti kullanılacak.")
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        
        # Dosya boyutu uyarısı
        estimated_size = calculate_file_size(characters, length)
        total_combinations = len(characters) ** length
        
        print(f"\nTahmini dosya boyutu: {estimated_size}")
        print(f"Toplam oluşturulacak kombinasyon sayısı: {total_combinations:,}")
        
        if total_combinations > 100000000:  # 100 milyon
            confirm = input("Bu işlem çok büyük bir dosya oluşturacak ve uzun sürebilir. Devam etmek istiyor musunuz? (e/h): ")
            if confirm.lower() != 'e':
                print("İşlem iptal edildi.")
                return
        
        # Çoklu işlem için CPU sayısı belirleme
        num_cores = min(multiprocessing.cpu_count(), 8)  # Maksimum 8 çekirdek kullan
        
        print(f"\nWordlist oluşturuluyor, lütfen bekleyin...")
        print(f"{num_cores} işlemci çekirdeği kullanılıyor.")
        
        start_time = time.perf_counter()
        
        # Paralel işleme için kombinasyonları bölme
        chunk_size = max(1, total_combinations // (num_cores * 10))  # Her çekirdek için 10 adet parça
        
        # Çalıştırılacak görevleri oluştur
        tasks = []
        for i in range(0, total_combinations, chunk_size):
            end_idx = min(i + chunk_size, total_combinations)
            tasks.append((characters, length, i, end_idx - i, name))
        
        # İlerleme çubuğu için tqdm kullan
        temp_files = []
        total_written = 0
        
        with multiprocessing.Pool(processes=num_cores) as pool:
            for temp_file, count in tqdm(pool.imap_unordered(generate_wordlist_chunk, tasks), 
                                        total=len(tasks), 
                                        desc="İşleniyor", 
                                        unit="parça"):
                temp_files.append(temp_file)
                total_written += count
        
        print("\nDosyalar birleştiriliyor...")
        merge_files(temp_files, name)
        
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        
        print(f"\nİşlem tamamlandı!")
        print(f"Süre: {elapsed_time:.2f} saniye")
        print(f"Toplam yazılan kombinasyon: {total_written:,}")
        print(f"Dosya: {os.path.abspath(name)}")
        
    except KeyboardInterrupt:
        print("\nİşlem kullanıcı tarafından iptal edildi.")
    except Exception as e:
        print(f"\nHata oluştu: {e}")

if __name__ == "__main__":
    main()
