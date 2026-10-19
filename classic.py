# ==========================================
# 1. CAESAR CIPHER
# ==========================================
def encrypt_caesar(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted += char
    return encrypted

def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)


# ==========================================
# 2. VIGENERE CIPHER
# ==========================================
def encrypt_vigenere(text, key):
    encrypted = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Mencegah error jika kunci kosong
            if key_length == 0:
                shift = 0
            else:
                shift = ord(key[key_index % key_length]) - ord('a')
            encrypted += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            key_index += 1
        else:
            encrypted += char
    return encrypted

def decrypt_vigenere(text, key):
    decrypted = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            if key_length == 0:
                shift = 0
            else:
                shift = ord(key[key_index % key_length]) - ord('a')
            decrypted += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            key_index += 1
        else:
            decrypted += char
    return decrypted


# ==========================================
# SIMULASI INTERAKTIF (INPUT USER)
# ==========================================
if __name__ == "__main__":
    print("=== PROGRAM SIMULASI KRIPTOGRAFI KLASIK ===")
    
    # Input pesan asli dari user
    pesan_asli = input("Masukkan pesan (plaintext) yang ingin dikirim: ")
    print(f"\nPesan Asli: {pesan_asli}\n")
    
    # --- Simulasi 1: Caesar Cipher ---
    print("--- 1. Simulasi Caesar Cipher ---")
    try:
        kunci_caesar = int(input("Masukkan angka pergeseran kunci Caesar (contoh: 3): "))
    except ValueError:
        kunci_caesar = 3
        print("Input tidak valid, otomatis menggunakan angka 3.")
        
    cipher_c = encrypt_caesar(pesan_asli, kunci_caesar)
    print(f"Alice Mengirim (Ciphertext): {cipher_c}")
    plain_c = decrypt_caesar(cipher_c, kunci_caesar)
    print(f"Bob Menerima (Plaintext): {plain_c}\n")
    
    # --- Simulasi 2: Vigenère Cipher ---
    print("--- 2. Simulasi Vigenère Cipher ---")
    kunci_vigenere = input("Masukkan kata kunci (string) untuk Vigenère (contoh: KUNCI): ")
    if not kunci_vigenere:
        kunci_vigenere = "KUNCI"
        print("Kunci kosong, otomatis menggunakan 'KUNCI'.")
        
    cipher_v = encrypt_vigenere(pesan_asli, kunci_vigenere)
    print(f"Alice Mengirim (Ciphertext): {cipher_v}")
    plain_v = decrypt_vigenere(cipher_v, kunci_vigenere)
    print(f"Bob Menerima (Plaintext): {plain_v}")
