# import library pandas untuk membaca file csv
from ast import Try
import pandas as pd
# import library levensteinch distance
from nltk.metrics.distance import edit_distance

# import library KBBI
from kbbi import KBBI

read_parameter = pd.read_csv('data.csv')
parameter = read_parameter['a'].values.tolist()


def cek_kata(kata):
    if(len(kata.split()) > 1):
        print("Silahkan Masukkan 1 kata")
    else:
        result = []
        rekomendasi_kata = []

        for p in parameter:

            leven = edit_distance(p, kata)
            presentase_kesalahan = tingkat_kesalahan(leven, len(p))

            if(presentase_kesalahan == 0):
                result.append(p)

            elif(presentase_kesalahan > 0 and presentase_kesalahan < 35):
                rekomendasi_kata.append(p)
        print("")
        print("============ HASIL KOREKSI ============")

        if(len(result) > 0):
            print("")
            print(
                "Kata Yang anda maksud terdapat dalam kamus yakni : ", result[0])
            print("")

        elif(len(result) == 0 and len(rekomendasi_kata) > 0):
            print("")
            print("Kata yang anda maksud mendekati kata-kata berikut ini : ")
            no = 0
            for w in rekomendasi_kata:
                no += 1
                print(no, ") " + w)
            print("")

        else:
            try:
                suggest = KBBI(kata)
                print("")
                print("Mohon maaf kata yang anda masukkan tidak terdapat didalam kamus !!!, berikut suggest kata yang anda masukkan berdasarkan KBBI : ")
                print("")
                print(suggest.__str__(contoh=False, terkait=False))
                print("")
            except:
                print("Tidak terdapat suggest pada kata : ", kata)


def tingkat_kesalahan(leven, panjang_kata):
    tingkat_kesalahan = leven / panjang_kata * 100
    return round(tingkat_kesalahan)


print("")
print("----- APLIKASI SPEEL CHECKER MENGGUNAKAN LEVENSTEINCH DISTANCE -------")
print("                     Developed By Nofrisdan Sitopu                     ")
print("")
kata = str(input("Masukkan Satu Kata : "))
cek_kata(kata)
