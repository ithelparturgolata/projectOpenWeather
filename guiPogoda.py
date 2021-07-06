# pip install pep8
# pip install pycodestyle
# pep8 --first guiPogoda.py
# pycodestyle --first dk_modraczek.py
# coding: utf-8
from tkinter import *
import tkinter as tk
from datetime import datetime
import requests
from tkinter import messagebox


class Weather():
    """
    Klasa Weather, prosta aplikacja do sprawdzania pogody
    zawiera dwie metody:
    report - pobieranie danych
    clear - czyszczenie pola szukaj
    """

    def report(self):
        """
        Metoda pobierania danych ze strony OpenWeather
        Własne API
        JSON
        pobiera pogodę, temperaturę, wilgotność, ciśnienie
        angielskie nazewnictwo wynika z dokumentacji
        """
        self.url = "http://api.openweathermap.org/data/2.5/weather?q="
        self.cityname = self.loc.get(1.0, END)
        self.api_key = "2213901a0c8514848e49f8c2433e97c9"
        self.data = requests.get(self.url + self.cityname +
                                 '&appid=' + self.api_key).json()

        if self.data["cod"] == "404":
            messagebox.showwarning("Błąd",
                                   "Wpisz nazwę miasta "
                                   "bez znaków diakretycznych")
        else:
            self.location["text"] = self.data["name"] \
                                    + "," + self.data["sys"]["country"]
            self.c = int(self.data["main"]["temp_max"] - 273.15)
            self.weather["text"] = self.data["weather"][0]["main"]
            self.weather["font"] = ("verdana", 10, "bold")
            self.temperature["text"] = f"{self.c}°C \n"
            self.temperature["font"] = ("verdana", 10, "bold")
            self.humidity["text"] = self.data["main"]["humidity"]
            self.humidity["font"] = ("verdana", 10, "bold")
            self.pressure["text"] = self.data["main"]["pressure"]
            self.pressure["font"] = ("verdana", 10, "bold")

    def clear(self):
        """
        metoda czyszczenia
        """
        self.loc.delete("1.0", END)

    def __init__(self):
        """
        Kontstruktor oraz budowa GUI
        """
        self.root = tk.Tk()
        self.root.geometry("550x400")
        self.root.title("Pogoda")
        self.root.resizable(0, 0)
        self.font = ("verdana", 10, "bold")

        self.header = Label(self.root, width=100, height=2, bg="#666699")
        self.header.place(x=0, y=0)

        self.date = Label(self.root, text=datetime.now().date(),
                          bg="#666699", fg="#FFFFFF", font=self.font)
        self.date.place(x=400, y=5)

        self.heading = Label(self.root, text="Aktualna pogoda",
                             bg="#666699", fg="#FFFFFF", font=self.font)
        self.heading.place(x=180, y=5)

        self.location = Label(self.root, text="Miasto",
                              bg="#666699", fg="#FFFFFF", font=self.font)
        self.location.place(x=10, y=5)

        self.name = Label(self.root, text="Wpisz miasto",
                          fg="#000000", font=self.font)
        self.name.place(x=140, y=45)

        self.loc = Text(self.root, width=25, height=1)
        self.loc.place(x=140, y=70)

        self.button = Button(self.root, text="Szukaj",
                             bg="#666699", fg="white", relief=RAISED,
                             command=self.report, font=self.font)
        self.button.place(x=350, y=65)

        self.button1 = Button(self.root, text="Wyczyść",
                              bg="#666699", fg="white", relief=RAISED,
                              command=self.clear,
                              font=self.font)
        self.button1.place(x=420, y=65)

        self.report = Label(self.root, text="Raport pogodowy",
                            bg="#666699", fg="#FFFFFF",
                            font=self.font, padx=10)
        self.report.place(x=180, y=120)

        self.report2 = Label(self.root, text="Warunki: ",
                             bg="#666699", fg="#FFFFFF",
                             font=self.font, padx=10)
        self.report2.place(x=50, y=160)

        self.report3 = Label(self.root, text="Temperatura: ",
                             bg="#666699", fg="#FFFFFF",
                             font=self.font, padx=10)
        self.report3.place(x=50, y=200)

        self.report4 = Label(self.root, text="Wilgotność: ",
                             bg="#666699", fg="#FFFFFF",
                             font=self.font, padx=10)
        self.report4.place(x=50, y=240)

        self.report5 = Label(self.root, text="Ciśnienie: ",
                             bg="#666699", fg="#FFFFFF",
                             font=self.font, padx=10)
        self.report5.place(x=50, y=280)

        self.weather = Label(self.root, text="???",
                             fg="#00274c", font=self.font)
        self.weather.place(x=200, y=160)

        self.temperature = Label(self.root, text="???",
                                 fg="#00274c", font=self.font)
        self.temperature.place(x=200, y=200)

        self.humidity = Label(self.root, text="??? ",
                              fg="#00274c", font=self.font)
        self.humidity.place(x=200, y=240)
        self.humidity2 = Label(self.root, text="%",
                               fg="#00274c", font=self.font)
        self.humidity2.place(x=240, y=240)

        self.pressure = Label(self.root, text="???",
                              fg="#00274c", font=self.font)
        self.pressure.place(x=200, y=280)

        self.pressure2 = Label(self.root, text="hPa",
                               fg="#00274c", font=self.font)
        self.pressure2.place(x=240, y=280)

        self.root.mainloop()


if __name__ == '__main__':
    Weather()
