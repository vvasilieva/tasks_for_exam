"""Модуль класса автозаполнения комбобокса."""

import tkinter
from tkinter.ttk import Combobox


class AutocompleteCombobox(Combobox):
    """Класс автозаполнения комбобокса."""

    def __init__(self, parent=None):
        """Конструктор."""
        super().__init__(parent)
        self._completion_list = []
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)

    def set_completion_list(self, completion_list):
        """Заполнение значений Combobox."""
        self._completion_list = sorted(completion_list, key=str.lower)
        self['values'] = self._completion_list

    def autocomplete(self, delta=0):
        """Автозаполнение."""
        if delta:
            self.delete(self.position, tkinter.END)
        else:
            self.position = len(self.get())
        _hits = []
        for element in self._completion_list:
            if element.lower().startswith(self.get().lower()):
                _hits.append(element)
        if _hits != self._hits:
            self._hit_index = 0
            self._hits = _hits
        if _hits == self._hits and self._hits:
            self._hit_index = (self._hit_index + delta) % len(self._hits)
        if self._hits:
            self.delete(0, tkinter.END)
            self.insert(0, self._hits[self._hit_index])
            self.select_range(self.position, tkinter.END)

    def handle_keyrelease(self, event):
        """Обработчик нажатия на клавишу клавиатуры."""
        if event.keysym == "BackSpace":
            self.delete(self.index(tkinter.INSERT), tkinter.END)
            self.position = self.index(tkinter.END)
        if event.keysym == "Left":
            if self.position < self.index(tkinter.END):
                self.delete(self.position, tkinter.END)
            else:
                self.position = self.position - 1
                self.delete(self.position, tkinter.END)
        if event.keysym == "Right":
            self.position = self.index(tkinter.END)
        if len(event.keysym) == 1:
            self.autocomplete()
