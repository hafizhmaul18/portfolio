#Soal: Buat sebuah fungsi fizz_buzz yang menerima satu parameter n. Fungsi ini mencetak angka dari 1 hingga n. 
# Untuk setiap angka yang merupakan kelipatan 3, cetak "Fizz" sebagai gantinya. 
# Untuk setiap angka yang merupakan kelipatan 5, cetak "Buzz" sebagai gantinya. 
# Jika angka merupakan kelipatan 3 dan 5, cetak "FizzBuzz".

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Contoh penggunaan
fizz_buzz(15)
