'''Soal: Buat sebuah fungsi bernama parse_and_sum yang menerima string angka yang dipisahkan oleh koma, 
misalnya "1,2,3,4,5", lalu mengonversi setiap angka menjadi integer, menjumlahkan semua angka tersebut, 
dan mengembalikan hasilnya dalam bentuk integer. Jika input kosong, kembalikan 0.'''

def parse_and_sum(number_string):
    if not number_string:
        return 0
    
    # Memisahkan string berdasarkan koma dan mengonversi ke integer
    numbers = [int(num) for num in number_string.split(",")]
    # Menjumlahkan semua angka
    return sum(numbers)

# Contoh penggunaan
print(parse_and_sum("1,2,3,4,5"))  # Output: 15
print(parse_and_sum(""))           # Output: 0