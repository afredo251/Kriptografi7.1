from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib
import base64

def generate_barcode(nomor_pengiriman, tanggal_kirim, kode_cabang):
    # Gabungkan nomor_pengiriman, tanggal_kirim, dan kode_cabang
    data = nomor_pengiriman + tanggal_kirim + kode_cabang
    
    # Enkripsi menggunakan AES 256 OCB
    key = hashlib.sha256(b"KunciRahasia").digest()
    cipher = AES.new(key, AES.MODE_OCB)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    
    # Gabungkan nonce, ciphertext, dan tag
    encrypted_data = nonce + ciphertext + tag
    
    # Encode data enkripsi menggunakan Base64
    encoded_data = base64.b64encode(encrypted_data).decode()
    
    return encoded_data

# Main program
nomor_pengiriman = input("Masukkan Nomor Pengiriman: ")
tanggal_kirim = input("Masukkan Tanggal Kirim: ")
kode_cabang = input("Masukkan Kode Cabang Distributor: ")

barcode = generate_barcode(nomor_pengiriman, tanggal_kirim, kode_cabang)
print("Barcode yang dihasilkan:")
print(barcode)