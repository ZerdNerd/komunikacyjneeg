import random
import sys

co_chcesz_obliczyc = input("Wpisz co chcesz obliczyć: popyt, koszt wynajmu nieruchomości, koszt wykupu nieruchomości, cenę najmu toru. WPISZ TAK JAK WIDNIEJE OBOK. ")

if co_chcesz_obliczyc == "popyt":

    ile_relacji = int(input("Popyt dla ilu relacji chcesz dziś obliczyć? (wpisz liczbę) "))
    pierwsza_klasa = input("Czy potrzebujesz popytu na 1 klasę? (TAK lub NIE) ")
    sypialne = input("Czy potrzebujesz popytu na wagony sypialne? (TAK lub NIE) ")
    kuszetki = input("Czy potrzebujesz popytu na wagony kuszetki? (TAK lub NIE) ")
    autokuszetki = input("Czy potrzebujesz popytu na autokuszetki? (TAK lub NIE) ")
    poczta = input("Czy potrzebujesz popytu na wagony pocztowe? (TAK lub NIE) ")

    for ile_relacji in range(0, ile_relacji):
        wynik = 0
        stacja_1 = float(input("Podaj liczbę mieszkańców miejscowości przy pierwszej stacji. "))
        stacja_2 = float(input("Podaj liczbę mieszkańców miejscowości przy drugiej stacji. "))
        odleglosc = float(input("Podaj odległość między stacjami w km jako ułamek dziesiętny (jeżeli kwalifikuje się; PAMIĘTAJ ŻE UŁAMKI Z KROPKĄ). "))
        czas = float(input("Podaj czas przejazdu między stacjami w godzinach. Jeżeli są minuty, podaj jako ułamek dziesiętny (podziel minuty przez 60). "))
        czynnik_specjalny = 1 #float(input("Podaj czynnik specjalny zgodnie z instrukcją w pdf. "))
        wspolczynnik_pop = float(input("Podaj współczynnik pop. "))
    #    czynnik_dnia = float(input("Podaj współczynnik dnia kursowania zgodnie z instrukcją. "))
        wynik_cd_2 = round((stacja_1+stacja_2)/600000*(odleglosc/czas)*czynnik_specjalny*wspolczynnik_pop*2)
        wynik_cd_1_7 = round((stacja_1+stacja_2)/600000*(odleglosc/czas)*czynnik_specjalny*wspolczynnik_pop*1.7)
        wynik_cd_1_5 = round((stacja_1+stacja_2)/600000*(odleglosc/czas)*czynnik_specjalny*wspolczynnik_pop*1.5)
        wynik_cd_1_3 = round((stacja_1+stacja_2)/600000*(odleglosc/czas)*czynnik_specjalny*wspolczynnik_pop*1.3)
        wynik_cd_1 = round((stacja_1+stacja_2)/600000*(odleglosc/czas)*czynnik_specjalny*wspolczynnik_pop*1)
        wynik_cd_1_kl1 = (round(wynik_cd_1/5))
        wynik_cd_1_3_kl1 = (round(wynik_cd_1_3/5))
        wynik_cd_1_5_kl1 = (round(wynik_cd_1_5/5))
        wynik_cd_1_7_kl1 = (round(wynik_cd_1_7/5))
        wynik_cd_2_kl1 = (round(wynik_cd_2/5))
        wynik_cd_1_syp = (round(wynik_cd_1/15))
        wynik_cd_1_3_syp = (round(wynik_cd_1_3/15))
        wynik_cd_1_5_syp = (round(wynik_cd_1_5/15))
        wynik_cd_1_7_syp = (round(wynik_cd_1_7/15))
        wynik_cd_2_syp = (round(wynik_cd_2/15))
        wynik_cd_1_kusz = (round(wynik_cd_1/13))
        wynik_cd_1_3_kusz = (round(wynik_cd_1_3/13))
        wynik_cd_1_5_kusz = (round(wynik_cd_1_5/13))
        wynik_cd_1_7_kusz = (round(wynik_cd_1_7/13))
        wynik_cd_2_kusz = (round(wynik_cd_2/13))
        wynik_cd_1_autkusz = (round(wynik_cd_1/70))
        wynik_cd_1_3_autkusz = (round(wynik_cd_1_3/70))
        wynik_cd_1_5_autkusz = (round(wynik_cd_1_5/70))
        wynik_cd_1_7_autkusz = (round(wynik_cd_1_7/70))
        wynik_cd_2_autkusz = (round(wynik_cd_2/70))
        wynik_cd_1_poczta = (round(wynik_cd_1/450))
        wynik_cd_1_3_poczta = (round(wynik_cd_1_3/450))
        wynik_cd_1_5_poczta = (round(wynik_cd_1_5/450))
        wynik_cd_1_7_poczta = (round(wynik_cd_1_7/450))
        wynik_cd_2_poczta = (round(wynik_cd_2/450))
    #    wynik = round((stacja_1+stacja_2)/600000*(odleglosc/czas)*czynnik_specjalny*wspolczynnik_pop*czynnik_dnia)
        print("Popyt na połączenie w tej relacji wynosi:")
        print(wynik_cd_1, "pasażerów 2 klasy w dni robocze;")
        print(wynik_cd_1_3, "pasażerów 2 klasy od poniedziałku do czwartku podczas ferii zimowych;")
        print(wynik_cd_1_5, "pasażerów 2 klasy od poniedziałku do czwartku podczas wakacji oraz pozostałe weekendy;")
        print(wynik_cd_1_7, "pasażerów 2 klasy w weekendy podczas ferii zimowych;")
        print(wynik_cd_2, "pasażerów 2 klasy w wakacyjne weekendy, w weekend majowy, na święta Narodzenia i Zmartwychwstania Pańskiego, na Nowy Rok;")
        if pierwsza_klasa == "TAK":
            print(wynik_cd_1_kl1, "pasażerów 1 klasy w dni robocze;")
            print(wynik_cd_1_3_kl1, "pasażerów 1 klasy od poniedziałku do czwartku podczas ferii zimowych;")
            print(wynik_cd_1_5_kl1, "pasażerów 1 klasy od poniedziałku do czwartku podczas wakacji oraz pozostałe weekendy;")
            print(wynik_cd_1_7_kl1, "pasażerów 1 klasy w weekendy podczas ferii zimowych;")
            print(wynik_cd_2_kl1, "pasażerów 1 klasy w wakacyjne weekendy, w weekend majowy, na święta Narodzenia i Zmartwychwstania Pańskiego, na Nowy Rok;")
        if sypialne == "TAK":
            print(wynik_cd_1_syp, "pasażerów wagonów sypialnych w dni robocze;")
            print(wynik_cd_1_3_syp, "pasażerów wagonów sypialnych od poniedziałku do czwartku podczas ferii zimowych;")
            print(wynik_cd_1_5_syp, "pasażerów wagonów sypialnych od poniedziałku do czwartku podczas wakacji oraz pozostałe weekendy;")
            print(wynik_cd_1_7_syp, "pasażerów wagonów sypialnych w weekendy podczas ferii zimowych;")
            print(wynik_cd_2_syp, "pasażerów wagonów sypialnych w wakacyjne weekendy, w weekend majowy, na święta Narodzenia i Zmartwychwstania Pańskiego, na Nowy Rok;")
        if kuszetki == "TAK":
            print(wynik_cd_1_kusz, "pasażerów wagonów kuszetek w dni robocze;")
            print(wynik_cd_1_3_kusz, "pasażerów wagonów kuszetek od poniedziałku do czwartku podczas ferii zimowych;")
            print(wynik_cd_1_5_kusz, "pasażerów wagonów kuszetek od poniedziałku do czwartku podczas wakacji oraz pozostałe weekendy;")
            print(wynik_cd_1_7_kusz, "pasażerów wagonów kuszetek w weekendy podczas ferii zimowych;")
            print(wynik_cd_2_kusz, "pasażerów wagonów kuszetek w wakacyjne weekendy, w weekend majowy, na święta Narodzenia i Zmartwychwstania Pańskiego, na Nowy Rok;")
        if autokuszetki == "TAK":
            print(wynik_cd_1_autkusz, "pasażerów wagonów autokuszetek w dni robocze;")
            print(wynik_cd_1_3_autkusz, "pasażerów wagonów autokuszetek od poniedziałku do czwartku podczas ferii zimowych;")
            print(wynik_cd_1_5_autkusz, "pasażerów wagonów autokuszetek od poniedziałku do czwartku podczas wakacji oraz pozostałe weekendy;")
            print(wynik_cd_1_7_autkusz, "pasażerów wagonów autokuszetek w weekendy podczas ferii zimowych;")
            print(wynik_cd_2_autkusz, "pasażerów wagonów autokuszetek w wakacyjne weekendy, w weekend majowy, na święta Narodzenia i Zmartwychwstania Pańskiego, na Nowy Rok;")
        if poczta == "TAK":
            print(wynik_cd_1_poczta, "worków poczty w dni robocze;")
            print(wynik_cd_1_3_poczta, "worków poczty od poniedziałku do czwartku podczas ferii zimowych;")
            print(wynik_cd_1_5_poczta, "worków poczty od poniedziałku do czwartku podczas wakacji oraz pozostałe weekendy;")
            print(wynik_cd_1_7_poczta, "worków poczty w weekendy podczas ferii zimowych;")
            print(wynik_cd_2_poczta, "worków poczty w wakacyjne weekendy, w weekend majowy, na święta Narodzenia i Zmartwychwstania Pańskiego, na Nowy Rok;")
    else:
        wyjscie = input("Zakończyłem liczenie. Do dalszego działania musisz mnie uruchomić ponownie bo autor jest leniwą bułą albo nie potrafi kodować w pythonie (raczej to drugie). Naciśnij enter, aby wyjść z programu. ")

if co_chcesz_obliczyc == "koszt wynajmu nieruchomości":
    powierzchnia_dzialki = float(input("Podaj powierzchnię działki w metrach kwadratowych. PAMIĘTAJ ŻE UŁAMKI Z KROPKĄ. "))
    cena_za_metr = float(input("Podaj cenę za metr kwadratowy. Znajdziesz ją w tabelach w arkuszu EG 2.0, zakładka Ekonomia - Nieruchomości. "))
    procent_podatku = float(input("Podaj procent podatku jaki ma zastosowanie: 8.5% lub 12.5%. "))
    t = (round(powierzchnia_dzialki*cena_za_metr), 2)
    o = (round(procent_podatku/100*cena_za_metr), 2)
    n = (o+t)
    print("Cena wynajmu wybranej działki wynosi", n, "złotych. Cena zawiera już doliczony podatek, który wynosi", o, "złotych. ")
    wyjscie = input("Zakończyłem liczenie. Do dalszego działania musisz mnie uruchomić ponownie bo autor jest leniwą bułą albo nie potrafi kodować w pythonie (raczej to drugie). Naciśnij enter, aby wyjść z programu. ")

if co_chcesz_obliczyc == "koszt wykupu nieruchomości":
    jednorazowo_czy_raty = input("Płatność jednorazowa czy ratalna? Wpisz tak jak jest obok. ")
    if jednorazowo_czy_raty == "jednorazowa":
        powierzchnia_dzialki = float(input("Podaj powierzchnię działki w metrach kwadratowych. PAMIĘTAJ ŻE UŁAMKI Z KROPKĄ. "))
        cena_za_metr = float(input("Podaj cenę za metr kwadratowy. Znajdziesz ją w tabelach w arkuszu EG 2.0, zakładka Ekonomia - Nieruchomości. "))
        t = (round(powierzchnia_dzialki*cena_za_metr), 2)
        k = (round(t*20), 2)
        d = (round(t*k), 2)
        s = (round((d*0.23)+d), 2)
        vat = (round(d*0.23), 2)
        print("Cena zakupu działki wynosi", s, "złotych. VAT wynosi", vat, "złotych. ")
        wyjscie = input("Zakończyłem liczenie. Do dalszego działania musisz mnie uruchomić ponownie bo autor jest leniwą bułą albo nie potrafi kodować w pythonie (raczej to drugie). Naciśnij enter, aby wyjść z programu. ")
    if jednorazowo_czy_raty == "ratalna":
        powierzchnia_dzialki = float(input("Podaj powierzchnię działki w metrach kwadratowych. PAMIĘTAJ ŻE UŁAMKI Z KROPKĄ. "))
        cena_za_metr = float(input("Podaj cenę za metr kwadratowy. Znajdziesz ją w tabelach w arkuszu EG 2.0, zakładka Ekonomia - Nieruchomości. "))
        r = float(input("Jaka ilość rat wariacie? "))
        t = (round(powierzchnia_dzialki*cena_za_metr), 2)
        l = (round(t*20), 2)
        d = (round(t*l), 2)
        wr = (round(d/r), 2)
        nwr = (round((wr*0.095)+wr), 2)
        podatek = (round((nwr*r)*0.23), 2)
        sd = (round(d+podatek), 2)
        print("Cena zakupu działki wynosi", sd, "złotych. VAT wynosi", podatek, "złotych. Wysokość jednej raty to", nwr, "złotych. ")
        wyjscie = input("Zakończyłem liczenie. Do dalszego działania musisz mnie uruchomić ponownie bo autor jest leniwą bułą albo nie potrafi kodować w pythonie (raczej to drugie). Naciśnij enter, aby wyjść z programu. ")

if co_chcesz_obliczyc == "cenę najmu toru":
    na_godziny_czy_dlugoterminowo = input("Na godziny czy długoterminowo? Wpisz 'na godziny' lub 'długoterminowo'. ")
    if na_godziny_czy_dlugoterminowo == "na godziny":
        h = (float(input("Podaj ilość godzin. ")))
        x = (float(input("Podaj długość toru w metrach. ")))
        t = (round((8.2*(x+2.5))*h*1.48), 2)
        vat = (round(t*0.23), 2)
        print("Cena wynajmu toru wynosi", t, "złotych za cały okres. VAT wynosi", vat, "złotych. ")
        wyjscie = input("Zakończyłem liczenie. Do dalszego działania musisz mnie uruchomić ponownie bo autor jest leniwą bułą albo nie potrafi kodować w pythonie (raczej to drugie). Naciśnij enter, aby wyjść z programu. ")
    if na_godziny_czy_dlugoterminowo == "długoterminowo":
        d = (float(input("Podaj ilość dni. ")))
        x = (float(input("Podaj długość toru w metrach. ")))
        t = (round((8.2*(x+5))*(24*d)*1.48), 2)
        vat = (round(t*0.23), 2)
        print("Cena wynajmu toru wynosi", t, "złotych za cały okres. VAT wynosi", vat, "złotych. ")
        wyjscie = input("Zakończyłem liczenie. Do dalszego działania musisz mnie uruchomić ponownie bo autor jest leniwą bułą albo nie potrafi kodować w pythonie (raczej to drugie). Naciśnij enter, aby wyjść z programu. ")
else:
    print("wtf, coś ty wpisał?")