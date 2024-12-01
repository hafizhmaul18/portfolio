def addition_to_string(num1, num2):
    # Konversi string ke integer
    int_num1 = int(num1)
    int_num2 = int(num2)
    
    # Lakukan penjumlahan
    result = str(int_num1 + int_num2)
    
    # Kembalikan hasil sebagai string
    return ','.join(result)

# Contoh penggunaan
print(addition_to_string("123", "456"))  # Output: "579"
print(addition_to_string("999", "1"))    # Output: "1000"
