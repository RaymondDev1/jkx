from tkinter import *


def import_dannyx():
    uslugi_func = []
    f1 = open("d:\\Dannye\d.txt", "r")
    a = f1.readlines()
    print(a)
    f1.close()
    for c in a:
        b = c.split(' ')
        b.pop()
        chisla = []
        for i in b:
            ch = int(i)
            chisla.append(ch)
        uslugi_func.append(chisla)
    print(uslugi_func)
    return uslugi_func


def import_tarifs():
    f1 = open("d:\\Dannye\_tarifs.txt", "r")
    a = f1.read()
    f1.close()
    tarif_m = []
    b = a.split(" ")
    for i in b:
        ch = int(i)
        tarif_m.append(ch)
    print(tarif_m)
    return tarif_m


uslugi_main = import_dannyx()
tarif = import_tarifs()


def vyvod_info_cl(uslugi_func):
    def wclose4():
        wind4.destroy()

    def wenter4():
        no_kv0 = e41.get()
        dannye = 0
        if no_kv0 == "":
            txt42.config(text="Данные не введены")
        else:
            no_kv = int(e41.get())
            if len(uslugi_func) == 0:
                txt42.config(text="База пуста")
            else:
                for t in uslugi_func:
                    if t[0] == no_kv:
                        dannye = dannye + 1

                j = 0
                for t in uslugi_func:
                    if t[0] == no_kv:
                        txt42.config(text='')
                        txt43[j].config(
                            text='Инфо. о квартире: ' + str(t[0]) + ' - номер квартиры, ' + str(t[1]) + ' - месяц, '
                                 + str(t[2]) + ' - кв. плата, ' + str(t[3]) + ' - электричество, ' + str(t[4]) +
                                 ' - вода, ' + str(t[5]) + ' - газ')
                        j += 1
                for o in range(j, len(uslugi_func)):
                    txt43[o].config(text='')

            if dannye == 0:
                txt42.config(text='Запрашиваемые данные не найдены.')


    wind4 = Tk()
    wind4.title("Вывод информации о квартире")
    wind4.geometry("800x600+200+200")

    txt41 = Label(wind4)
    txt41.config(text="Номер квартиры")
    txt41.pack()

    e41 = Entry(wind4)
    e41.pack()

    btn41 = Button(wind4)
    btn41.config(text="Ввести", font=("Arial", 12), command=wenter4)
    btn41.pack(pady=10)

    txt42 = Label(wind4)
    txt42.pack()

    txt43 = []
    for i in range(len(uslugi_func)):
        a = Label(wind4)
        a.pack()
        txt43.append(a)

    btn42 = Button(wind4)
    btn42.config(text="Закрыть", font=("Arial", 12), command=wclose4)
    btn42.pack(side=BOTTOM, pady=10)
    wind4.mainloop()


def info(uslugi_func):
    def wclose5():
        wind5.destroy()

    wh = str(len(uslugi_func) * 30 + 50)
    wind5 = Tk()
    wind5.title("Вывод информации о всех квартирах")
    wind5.geometry("800x" + wh + "+200+200")

    txt52 = Label(wind5)

    txt51 = []
    for i in range(len(uslugi_func)):
        a = Label(wind5)
        a.pack()
        txt51.append(a)

    if len(uslugi_func) == 0:
        txt52.config(text="База пуста ")
    else:
        for j in range(len(uslugi_func)):
            txt51[j].config(text='Инфо. о квартире: ' + str(uslugi_func[j][0]) + ' - номер квартиры, ' + str(
                uslugi_func[j][1]) + ' - месяц, ' + str(uslugi_func[j][2]) + ' - кв. плата, ' + str(uslugi_func[j][3]) +
                                 ' - электричество, ' + str(uslugi_func[j][4]) + ' - вода, ' + str(uslugi_func[j][5])
                                 + ' - газ')
            print('Инфо. о квартире:', uslugi_func[j][0], ' - номер квартиры,', uslugi_func[j][1], ' - месяц,',
                  uslugi_func[j][2], ' - кв. плата,', uslugi_func[j][3], ' - электричество,',
                  uslugi_func[j][4], ' - вода,', uslugi_func[j][5], ' - газ')
    txt52.pack()

    btn51 = Button(wind5)
    btn51.config(text="Закрыть", font=("Arial", 12), command=wclose5)
    btn51.pack(side=BOTTOM, pady=10)
    wind5.mainloop()

    return uslugi_func


def dolg(uslugi_func):
    def wclose6():
        wind6.destroy()

    def wenter6():
        dannye = 0
        mas_zadolj = [0, 0, 0, 0]
        podskazki_dolg = ["За кв.плату: ", "За эл-во: ", "За воду: ", "За газ: "]

        no_kv0 = e61.get()
        if no_kv0 == '':
            txt62.config(text='Данные не введены')
            for j in range(5):
                txt63[j].config(text="")
        else:
            no_kv = int(no_kv0)
            for i in uslugi_func:
                if i[0] == no_kv:
                    dannye = 1
                    for j in range(4):
                        if len(i) > 6:
                            mas_zadolj[j] = mas_zadolj[j] + i[j + 2] * tarif[j] - i[j + 6]
                        else:
                            (mas_zadolj[j]) = mas_zadolj[j] + i[j + 2] * tarif[j]
            if dannye == 0:
                txt62.config(text='Запрашиваемые данные не найдены.')
                for j in range(5):
                    txt63[j].config(text="")
            else:
                txt62.config(text='Задолженность по квартире № ' + str(no_kv))
                for j in range(4):
                    if mas_zadolj[j] < 0:
                        txt63[j].config(text=str(podskazki_dolg[j]) + 'Остаток на балансе: ' + str(-1 * mas_zadolj[j]))
                    else:
                        txt63[j].config(text=podskazki_dolg[j] + str(mas_zadolj[j]))
                if sum(mas_zadolj) < 0:
                    txt63[4].config(text='Общий остаток на балансе: ' + str(-1 * sum(mas_zadolj)))
                else:
                    txt63[4].config(text='Общая сумма задолженности: ' + str(sum(mas_zadolj)))


    wind6 = Tk()
    wind6.title("Вывод информации о задолженности")
    wind6.geometry("500x300")

    txt61 = Label(wind6)
    txt61.config(text="Номер квартиры")
    txt61.pack()

    e61 = Entry(wind6)
    e61.pack()

    btn61 = Button(wind6)
    btn61.config(text="Ввести", font=("Arial", 12), command=wenter6)
    btn61.pack(pady=10)

    txt62 = Label(wind6)
    txt62.config(text="")
    txt62.pack()

    txt63 = []
    for i in range(5):
        a = Label(wind6)
        a.pack()
        txt63.append(a)

    btn61 = Button(wind6)
    btn61.config(text="Закрыть", font=("Arial", 12), command=wclose6)
    btn61.pack(side=BOTTOM, pady=10)
    wind6.mainloop()
    return uslugi_func


def kvit(uslugi_func):
    def wclose3():
        wind3.destroy()

    def wenter3():
        no_kv0 = e31.get()
        mesyac0 = e32.get()
        if no_kv0 == "" or mesyac0 == "":
            txt33.config(text='Данные не введены')
        else:
            no_kv = int(e31.get())
            mesyac = int(e32.get())
            par_f = []
            dannye = 0
            for k in uslugi_func:
                if k[0] == no_kv and k[1] == mesyac:
                    dannye = 1
                    for i in range(0, 4):
                        p = k[i + 2] * tarif[i]
                        par_f.append(p)
                    txt33.config(text='Квитанция квартиры № ' + str(no_kv) + ' за ' + str(mesyac) + ' месяц')
                    txt34.config(text=str(par_f[0]) + ' руб. = кварт. плата\n' + str(par_f[1]) +
                                      ' руб. = электричество\n' + str(par_f[2]) + ' руб. = вода\n' + str(
                        par_f[3]) + ' руб. = газ\n' +
                                      str(sum(par_f)) + ' руб. = общая сумма за квитанцию')
            if dannye == 0:
                txt33.config(text='Запрашиваемые данные не найдены')
                txt34.config(text='')

    wind3 = Tk()
    wind3.title("Получить квитанцию о квартире")
    wind3.geometry("500x400")

    txt31 = Label(wind3)
    txt31.config(text="Какой номер квартиры? ")
    txt31.pack(pady=10, padx=10)

    e31 = Entry(wind3)
    e31.pack()

    txt32 = Label(wind3)
    txt32.config(text="Какой месяц? ")
    txt32.pack(pady=10, padx=10)

    e32 = Entry(wind3)
    e32.pack()

    btn31 = Button(wind3)
    btn31.config(text="Ввести", font=("Arial", 12), command=wenter3)
    btn31.pack(pady=10)

    txt33 = Label(wind3)
    txt33.pack()

    txt34 = Label(wind3)
    txt34.pack()

    btn32 = Button(wind3)
    btn32.config(text="Закрыть", font=("Arial", 12), command=wclose3)
    btn32.pack(side=BOTTOM, pady=10)
    wind3.mainloop()


def enter1(uslugi_func):
    def wclose1():
        wind1.destroy()

    def wenter1():

        def wenter1_yes():
            uslugi_func.pop(nd)
            uslugi_func.append(kvartira_m)
            txt17.config(text="Данные перезаписаны")
            txt16.config(text="")

        def wenter1_no():
            txt17.config(text="Данные в исходном состоянии")
            txt16.config(text="")

        kvartira_m = []
        btn11.config(state="disabled")

        for i in range(6):
            par_f = e1[i].get()
            kvartira_m.append(par_f)
        txt16.config(text="")
        if "" in kvartira_m:
            txt16.config(text="Заполните данные")
        else:
            for i in range(6):
                kvartira_m[i] = int(kvartira_m[i])
            dd = 0
            i = 0
            for k in uslugi_func:
                if k[0] == kvartira_m[0] and k[1] == kvartira_m[1]:
                    dd = 1
                    nd = i
                i = i + 1

            if dd == 1:
                wind1.geometry("500x700")
                txt11 = Label(wind1)
                txt11.pack()
                txt11.config(text='Такие данные есть в базе данных. Перезаписать?')
                btn12 = Button(wind1)
                btn12.config(text="Да", font=("Arial", 12), command=wenter1_yes)
                btn12.pack(pady=10)
                btn13 = Button(wind1)
                btn13.config(text="Нет", font=("Arial", 12), command=wenter1_no)
                btn13.pack(pady=10)
            else:
                uslugi_func.append(kvartira_m)
            txt17 = Label(wind1)
            txt17.pack()

            f1 = open("d:\\Dannye\d.txt", "w")
            for k in uslugi_func:
                for i in range(len(k)):
                    f1.write(str(k[i]))
                    f1.write(" ")
                f1.write("\n")
            f1.close()

    podskazki = ["номер квартиры: ", "месяц: ", "кв.плату: ", "за эл-во: ", "за воду: ", "за газ: "]

    wind1 = Tk()
    wind1.title("Ввод данных о квартире")
    wind1.geometry("500x600")
    txt1 = []
    e1 = []
    for i in range(6):
        a = Label(wind1)
        a.config(text="Введите " + podskazki[i], pady=5)
        a.pack()
        txt1.append(a)
        b = Entry(wind1)
        b.pack()
        e1.append(b)

    btn11 = Button(wind1)
    btn11.config(text="Ввести", font=("Arial", 12), command=wenter1)
    btn11.pack(pady=10)

    txt16 = Label(wind1)
    txt16.pack()

    btn14 = Button(wind1)
    btn14.config(text="Закрыть", font=("Arial", 12), command=wclose1)
    btn14.pack(side=BOTTOM, pady=10)
    wind1.mainloop()
    return uslugi_func


def oplata(uslugi_func):
    def wclose2():
        wind2.destroy()

    def wenter2():

        kvartira_f = []

        for i in range(6):
            par_f = e2[i].get()
            kvartira_f.append(par_f)
        txt26.config(text="")
        if "" in kvartira_f:
            txt26.config(text="Заполните данные")
        else:
            for i in range(6):
                kvartira_f[i] = int(kvartira_f[i])

        dannye = 0
        for k in uslugi_func:
            if k[0] == kvartira_f[0] and k[1] == kvartira_f[1]:
                dannye = 1
                for i in range(4):
                    k.append(kvartira_f[i + 2])
        if dannye == 0:
            txt26.config(text='Запрашиваемые данные не найдены.')

        f1 = open("d:\\Dannye\d.txt", "w")
        for k in uslugi_func:
            for i in range(len(k)):
                f1.write(str(k[i]))
                f1.write(" ")
            f1.write("\n")
        f1.close()

    wind2 = Tk()
    wind2.title("Введите данные об оплате")
    wind2.geometry("500x600")

    podskazki_oplata = ["номер квартиры: ", "месяц: ", "оплату за кв.плату: ", "оплату за эл-во: ", "оплату за воду: ",
                        "оплату за газ: "]

    txt2 = []
    e2 = []

    for i in range(6):
        a = Label(wind2)
        a.config(text="Введите " + podskazki_oplata[i], pady=5)
        a.pack()
        txt2.append(a)
        b = Entry(wind2)
        b.pack()
        e2.append(b)

    btn21 = Button(wind2)
    btn21.config(text="Ввести", font=("Arial", 12), command=wenter2)
    btn21.pack(pady=10)

    txt26 = Label(wind2)
    txt26.pack()

    btn22 = Button(wind2)
    btn22.config(text="Закрыть", font=("Arial", 12), command=wclose2)
    btn22.pack(side=BOTTOM, pady=10)
    wind2.mainloop()

    return uslugi_func


def del_data(uslugi_func):
    def wclose6():
        wind6.destroy()

    def wenter6():
        no_kv0 = e61.get()
        mesyac0 = e62.get()
        if no_kv0 == "" or mesyac0 == "":
            txt64.config(text='Данные не введены')
        else:
            fl = 0
            print('Какие данные нужно удалить?')
            no_kv = int(no_kv0)
            mesyac = int(mesyac0)
            for i in uslugi_func:
                if no_kv == i[0] and mesyac == i[1]:
                    uslugi_func.remove(i)
                    txt64.config(text='Данные удалены.')
                    fl = 1
                    break
            if fl == 0:
                txt64.config(text='Данные не найдены.')

        f1 = open("d:\\Dannye\d.txt", "w")
        for k in uslugi_func:
            for i in range(len(k)):
                f1.write(str(k[i]))
                f1.write(" ")
            f1.write("\n")
        f1.close()

        return uslugi_func

    wind6 = Tk()
    wind6.title("Удаление данных")
    wind6.geometry("500x400")

    txt61 = Label(wind6)
    txt61.config(text='Какие данные нужно удалить?')
    txt61.pack(pady=10, padx=10)

    txt62 = Label(wind6)
    txt62.config(text='Номер квартиры:')
    txt62.pack(pady=10, padx=10)

    e61 = Entry(wind6)
    e61.pack()

    txt63 = Label(wind6)
    txt63.config(text='Месяц:')
    txt63.pack(pady=10, padx=10)

    e62 = Entry(wind6)
    e62.pack()

    btn61 = Button(wind6)
    btn61.config(text="Ввести", font=("Arial", 12), command=wenter6)
    btn61.pack(pady=10)

    txt64 = Label(wind6)
    txt64.pack()

    btn62 = Button(wind6)
    btn62.config(text="Закрыть", font=("Arial", 12), command=wclose6)
    btn62.pack(side=BOTTOM, pady=10)

    wind6.mainloop()


wind = Tk()
wind.title("Оплата услуг ЖКХ")
wind.geometry("800x600")

btn = []
nadpisi_kn = ["Ввод данных о квартире", "Ввод данных об оплате", "Получить квитанцию о квартире",
              "Вывод информации о квартире", "Вывод информации о всех квартирах", "Вывод информации о задолженности",
              "Удаление данных"]
for i in range(7):
    a = Button()
    btn.append(a)
for i in range(7):
    btn[i].config(text=nadpisi_kn[i], font=("Arial", 20), width=30, pady=5, padx=5, background="black",
                  foreground="white")
    btn[i].place(x=140, y=20 + i * 80)

btn[0].config(command=lambda: enter1(uslugi_main))
btn[1].config(command=lambda: oplata(uslugi_main))
btn[2].config(command=lambda: kvit(uslugi_main))
btn[3].config(command=lambda: vyvod_info_cl(uslugi_main))
btn[4].config(command=lambda: info(uslugi_main))
btn[5].config(command=lambda: dolg(uslugi_main))
btn[6].config(command=lambda: del_data(uslugi_main))

wind.mainloop()
