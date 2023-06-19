#materi percabangan
#di python hanya ada 1 percabangan yaitu if saja
#if satu kondisi

nilai = int(input('Masukkan nilai: '))
if (nilai>0):
    print("Bilangan", nilai, "merupakan bilangan bilangan bulat")

#if dua kondisi
nilai = int(input('Masukkan nilai: '))
if (nilai>0):
    print("Bilangan", nilai, "merupakan bilangan bilangan positif")
else:
    print("Bilangan", nilai, "merupakan bilangan negatif")
    
#if tiga kondisi atau lebih
nilai = int(input('Masukkan nilai: '))
if (nilai>0):
    print("Bilangan", nilai, "merupakan bilangan bilangan positif")
elif (nilai<0):
    print("Bilangan", nilai, "merupakan bilangan negatif")
else:
    print("Bilangan", nilai, "merupakan bilangan nol")
    
