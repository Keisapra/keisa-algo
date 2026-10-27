namamhs = input("Masukkan Nama :")
nilaialgo = int(input("Masukkan Nilai Algoritma :"))
nilaibasisdata = int(input("Masukkan Nilai Basis Data :"))
nilaiagama = int(input("Masukkan Nilai Agama :"))
nilaipancasila = int(input("Masukkan Nilai Pancasila :"))
nilaibahasainggris = int(input("Masukkan Nilai Bahasa Inggris :"))
nilaibahasaindonesia = int(input("Masukkan Nilai Bahasa Indonesia :"))
nilailogikainformatika = int(input("Masukkan Nilai Logika Informatika :"))

rata_rata = (nilaialgo + nilaibasisdata + nilaiagama + nilaipancasila + nilaibahasainggris + nilaibahasaindonesia + nilailogikainformatika) / 7
print(rata_rata)     

# penentuan lulus atau tidak
if rata_rata >=80 and rata_rata <=100:
    # kondisi jika terpenuhi
    #maka
    print("Nilai : A")
elif rata_rata >=70 and rata_rata<=80:
    print("Nilai: B")
elif rata_rata >=50 and rata_rata<=70:
    print("Nilai C")
elif rata_rata >=30 and rata_rata<=50:
    print("Nilai D")
elif rata_rata >=10 and rata_rata<=30:
    print("Nilai E")
else:
    # cukup menampilkan hasil
    # maka
    print("Nilai Lebih dari 100 atau dibawah 50")