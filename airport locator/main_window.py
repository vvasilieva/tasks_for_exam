"""Модуль класса главного окна."""

from tkinter import *
from tkintermapview import TkinterMapView

from auto_combobox import AutocompleteCombobox
from read_data import read_file


class MainWindow:
    """Класс главного окна."""

    def __init__(self):
        """Конструктор."""
        self.window = Tk()
        self.window.title("Airport Locator")
        self.window.geometry('800x600')
        self.window.resizable(width=0, height=0)
        self.window.iconphoto(False, PhotoImage(file='airplane.png'))

        self.countries = read_file('airports.json')

        self.btn = Button(self.window, text="Loading Maps", bg="red", fg="white", font=("Arial Bold", 10), command=self.clicked)
        self.btn.grid(column=2, row=0)

        self.combo_country = AutocompleteCombobox(self.window)
        self.combo_country.set_completion_list(self.countries)
        self.combo_country.current(0)
        self.combo_country.focus_set()
        self.combo_country.grid(column=0, row=0)
        self.combo_country.bind('<<ComboboxSelected>>', self.country_selected)
        self.combo_country.bind('<Return>', self.country_selected)

        self.combo_city = AutocompleteCombobox(self.window)
        self.combo_city.set_completion_list(self.countries[self.combo_country.get()])
        self.combo_city.current(0)
        self.combo_city.grid(column=1, row=0)
        self.combo_city.bind('<Return>', self.enter_clicked)

        self.text = Text(self.window, width=100, height=100)
        self.text.grid(row=1, column=0, columnspan=3)
        self.text.insert(1.0, "\n\nВыберите страну,\n\nгород с аэропортом\n\n и запустите процесс.\n\n Поехали;)")
        self.text.tag_add('title', 1.0, 'end')
        self.text.tag_config('title', justify=CENTER, font=("Verdana", 24, 'bold'))
        self.text.config(state=DISABLED)

    def clicked(self):
        """Функция обработки нажатия на загрузку карты."""
        if self.text.winfo_exists():
            self.text.grid_remove()
            self.map_widget = TkinterMapView(self.window, width=800, height=600, corner_radius=0)
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
            self.map_widget.set_address("{0} {1}".format(self.combo_city.get(), self.combo_country.get()), marker=True)
            self.map_widget.grid(row=1, column=0, columnspan=3, sticky=N + S + E + W)
        else:
            self.map_widget.set_address("{0} {1}".format(self.combo_city.get(), self.combo_country.get()), marker=True)

    def country_selected(self, event):
        """Обработчик выбора страны в комбобоксе."""
        self.combo_city.set_completion_list(self.countries[self.combo_country.get()])
        self.combo_city.current(0)

    def enter_clicked(self, event):
        """Обработчик нажатия на Enter после ввода названия города."""
        self.clicked()

    def mainloop(self):
        """Запуск главного цикла обработки событий."""
        self.window.mainloop()
