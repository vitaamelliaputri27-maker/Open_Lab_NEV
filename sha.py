import hashlib

print("--- 1. SIMULASI SHA-256 ---")
pesan_1 = "Belajar Kriptografi"
pesan_2 = "Belajar Kriptografi"  # Perhatikan huruf 'm' kecil di akhir

# Membuat objek hash SHA-256
hash_1 = hashlib.sha256(pesan_1.encode('utf-8')).hexdigest()
hash_2 = hashlib.sha256(pesan_2.encode('utf-8')).hexdigest()

print(f"Pesan 1     : {pesan_1}")
print(f"Hash SHA256 : {hash_1}\n")

print(f"Pesan 2     : {pesan_2} (berbeda 1 huruf kapital)")
print(f"Hash SHA256 : {hash_2}\n")