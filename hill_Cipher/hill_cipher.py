import numpy as np

# Fungsi bantu untuk konversi huruf ke angka dan sebaliknya
def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

def numbers_to_text(numbers):
    return ''.join([chr((num % 26) + ord('A')) for num in numbers])

# Fungsi enkripsi Hill Cipher
def hill_encrypt(plaintext, key_matrix):
    plaintext_numbers = text_to_numbers(plaintext)
    n = key_matrix.shape[0]

    # Padding jika panjang plaintext tidak habis dibagi ukuran matriks
    while len(plaintext_numbers) % n != 0:
        plaintext_numbers.append(ord('X') - ord('A'))

    ciphertext_numbers = []
    for i in range(0, len(plaintext_numbers), n):
        block = np.array(plaintext_numbers[i:i+n])
        result = np.dot(key_matrix, block) % 26
        ciphertext_numbers.extend(result)

    return numbers_to_text(ciphertext_numbers)

# Fungsi mencari inverse matriks modulo 26 (untuk dekripsi)
def mod_inverse_matrix(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix))) % modulus
    det_inv = pow(det, -1, modulus)
    matrix_mod_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)
    ) % modulus
    return matrix_mod_inv.astype(int)

# Fungsi dekripsi Hill Cipher
def hill_decrypt(ciphertext, key_matrix):
    ciphertext_numbers = text_to_numbers(ciphertext)
    n = key_matrix.shape[0]

    inverse_key = mod_inverse_matrix(key_matrix, 26)

    plaintext_numbers = []
    for i in range(0, len(ciphertext_numbers), n):
        block = np.array(ciphertext_numbers[i:i+n])
        result = np.dot(inverse_key, block) % 26
        plaintext_numbers.extend(result)

    return numbers_to_text(plaintext_numbers)
