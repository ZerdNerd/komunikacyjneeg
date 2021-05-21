import random
import sys

miejsca_w_ikarusie_260_04 = 22
miejsca_w_ikarusie_260_04_szczyt = 110
miejsca_w_ikarusie_280_11 = 29
miejsca_w_ikarusie_280_11_szczyt = 143
miejsca_w_ikarusie_280_26 = 35
miejsca_w_ikarusie_280_26_szczyt = 160
miejsca_w_ikarusie_280_46 = 35
miejsca_w_ikarusie_280_46_szczyt = 160
miejsca_w_ikarusie_280_57 = 35
miejsca_w_ikarusie_280_57_szczyt = 160
miejsca_w_zemunie = 47
miejsca_w_zemunie_szczyt = 145
miejsca_w_peerce = 35
miejsca_w_peerce_szczyt = 109
miejsca_w_peerce_d = 51
miejsca_w_peerce_d_szczyt = 51
miejsca_w_L11 = 40
miejsca_w_L11_szczyt = 90
miejsca_w_migu = 30
miejsca_w_migu_szczyt = 100
miejsca_w_h9 = 51
miejsca_w_h9_szczyt = 51

liczba_miejsc_w_autobusie = 0

liczba_pasazerow_temp = 0

liczba_pasazerow_total = 0

popularnosc_firmy = float(input("Podaj popularność firmy jako ułamek dziesiętny. Przykład: 50pp to 0,5. "))

typ_autobusu = input("Podaj typ autobusu obsługującego linię.\nDostępne typy to: IK260.04, IK280.11, IK280.26, IK280.46, IK280.57, 160P, PR110, PR110D, L11, M11, H9-21.\n")

czy_szczyt = input("Czy kurs odbywa się w szczycie komunikacyjnym? Odpowiedz tak lub nie. ")


if czy_szczyt == "nie":
    if typ_autobusu == "IK260.04":
        liczba_miejsc_w_autobusie = miejsca_w_ikarusie_260_04
    elif typ_autobusu == "IK280.11":
        liczba_miejsc_w_autobusie = miejsca_w_ikarusie_280_11
    elif typ_autobusu == "IK280.26":
        liczba_miejsc_w_autobusie = miejsca_w_ikarusie_280_26
    elif typ_autobusu == "IK280.46":
        liczba_miejsc_w_autobusie = miejsca_w_ikarusie_280_46
    elif typ_autobusu == "IK280.57":
        liczba_miejsc_w_autobusie = miejsca_w_ikarusie_280_57
    elif typ_autobusu == "160P":
        liczba_miejsc_w_autobusie = miejsca_w_zemunie
    elif typ_autobusu == "PR110":
        liczba_miejsc_w_autobusie = miejsca_w_peerce
    elif typ_autobusu == "PR110D":
        liczba_miejsc_w_autobusie = miejsca_w_peerce_d
    elif typ_autobusu == "L11":
        liczba_miejsc_w_autobusie = miejsca_w_L11
    elif typ_autobusu == "M11":
        liczba_miejsc_w_autobusie = miejsca_w_migu
    elif typ_autobusu == "H9-21":
        liczba_miejsc_w_autobusie = miejsca_w_h9
    else:
        print("Co by pan zrobił, gdyby się pan dowiedział, że pańska siorka opierdala kiełbachy kosmitom?")
        sys.exit()
if czy_szczyt == "tak":
    if typ_autobusu == "IK260.04":
        liczba_miejsc_w_autobusie = miejsca_w_ikarusie_260_04_szczyt
    elif typ_autobusu == "IK280.11":
        liczba_miejsc_w_autobusie = miejsca_w_ikarusie_280_11_szczyt
    elif typ_autobusu == "IK280.26":
        liczba_miejsc_w_autobusie = miejsca_w_ikarusie_280_26_szczyt
    elif typ_autobusu == "IK280.46":
        liczba_miejsc_w_autobusie = miejsca_w_ikarusie_280_46_szczyt
    elif typ_autobusu == "IK280.57":
        liczba_miejsc_w_autobusie = miejsca_w_ikarusie_280_57_szczyt
    elif typ_autobusu == "160P":
        liczba_miejsc_w_autobusie = miejsca_w_zemunie_szczyt
    elif typ_autobusu == "PR110":
        liczba_miejsc_w_autobusie = miejsca_w_peerce_szczyt
    elif typ_autobusu == "PR110D":
        liczba_miejsc_w_autobusie = miejsca_w_peerce_d_szczyt
    elif typ_autobusu == "L11":
        liczba_miejsc_w_autobusie = miejsca_w_L11_szczyt
    elif typ_autobusu == "M11":
        liczba_miejsc_w_autobusie = miejsca_w_migu_szczyt
    elif typ_autobusu == "H9-21":
        liczba_miejsc_w_autobusie = miejsca_w_h9_szczyt
    else:
        print("Co by pan zrobił, gdyby się pan dowiedział, że pańska siorka opierdala kiełbachy kosmitom?")
        sys.exit()

if czy_szczyt != "tak":
    if czy_szczyt != "nie":
        print("Tępy chuju! Nie wypełniłeś prawidłowo pola! Zapierdalaj do Orzeła i popraw błędy!")
        sys.exit()


liczba_przystankow = int(input("Podaj liczbę przystanków, jakie ma linia w jednym kierunku. "))

liczba_przystankow_dynamo = 0

for n in range (1, liczba_przystankow):
    var1 = "przystanek_"
    val1 = {n}
    dict1 = {var1:val1}
    var2 = "popyt_przystanek_"
    val2 = {n}
    dict2 = {var2:val2}
    
for n in range (1, liczba_przystankow):
    dict1[n] = round(float(input("Podaj liczbę potencjalnych pasażerów w zasięgu przystanku %s. " % n)))
    dict2[n] = dict1[n]*popularnosc_firmy
    print("Pop na przystanku %s to:" % n, dict2[n])

if popularnosc_firmy == 0.0:
    print("Serio?")
    sys.exit()

if 0 < popularnosc_firmy < 0.1:
    for n in range (1, liczba_przystankow):
        var3 = "pasazerowie_przystanek_"
        val3 = {n}
        dict3 = {var3:val3}
        var4 = "temp_pasazerowie_przystanek_"
        val4 = {n}
        dict4 = {var4:val4}
        random.seed(a=random.random(), version=2)
        dict4[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1])
        var5 = "zaokraglacz_pasazerowie_przystanek_"
        val5 = {n}
        dict5 = {var5:val5}
        var6 = "obliczacz_pasazerowie_przystanek_"
        val6 = {n}
        dict6 = {var6:val6}
        dict6[n] = dict4[n]*liczba_miejsc_w_autobusie
        dict5[n] = round(dict6[n])
        var55 = "check_przystanku_"
        val55 = n
        dict55 = {var55:val55}
        if czy_szczyt == "tak":
            if dict1[n] < 300:
                dict5[n] = round(dict5[n]/3)
            if dict1[n] >= 300:
                dict5[n] = round(dict5[n]/1.5)
        if czy_szczyt == "nie":
            if dict1[n] < 200:
                dict5[n] = round(dict5[n]/2)
        dict3[n] = dict5[n]
        liczba_pasazerow_total = liczba_pasazerow_total + dict3[n]
        random.seed(a=random.random(), version=2)
        if n < 3:
            liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        if n > 2:
            var7 = "czy_wysiadaja_przystanek_"
            val7 = {n}
            dict7 = {var7:val7}
            dict7[n] = random.choice([0, 1]) #0 - nie wysiadają, 1 - wysiadają
            if dict7[n] == 1:
                var8 = "wysiadajacy_na_przystanku_"
                val8 = {n}
                dict8 = {var8:val8}
                var88 = "wysiadajacy_na_przystanku_temp_"
                val88 = {n}
                dict88 = {var88:val88}
                if 2 < n < 6:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 5 < n < 11:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 10 < n < 16:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 15 < n:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                print("Na przystanku %s wysiadło" % n, dict88[n], "pasażerów.")
                liczba_pasazerow_temp = dict8[n]+dict3[n]
            if dict7[n] == 0:
                liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        print("Na przystanku %s na ten kurs oczekiwało" % n, dict3[n], "pasażerów. W autobusie znajdowało się", liczba_pasazerow_temp, "pasażerów.")

if 0.1 < popularnosc_firmy < 0.19:
    for n in range (1, liczba_przystankow):
        var3 = "pasazerowie_przystanek_"
        val3 = {n}
        dict3 = {var3:val3}
        var4 = "temp_pasazerowie_przystanek_"
        val4 = {n}
        dict4 = {var4:val4}
        random.seed(a=random.random(), version=2)
        dict4[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2])
        var5 = "zaokraglacz_pasazerowie_przystanek_"
        val5 = {n}
        dict5 = {var5:val5}
        var6 = "obliczacz_pasazerowie_przystanek_"
        val6 = {n}
        dict6 = {var6:val6}
        dict6[n] = dict4[n]*liczba_miejsc_w_autobusie
        dict5[n] = round(dict6[n])
        var55 = "check_przystanku_"
        val55 = n
        dict55 = {var55:val55}
        if czy_szczyt == "tak":
            if dict1[n] < 300:
                dict5[n] = round(dict5[n]/3)
            if dict1[n] >= 300:
                dict5[n] = round(dict5[n]/1.5)
        if czy_szczyt == "nie":
            if dict1[n] < 200:
                dict5[n] = round(dict5[n]/2)
        dict3[n] = dict5[n]
        liczba_pasazerow_total = liczba_pasazerow_total + dict3[n]
        random.seed(a=random.random(), version=2)
        if n < 3:
            liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        if n > 2:
            var7 = "czy_wysiadaja_przystanek_"
            val7 = {n}
            dict7 = {var7:val7}
            dict7[n] = random.choice([0, 1]) #0 - nie wysiadają, 1 - wysiadają
            if dict7[n] == 1:
                var8 = "wysiadajacy_na_przystanku_"
                val8 = {n}
                dict8 = {var8:val8}
                var88 = "wysiadajacy_na_przystanku_temp_"
                val88 = {n}
                dict88 = {var88:val88}
                if 2 < n < 6:
                    dict88[n] = random.choice([0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 5 < n < 11:
                    dict88[n] = random.choice([0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 10 < n < 16:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 15 < n:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                print("Na przystanku %s wysiadło" % n, dict88[n], "pasażerów.")
                liczba_pasazerow_temp = dict8[n]+dict3[n]
            if dict7[n] == 0:
                liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        print("Na przystanku %s na ten kurs oczekiwało" % n, dict3[n], "pasażerów. W autobusie znajdowało się", liczba_pasazerow_temp, "pasażerów.")

if 0.2 < popularnosc_firmy < 0.29:
    for n in range (1, liczba_przystankow):
        var3 = "pasazerowie_przystanek_"
        val3 = {n}
        dict3 = {var3:val3}
        var4 = "temp_pasazerowie_przystanek_"
        val4 = {n}
        dict4 = {var4:val4}
        random.seed(a=random.random(), version=2)
        dict4[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3])
        var5 = "zaokraglacz_pasazerowie_przystanek_"
        val5 = {n}
        dict5 = {var5:val5}
        var6 = "obliczacz_pasazerowie_przystanek_"
        val6 = {n}
        dict6 = {var6:val6}
        dict6[n] = dict4[n]*liczba_miejsc_w_autobusie
        dict5[n] = round(dict6[n])
        var55 = "check_przystanku_"
        val55 = n
        dict55 = {var55:val55}
        if czy_szczyt == "tak":
            if dict1[n] < 300:
                dict5[n] = round(dict5[n]/3)
            if dict1[n] >= 300:
                dict5[n] = round(dict5[n]/1.5)
        if czy_szczyt == "nie":
            if dict1[n] < 200:
                dict5[n] = round(dict5[n]/2)
        dict3[n] = dict5[n]
        liczba_pasazerow_total = liczba_pasazerow_total + dict3[n]
        random.seed(a=random.random(), version=2)
        if n < 3:
            liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        if n > 2:
            var7 = "czy_wysiadaja_przystanek_"
            val7 = {n}
            dict7 = {var7:val7}
            dict7[n] = random.choice([0, 1]) #0 - nie wysiadają, 1 - wysiadają
            if dict7[n] == 1:
                var8 = "wysiadajacy_na_przystanku_"
                val8 = {n}
                dict8 = {var8:val8}
                var88 = "wysiadajacy_na_przystanku_temp_"
                val88 = {n}
                dict88 = {var88:val88}
                if 2 < n < 6:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 5 < n < 11:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 10 < n < 16:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 15 < n:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                print("Na przystanku %s wysiadło" % n, dict88[n], "pasażerów.")
                liczba_pasazerow_temp = dict8[n]+dict3[n]
            if dict7[n] == 0:
                liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        print("Na przystanku %s na ten kurs oczekiwało" % n, dict3[n], "pasażerów. W autobusie znajdowało się", liczba_pasazerow_temp, "pasażerów.")

if 0.3 < popularnosc_firmy < 0.39:
    for n in range (1, liczba_przystankow):
        var3 = "pasazerowie_przystanek_"
        val3 = {n}
        dict3 = {var3:val3}
        var4 = "temp_pasazerowie_przystanek_"
        val4 = {n}
        dict4 = {var4:val4}
        random.seed(a=random.random(), version=2)
        dict4[n] = random.choice([0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4])
        var5 = "zaokraglacz_pasazerowie_przystanek_"
        val5 = {n}
        dict5 = {var5:val5}
        var6 = "obliczacz_pasazerowie_przystanek_"
        val6 = {n}
        dict6 = {var6:val6}
        dict6[n] = dict4[n]*liczba_miejsc_w_autobusie
        dict5[n] = round(dict6[n])
        var55 = "check_przystanku_"
        val55 = n
        dict55 = {var55:val55}
        if czy_szczyt == "tak":
            if dict1[n] < 300:
                dict5[n] = round(dict5[n]/3)
            if dict1[n] >= 300:
                dict5[n] = round(dict5[n]/1.5)
        if czy_szczyt == "nie":
            if dict1[n] < 200:
                dict5[n] = round(dict5[n]/2)
        dict3[n] = dict5[n]
        liczba_pasazerow_total = liczba_pasazerow_total + dict3[n]
        random.seed(a=random.random(), version=2)
        if n < 3:
            liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        if n > 2:
            var7 = "czy_wysiadaja_przystanek_"
            val7 = {n}
            dict7 = {var7:val7}
            dict7[n] = random.choice([0, 1]) #0 - nie wysiadają, 1 - wysiadają
            if dict7[n] == 1:
                var8 = "wysiadajacy_na_przystanku_"
                val8 = {n}
                dict8 = {var8:val8}
                var88 = "wysiadajacy_na_przystanku_temp_"
                val88 = {n}
                dict88 = {var88:val88}
                if 2 < n < 6:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 5 < n < 11:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 10 < n < 16:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 15 < n:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                print("Na przystanku %s wysiadło" % n, dict88[n], "pasażerów.")
                liczba_pasazerow_temp = dict8[n]+dict3[n]
            if dict7[n] == 0:
                liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        print("Na przystanku %s na ten kurs oczekiwało" % n, dict3[n], "pasażerów. W autobusie znajdowało się", liczba_pasazerow_temp, "pasażerów.")

if 0.4 < popularnosc_firmy < 0.49:
    for n in range (1, liczba_przystankow):
        var3 = "pasazerowie_przystanek_"
        val3 = {n}
        dict3 = {var3:val3}
        var4 = "temp_pasazerowie_przystanek_"
        val4 = {n}
        dict4 = {var4:val4}
        random.seed(a=random.random(), version=2)
        dict4[n] = random.choice([0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5])
        var5 = "zaokraglacz_pasazerowie_przystanek_"
        val5 = {n}
        dict5 = {var5:val5}
        var6 = "obliczacz_pasazerowie_przystanek_"
        val6 = {n}
        dict6 = {var6:val6}
        dict6[n] = dict4[n]*liczba_miejsc_w_autobusie
        dict5[n] = round(dict6[n])
        var55 = "check_przystanku_"
        val55 = n
        dict55 = {var55:val55}
        if czy_szczyt == "tak":
            if dict1[n] < 300:
                dict5[n] = round(dict5[n]/3)
            if dict1[n] >= 300:
                dict5[n] = round(dict5[n]/1.5)
        if czy_szczyt == "nie":
            if dict1[n] < 200:
                dict5[n] = round(dict5[n]/2)
        dict3[n] = dict5[n]
        liczba_pasazerow_total = liczba_pasazerow_total + dict3[n]
        random.seed(a=random.random(), version=2)
        if n < 3:
            liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        if n > 2:
            var7 = "czy_wysiadaja_przystanek_"
            val7 = {n}
            dict7 = {var7:val7}
            dict7[n] = random.choice([0, 1]) #0 - nie wysiadają, 1 - wysiadają
            if dict7[n] == 1:
                var8 = "wysiadajacy_na_przystanku_"
                val8 = {n}
                dict8 = {var8:val8}
                var88 = "wysiadajacy_na_przystanku_temp_"
                val88 = {n}
                dict88 = {var88:val88}
                if 2 < n < 6:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 5 < n < 11:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 10 < n < 16:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 15 < n:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                print("Na przystanku %s wysiadło" % n, dict88[n], "pasażerów.")
                liczba_pasazerow_temp = dict8[n]+dict3[n]
            if dict7[n] == 0:
                liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        print("Na przystanku %s na ten kurs oczekiwało" % n, dict3[n], "pasażerów. W autobusie znajdowało się", liczba_pasazerow_temp, "pasażerów.")

if 0.5 < popularnosc_firmy < 0.59:
    for n in range (1, liczba_przystankow):
        var3 = "pasazerowie_przystanek_"
        val3 = {n}
        dict3 = {var3:val3}
        var4 = "temp_pasazerowie_przystanek_"
        val4 = {n}
        dict4 = {var4:val4}
        random.seed(a=random.random(), version=2)
        dict4[n] = random.choice([0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6])
        var5 = "zaokraglacz_pasazerowie_przystanek_"
        val5 = {n}
        dict5 = {var5:val5}
        var6 = "obliczacz_pasazerowie_przystanek_"
        val6 = {n}
        dict6 = {var6:val6}
        dict6[n] = dict4[n]*liczba_miejsc_w_autobusie
        dict5[n] = round(dict6[n])
        var55 = "check_przystanku_"
        val55 = n
        dict55 = {var55:val55}
        if czy_szczyt == "tak":
            if dict1[n] < 300:
                dict5[n] = round(dict5[n]/3)
            if dict1[n] >= 300:
                dict5[n] = round(dict5[n]/2)
        if czy_szczyt == "nie":
            if dict1[n] < 200:
                dict5[n] = round(dict5[n]/2)
        dict3[n] = dict5[n]
        liczba_pasazerow_total = liczba_pasazerow_total + dict3[n]
        random.seed(a=random.random(), version=2)
        if n < 3:
            liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        if n > 2:
            var7 = "czy_wysiadaja_przystanek_"
            val7 = {n}
            dict7 = {var7:val7}
            dict7[n] = random.choice([0, 1]) #0 - nie wysiadają, 1 - wysiadają
            if dict7[n] == 1:
                var8 = "wysiadajacy_na_przystanku_"
                val8 = {n}
                dict8 = {var8:val8}
                var88 = "wysiadajacy_na_przystanku_temp_"
                val88 = {n}
                dict88 = {var88:val88}
                if 2 < n < 6:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 5 < n < 11:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 10 < n < 16:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 15 < n:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                print("Na przystanku %s wysiadło" % n, dict88[n], "pasażerów.")
                liczba_pasazerow_temp = dict8[n]+dict3[n]
            if dict7[n] == 0:
                liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        
        print("Na przystanku %s na ten kurs oczekiwało" % n, dict3[n], "pasażerów. W autobusie znajdowało się", liczba_pasazerow_temp, "pasażerów.")

if 0.6 < popularnosc_firmy < 0.69:
    for n in range (1, liczba_przystankow):
        var3 = "pasazerowie_przystanek_"
        val3 = {n}
        dict3 = {var3:val3}
        var4 = "temp_pasazerowie_przystanek_"
        val4 = {n}
        dict4 = {var4:val4}
        random.seed(a=random.random(), version=2)
        dict4[n] = random.choice([0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7])
        var5 = "zaokraglacz_pasazerowie_przystanek_"
        val5 = {n}
        dict5 = {var5:val5}
        var6 = "obliczacz_pasazerowie_przystanek_"
        val6 = {n}
        dict6 = {var6:val6}
        dict6[n] = dict4[n]*liczba_miejsc_w_autobusie
        dict5[n] = round(dict6[n])
        var55 = "check_przystanku_"
        val55 = n
        dict55 = {var55:val55}
        if czy_szczyt == "tak":
            if dict1[n] < 300:
                dict5[n] = round(dict5[n]/3)
            if dict1[n] >= 300:
                dict5[n] = round(dict5[n]/1.5)
        if czy_szczyt == "nie":
            if dict1[n] < 200:
                dict5[n] = round(dict5[n]/2)
        dict3[n] = dict5[n]
        liczba_pasazerow_total = liczba_pasazerow_total + dict3[n]
        random.seed(a=random.random(), version=2)
        if n < 3:
            liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        if n > 2:
            var7 = "czy_wysiadaja_przystanek_"
            val7 = {n}
            dict7 = {var7:val7}
            dict7[n] = random.choice([0, 1]) #0 - nie wysiadają, 1 - wysiadają
            if dict7[n] == 1:
                var8 = "wysiadajacy_na_przystanku_"
                val8 = {n}
                dict8 = {var8:val8}
                var88 = "wysiadajacy_na_przystanku_temp_"
                val88 = {n}
                dict88 = {var88:val88}
                if 2 < n < 6:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 5 < n < 11:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 10 < n < 16:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 15 < n:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                print("Na przystanku %s wysiadło" % n, dict88[n], "pasażerów.")
                liczba_pasazerow_temp = dict8[n]+dict3[n]
            if dict7[n] == 0:
                liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        print("Na przystanku %s na ten kurs oczekiwało" % n, dict3[n], "pasażerów. W autobusie znajdowało się", liczba_pasazerow_temp, "pasażerów.")

if 0.7 < popularnosc_firmy < 0.79:
    for n in range (1, liczba_przystankow):
        var3 = "pasazerowie_przystanek_"
        val3 = {n}
        dict3 = {var3:val3}
        var4 = "temp_pasazerowie_przystanek_"
        val4 = {n}
        dict4 = {var4:val4}
        random.seed(a=random.random(), version=2)
        dict4[n] = random.choice([0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8])
        var5 = "zaokraglacz_pasazerowie_przystanek_"
        val5 = {n}
        dict5 = {var5:val5}
        var6 = "obliczacz_pasazerowie_przystanek_"
        val6 = {n}
        dict6 = {var6:val6}
        dict6[n] = dict4[n]*liczba_miejsc_w_autobusie
        dict5[n] = round(dict6[n])
        var55 = "check_przystanku_"
        val55 = n
        dict55 = {var55:val55}
        if czy_szczyt == "tak":
            if dict1[n] < 300:
                dict5[n] = round(dict5[n]/3)
            if dict1[n] >= 300:
                dict5[n] = round(dict5[n]/1.5)
        if czy_szczyt == "nie":
            if dict1[n] < 200:
                dict5[n] = round(dict5[n]/2)
        dict3[n] = dict5[n]
        liczba_pasazerow_total = liczba_pasazerow_total + dict3[n]
        random.seed(a=random.random(), version=2)
        if n < 3:
            liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        if n > 2:
            var7 = "czy_wysiadaja_przystanek_"
            val7 = {n}
            dict7 = {var7:val7}
            dict7[n] = random.choice([0, 1]) #0 - nie wysiadają, 1 - wysiadają
            if dict7[n] == 1:
                var8 = "wysiadajacy_na_przystanku_"
                val8 = {n}
                dict8 = {var8:val8}
                var88 = "wysiadajacy_na_przystanku_temp_"
                val88 = {n}
                dict88 = {var88:val88}
                if 2 < n < 6:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 5 < n < 11:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 10 < n < 16:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 15 < n:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                print("Na przystanku %s wysiadło" % n, dict88[n], "pasażerów.")
                liczba_pasazerow_temp = dict8[n]+dict3[n]
            if dict7[n] == 0:
                liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        print("Na przystanku %s na ten kurs oczekiwało" % n, dict3[n], "pasażerów. W autobusie znajdowało się", liczba_pasazerow_temp, "pasażerów.")

if 0.8 < popularnosc_firmy < 0.89:
    for n in range (1, liczba_przystankow):
        var3 = "pasazerowie_przystanek_"
        val3 = {n}
        dict3 = {var3:val3}
        var4 = "temp_pasazerowie_przystanek_"
        val4 = {n}
        dict4 = {var4:val4}
        random.seed(a=random.random(), version=2)
        dict4[n] = random.choice([0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9])
        var5 = "zaokraglacz_pasazerowie_przystanek_"
        val5 = {n}
        dict5 = {var5:val5}
        var6 = "obliczacz_pasazerowie_przystanek_"
        val6 = {n}
        dict6 = {var6:val6}
        dict6[n] = dict4[n]*liczba_miejsc_w_autobusie
        dict5[n] = round(dict6[n])
        var55 = "check_przystanku_"
        val55 = n
        dict55 = {var55:val55}
        if czy_szczyt == "tak":
            if dict1[n] < 300:
                dict5[n] = round(dict5[n]/3)
            if dict1[n] >= 300:
                dict5[n] = round(dict5[n]/1.5)
        if czy_szczyt == "nie":
            if dict1[n] < 200:
                dict5[n] = round(dict5[n]/2)
        dict3[n] = dict5[n]
        liczba_pasazerow_total = liczba_pasazerow_total + dict3[n]
        random.seed(a=random.random(), version=2)
        if n < 3:
            liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        if n > 2:
            var7 = "czy_wysiadaja_przystanek_"
            val7 = {n}
            dict7 = {var7:val7}
            dict7[n] = random.choice([0, 1]) #0 - nie wysiadają, 1 - wysiadają
            if dict7[n] == 1:
                var8 = "wysiadajacy_na_przystanku_"
                val8 = {n}
                dict8 = {var8:val8}
                var88 = "wysiadajacy_na_przystanku_temp_"
                val88 = {n}
                dict88 = {var88:val88}
                if 2 < n < 6:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 5 < n < 11:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 10 < n < 16:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 15 < n:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                print("Na przystanku %s wysiadło" % n, dict88[n], "pasażerów.")
                liczba_pasazerow_temp = dict8[n]+dict3[n]
            if dict7[n] == 0:
                liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        print("Na przystanku %s na ten kurs oczekiwało" % n, dict3[n], "pasażerów. W autobusie znajdowało się", liczba_pasazerow_temp, "pasażerów.")

if 0.9 < popularnosc_firmy < 0.99:
    for n in range (1, liczba_przystankow):
        var3 = "pasazerowie_przystanek_"
        val3 = {n}
        dict3 = {var3:val3}
        var4 = "temp_pasazerowie_przystanek_"
        val4 = {n}
        dict4 = {var4:val4}
        random.seed(a=random.random(), version=2)
        dict4[n] = random.choice([0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1])
        var5 = "zaokraglacz_pasazerowie_przystanek_"
        val5 = {n}
        dict5 = {var5:val5}
        var6 = "obliczacz_pasazerowie_przystanek_"
        val6 = {n}
        dict6 = {var6:val6}
        dict6[n] = dict4[n]*liczba_miejsc_w_autobusie
        dict5[n] = round(dict6[n])
        var55 = "check_przystanku_"
        val55 = n
        dict55 = {var55:val55}
        if czy_szczyt == "tak":
            if dict1[n] < 300:
                dict5[n] = round(dict5[n]/3)
            if dict1[n] >= 300:
                dict5[n] = round(dict5[n]/1.5)
        if czy_szczyt == "nie":
            if dict1[n] < 200:
                dict5[n] = round(dict5[n]/2)
        dict3[n] = dict5[n]
        liczba_pasazerow_total = liczba_pasazerow_total + dict3[n]
        random.seed(a=random.random(), version=2)
        if n < 3:
            liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        if n > 2:
            var7 = "czy_wysiadaja_przystanek_"
            val7 = {n}
            dict7 = {var7:val7}
            dict7[n] = random.choice([0, 1]) #0 - nie wysiadają, 1 - wysiadają
            if dict7[n] == 1:
                var8 = "wysiadajacy_na_przystanku_"
                val8 = {n}
                dict8 = {var8:val8}
                var88 = "wysiadajacy_na_przystanku_temp_"
                val88 = {n}
                dict88 = {var88:val88}
                if 2 < n < 6:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 5 < n < 11:
                    dict88[n] = random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 10 < n < 16:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                if 15 < n:
                    dict88[n] = random.choice([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6])
                    dict88[n] = round(liczba_pasazerow_temp*dict88[n])
                    if czy_szczyt == "tak":
                        if dict1[n] < 300:
                            dict88[n] = round(dict88[n]/3)
                    if czy_szczyt == "nie":
                        if dict1[n] < 200:
                            dict88[n] = round(dict88[n]/2)
                    dict8[n] = liczba_pasazerow_temp - dict88[n]
                print("Na przystanku %s wysiadło" % n, dict88[n], "pasażerów.")
                liczba_pasazerow_temp = dict8[n]+dict3[n]
            if dict7[n] == 0:
                liczba_pasazerow_temp = liczba_pasazerow_temp + dict3[n]
        print("Na przystanku %s na ten kurs oczekiwało" % n, dict3[n], "pasażerów. W autobusie znajdowało się", liczba_pasazerow_temp, "pasażerów.")

print("Podczas kursu przewieziono łącznie", liczba_pasazerow_total, "pasażerów.")