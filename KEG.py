import random
import sys
import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [
            [sg.Text('Witaj w Kalkulatorze Kolejowego EG v2.0 - TERAZ Z GUI!')],
            [sg.Text('PAMIĘTAJ, ŻE UŁAMKI PODAJEMY Z KROPKĄ!')],
            [sg.Text('Obliczanie dziennego popytu:', size=(51, 1)), sg.Text('Obliczanie ceny wynajmu:', size=(33, 1)), sg.Text('Obliczanie ceny zakupu:', size=(34, 1)), sg.Text('Obliczanie ceny wynajmu toru:', size=(50, 1))],
            [sg.Text('Liczba mieszkańców przy pierwszej stacji:', size=(40, 1)), sg.InputText('150000', size=(10, 1), key='stacja_1'), sg.Text('Powierzchnia działki:', size=(23, 1)), sg.InputText('', size=(10, 1), key='powierzchnia_dzialki'), sg.Text('Powierzchnia działki:', size=(23, 1)), sg.InputText('', size=(10, 1), key='powierzchnia_dzialki_kupno'), sg.Text('Długość toru:', size=(23, 1)), sg.InputText('', size=(10, 1), key='dlugosc_toru')],
            [sg.Text('Liczba mieszkańców przy drugiej stacji:', size=(40, 1)), sg.InputText('90000', size=(10, 1), key='stacja_2'), sg.Text('Cena za metr:', size=(23, 1)), sg.InputText('', size=(10, 1), key='cena_za_metr'), sg.Text('Cena za metr:', size=(23, 1)), sg.InputText('', size=(10, 1), key='cena_za_metr_kupno'), sg.Radio('Na godziny', "WYNAJEMTORU", default=True, key='radioboks_godzinowy'), sg.Text('Godziny:', size=(10, 1)), sg.InputText('', size=(10, 1), key='tor_w_godziny')],
            [sg.Text('Odległość między stacjami w km (ułam. dziesiętny)', size=(40, 1)), sg.InputText('150', size=(10, 1), key='odleglosc'), sg.Text('Liczba rat:', size=(23, 1)), sg.InputText('', size=(10, 1), key='r'), sg.Checkbox('Płatność ratalna', default=False, key='czekboks_ratalny'), sg.Text('Ilość rat:', size=(7, 1)), sg.InputText('', size=(10, 1), key='r_kupno'), sg.Radio('Długoterminowy', "WYNAJEMTORU", default=False, key='radioboks_dlugi'), sg.Text('Ilość dni:', size=(7, 1)), sg.InputText('', size=(10, 1), key='tor_w_dlugoterminowy')],
            [sg.Text('Czas przejazdu w godzinach (ułam. dziesiętny)', size=(40, 1)), sg.InputText('1.5', size=(10, 1), key='czas'), sg.Submit(button_text='Oblicz wynajem'), sg.Text('', size=(20, 1)), sg.Submit(button_text='Oblicz kupno'), sg.Text('', size=(22, 1)), sg.Submit(button_text='Oblicz wynajem toru')],
            [sg.Text('Czynnik specjalny zgodnie z PDF', size=(40, 1)), sg.InputText('1', size=(10, 1), key='czynnik_specjalny'), sg.Text('Łączny koszt wynajmu:', size=(23, 1)), sg.Text('', size=(10, 1), key='n'), sg.Text('Koszt zakupu:', size=(23, 1)), sg.Text('', size=(10, 1), key='cena_zakupu'), sg.Text('Koszt wynajmu:', size=(23, 1)), sg.Text('', size=(10, 1), key='koszt_wynajmu_toru')],
            [sg.Text('Współczynnik pop według tabeli', size=(40, 1)), sg.InputText('2', size=(10, 1), key='wspolczynnik_pop'), sg.Text('Wysokość miesięcznej raty:', size=(23, 1)), sg.Text('', size=(10, 1), key='mrg'), sg.Text('Wysokość raty:', size=(23, 1)), sg.Text('', size=(10, 1), key='cena_zakupu_rata')],
            [sg.Text('Minimalna ilość miejsc siedzących w pociągu:', size=(40, 1)), sg.InputText('400', size=(10, 1), key='ilosc_miejsc')],
            [sg.Submit(button_text='Oblicz popyt')],
            [sg.Text('', size=(30, 1)), sg.Text('2 kl:', size=(10, 1)), sg.Text('1 kl:', size=(10, 1)), sg.Text('Syp:', size=(10, 1)), sg.Text('Kusz:', size=(10, 1)), sg.Text('Autokusz:', size=(10, 1)), sg.Text('Poczta:', size=(10, 1))],
            [sg.Text('W dni robocze:', size=(30, 1)), sg.Text('', size=(10, 1), key='wynik_cd_1'), sg.Text('', size=(10, 1), key='wynik_cd_1_kl1'), sg.Text('', size=(10, 1), key='wynik_cd_1_syp'), sg.Text('', size=(10, 1), key='wynik_cd_1_kusz'), sg.Text('', size=(10, 1), key='wynik_cd_1_autkusz'), sg.Text('', size=(10, 1), key='wynik_cd_1_poczta')],
            [sg.Text('Pon-czw, ferie zimowe:', size=(30, 1)), sg.Text('', size=(10, 1), key='wynik_cd_1_3'), sg.Text('', size=(10, 1), key='wynik_cd_1_3_kl1'), sg.Text('', size=(10, 1), key='wynik_cd_1_3_syp'), sg.Text('', size=(10, 1), key='wynik_cd_1_3_kusz'), sg.Text('', size=(10, 1), key='wynik_cd_1_3_autkusz'), sg.Text('', size=(10, 1), key='wynik_cd_1_3_poczta')],
            [sg.Text('Pon-czw, wakacje i inne weekendy:', size=(30, 1)), sg.Text('', size=(10, 1), key='wynik_cd_1_5'), sg.Text('', size=(10, 1), key='wynik_cd_1_5_kl1'), sg.Text('', size=(10, 1), key='wynik_cd_1_5_syp'), sg.Text('', size=(10, 1), key='wynik_cd_1_5_kusz'), sg.Text('', size=(10, 1), key='wynik_cd_1_5_autkusz'), sg.Text('', size=(10, 1), key='wynik_cd_1_5_poczta')],
            [sg.Text('W weekendy:', size=(30, 1))],
            [sg.Text('Podczas ferii zimowych:', size=(30, 1)), sg.Text('', size=(10, 1), key='wynik_cd_1_7'), sg.Text('', size=(10, 1), key='wynik_cd_1_7_kl1'), sg.Text('', size=(10, 1), key='wynik_cd_1_7_syp'), sg.Text('', size=(10, 1), key='wynik_cd_1_7_kusz'), sg.Text('', size=(10, 1), key='wynik_cd_1_7_autkusz'), sg.Text('', size=(10, 1), key='wynik_cd_1_7_poczta')],
            [sg.Text('Wakacje, majówka, BN i Wielkanoc, NR:', size=(30, 1)), sg.Text('', size=(10, 1), key='wynik_cd_2'), sg.Text('', size=(10, 1), key='wynik_cd_2_kl1'), sg.Text('', size=(10, 1), key='wynik_cd_2_syp'), sg.Text('', size=(10, 1), key='wynik_cd_2_kusz'), sg.Text('', size=(10, 1), key='wynik_cd_2_autkusz'), sg.Text('', size=(10, 1), key='wynik_cd_2_poczta')],
            [sg.Text('Potrzebnych par pociągów:', size=(30, 1)), sg.Text('', size=(30, 1), key='potrzebnych_par_pociągów')],
        ]

window = sg.Window('Kolejowe EG - Kalkulator - TERAZ Z GUI!', layout)
#co_chcesz_obliczyc = input("Wpisz co chcesz obliczyć: popyt, koszt wynajmu nieruchomości, koszt wykupu nieruchomości, cenę najmu toru. WPISZ TAK JAK WIDNIEJE OBOK. ")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Oblicz popyt':
        wynik = 0
        stacja_1 = float(values['stacja_1'])
        stacja_2 = float(values['stacja_2'])
        odleglosc = float(values['odleglosc'])
        czas = float(values['czas'])
        czynnik_specjalny = float(values['czynnik_specjalny'])
        wspolczynnik_pop = float(values['wspolczynnik_pop'])
        ilosc_miejsc = float(values['ilosc_miejsc'])
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
        potrzebnych_par_pociągów = round((wynik_cd_1+wynik_cd_1_kl1)/ilosc_miejsc)
        if potrzebnych_par_pociągów < 1:
            potrzebnych_par_pociągów = 1
        window['wynik_cd_1'](wynik_cd_1)
        window['wynik_cd_1_3'](wynik_cd_1_3)
        window['wynik_cd_1_5'](wynik_cd_1_5)
        window['wynik_cd_1_7'](wynik_cd_1_7)
        window['wynik_cd_2'](wynik_cd_2)
        window['wynik_cd_1_kl1'](wynik_cd_1_kl1)
        window['wynik_cd_1_3_kl1'](wynik_cd_1_3_kl1)
        window['wynik_cd_1_5_kl1'](wynik_cd_1_5_kl1)
        window['wynik_cd_1_7_kl1'](wynik_cd_1_7_kl1)
        window['wynik_cd_2_kl1'](wynik_cd_2_kl1)
        window['wynik_cd_1_syp'](wynik_cd_1_syp)
        window['wynik_cd_1_3_syp'](wynik_cd_1_3_syp)
        window['wynik_cd_1_5_syp'](wynik_cd_1_5_syp)
        window['wynik_cd_1_7_syp'](wynik_cd_1_7_syp)
        window['wynik_cd_2_syp'](wynik_cd_2_syp)
        window['wynik_cd_1_kusz'](wynik_cd_1_kusz)
        window['wynik_cd_1_3_kusz'](wynik_cd_1_3_kusz)
        window['wynik_cd_1_5_kusz'](wynik_cd_1_5_kusz)
        window['wynik_cd_1_7_kusz'](wynik_cd_1_7_kusz)
        window['wynik_cd_2_kusz'](wynik_cd_2_kusz)
        window['wynik_cd_1_autkusz'](wynik_cd_1_autkusz)
        window['wynik_cd_1_3_autkusz'](wynik_cd_1_3_autkusz)
        window['wynik_cd_1_5_autkusz'](wynik_cd_1_5_autkusz)
        window['wynik_cd_1_7_autkusz'](wynik_cd_1_7_autkusz)
        window['wynik_cd_2_autkusz'](wynik_cd_2_autkusz)
        window['wynik_cd_1_poczta'](wynik_cd_1_poczta)
        window['wynik_cd_1_3_poczta'](wynik_cd_1_3_poczta)
        window['wynik_cd_1_5_poczta'](wynik_cd_1_5_poczta)
        window['wynik_cd_1_7_poczta'](wynik_cd_1_7_poczta)
        window['wynik_cd_2_poczta'](wynik_cd_2_poczta)
        window['potrzebnych_par_pociągów'](potrzebnych_par_pociągów)
    if event == 'Oblicz wynajem':
        powierzchnia_dzialki = float(values['powierzchnia_dzialki'])
        cena_za_metr = float(values['cena_za_metr'])
        r = float(values['r'])
        t = round((float(powierzchnia_dzialki)*(float(cena_za_metr))), 2)
        if t > 100000:
            procent_podatku = 12.5
        if t < 100001:
            procent_podatku = 8.5
        o = round((float(procent_podatku)/100*(float(cena_za_metr))), 2)
        n = (float(o)+float(t))
        mrg = (float(n)/float(r))
        window['n'](n)
        window['mrg'](mrg)
    if event == 'Oblicz kupno':
        if values['czekboks_ratalny'] == False:
            powierzchnia_dzialki = float(values['powierzchnia_dzialki_kupno'])
            cena_za_metr = float(values['cena_za_metr_kupno'])
            t = round((powierzchnia_dzialki*cena_za_metr), 2)
            d = round((t*1), 2)
            nd = round((d-(d*0.3)), 2)
            window['cena_zakupu'](nd)
            window['cena_zakupu_rata']('')
        if values['czekboks_ratalny'] == True:
            powierzchnia_dzialki = float(values['powierzchnia_dzialki_kupno'])
            cena_za_metr = float(values['cena_za_metr_kupno'])
            r = float(values['r_kupno'])
            t = round((powierzchnia_dzialki*cena_za_metr), 2)
            l = round((float(t)*2), 2)
            d = round((float(t)+float(l)), 2)
            wr = round((float(d)/float(r)), 2)
            nwr = round(((float(wr)*0.095)+float(wr)), 2)
            wds = round((float(nwr)*float(r)), 2)
            window['cena_zakupu'](wds)
            window['cena_zakupu_rata'](nwr)
    if event == 'Oblicz wynajem toru':
        if values['radioboks_godzinowy'] == True:
            h = float(values['tor_w_godziny'])
            x = float(values['dlugosc_toru'])
            t = round(((8.2*(float(x)+2.5))*(float(h))*1.48), 2)
            vat = round((float(t)*0.23), 2)
            vatt = round((float(t)+float(vat)), 2)
            window['koszt_wynajmu_toru'](vatt)
        if values['radioboks_dlugi'] == True:
            d = float(values['tor_w_dlugoterminowy'])
            x = float(values['dlugosc_toru'])
            t = round((8.2*(float(x)+5))*(24*(float(d))*1.48), 2)
            vat = round((t*0.23), 2)
            vatt = round((float(t)+float(vat)), 2)
            window['koszt_wynajmu_toru'](vatt)

window.close()