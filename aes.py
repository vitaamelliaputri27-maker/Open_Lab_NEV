from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

print("--- PROGRAM AES-128 STANDARD (NON-FERNET) ---\n")

# ==========================================
# FUNGSI ENKRIPSI
# ==========================================
def aes_encrypt(pesan, kunci):
    # Pastikan kunci tepat 16 byte
    kunci_bytes = kunci.encode('utf-8')
    if len(kunci_bytes) != 16:
        raise ValueError(f"Kunci harus tepat 16 karakter! Kunci Anda: {len(kunci_bytes)} karakter.")
    
    # Buat cipher AES mode CBC
    cipher_encrypt = AES.new(kunci_bytes, AES.MODE_CBC)
    iv = cipher_encrypt.iv
    
    # Padding pesan agar kelipatan 16 byte
    padded_data = pad(pesan.encode('utf-8'), AES.block_size)
    ciphertext_bytes = cipher_encrypt.encrypt(padded_data)
    
    # Encode ke Base64
    ciphertext_base64 = base64.b64encode(ciphertext_bytes).decode('utf-8')
    iv_base64 = base64.b64encode(iv).decode('utf-8')
    
    return ciphertext_base64, iv_base64


# ==========================================
# FUNGSI DEKRIPSI
# ==========================================
def aes_decrypt(ciphertext_base64, kunci, iv_base64):
    kunci_bytes = kunci.encode('utf-8')
    if len(kunci_bytes) != 16:
        raise ValueError(f"Kunci harus tepat 16 karakter! Kunci Anda: {len(kunci_bytes)} karakter.")
    
    ciphertext_bytes = base64.b64decode(ciphertext_base64)
    iv = base64.b64decode(iv_base64)
    
    cipher_decrypt = AES.new(kunci_bytes, AES.MODE_CBC, iv=iv)
    decrypted_padded_bytes = cipher_decrypt.decrypt(ciphertext_bytes)
    pesan_terdekripsi = unpad(decrypted_padded_bytes, AES.block_size).decode('utf-8')
    
    return pesan_terdekripsi


# ==========================================
# PROGRAM UTAMA (INTERAKTIF)
# ==========================================
if __name__ == "__main__":
    print("Pilih mode:")
    print("  1. Enkripsi")
    print("  2. Dekripsi")
    pilihan = input("Masukkan pilihan (1/2): ").strip()
    
    if pilihan == "1":
        # ---- MODE ENKRIPSI ----
        print("\n--- MODE ENKRIPSI ---")
        pesan_rahasia = input("Masukkan pesan yang ingin dienkripsi: ")
        
        kunci = input("Masukkan kunci (harus tepat 16 karakter): ")
        
        try:
            ciphertext_base64, iv_base64 = aes_encrypt(pesan_rahasia, kunci)
            
            print(f"\n--- HASIL ENKRIPSI ---")
            print(f"Pesan Asli (Plaintext)      : {pesan_rahasia}")
            print(f"AES Encrypted Text (Base64) : {ciphertext_base64}")
            print(f"Secret Key (Plain Text)     : {kunci}")
            print(f"IV (Base64)                 : {iv_base64}")
            print("\n(Salin data di atas untuk keperluan dekripsi)")
            
        except ValueError as e:
            print(f"\n[ERROR] {e}")
    
    elif pilihan == "2":
        # ---- MODE DEKRIPSI ----
        print("\n--- MODE DEKRIPSI ---")
        ciphertext_base64 = input("Masukkan AES Encrypted Text (Base64): ").strip()
        kunci = input("Masukkan kunci (16 karakter): ").strip()
        iv_base64 = input("Masukkan IV (Base64): ").strip()
        
        try:
            pesan_terdekripsi = aes_decrypt(ciphertext_base64, kunci, iv_base64)
            print(f"\n--- HASIL DEKRIPSI ---")
            print(f"Pesan Terdekripsi : {pesan_terdekripsi}")
            
        except ValueError as e:
            print(f"\n[ERROR] {e}")
        except Exception as e:
            print(f"\n[ERROR] Gagal mendekripsi. Pastikan kunci, ciphertext, dan IV benar.")
            print(f"Detail: {e}")
    
    else:
        print("\n[ERROR] Pilihan tidak valid. Silakan jalankan program ulang dan pilih 1 atau 2.")
