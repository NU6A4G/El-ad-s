import tkinter as tk
from tkinter import simpledialog, messagebox


class AmobaJatek:
    def __init__(self, master):
        self.master = master
        self.master.title("Amőba Játék")

        self.jatekosok = self.jatekos_bekerese()
        self.aktualis_jatekos = 0

        self.tábla = [[" " for _ in range(3)] for _ in range(3)]

        self.statusz_label = tk.Label(self.master, text=f"{self.jatekosok[self.aktualis_jatekos]} következik",
                                      font=("Helvetica", 12))
        self.statusz_label.grid(row=3, column=0, columnspan=3)

        self.gombok_keszitese()

    def jatekos_bekerese(self):
        jatekosok = []
        for i in range(2):
            nev = simpledialog.askstring("Játékos neve", f"Add meg a(z) {i + 1}. játékos nevét:")
            if nev:
                jatekosok.append(nev)
            else:
                jatekosok.append(f"Játékos {i + 1}")
        return jatekosok

    def gombok_keszitese(self):
        for sor in range(3):
            for oszlop in range(3):
                gomb = tk.Button(self.master, text="", font=("Helvetica", 24), height=2, width=5,
                                 command=lambda s=sor, o=oszlop: self.kattintas(s, o))
                gomb.grid(row=sor, column=oszlop)

    def kattintas(self, sor, oszlop):
        if self.tábla[sor][oszlop] == " ":
            jel = "X" if self.aktualis_jatekos == 0 else "O"
            self.tábla[sor][oszlop] = jel
            self.frissites_gombok()

            if self.ellenorzes(jel):
                messagebox.showinfo("Győzelem!", f"{self.jatekosok[self.aktualis_jatekos]} győzött!")
                self.uj_jatek()
            elif self.ures_mezok() == 0:
                messagebox.showinfo("Döntetlen", "A játék döntetlen!")
                self.uj_jatek()
            else:
                self.aktualis_jatekos = 1 - self.aktualis_jatekos
                self.statusz_label.config(text=f"{self.jatekosok[self.aktualis_jatekos]} következik")

    def frissites_gombok(self):
        for sor in range(3):
            for oszlop in range(3):
                text = self.tábla[sor][oszlop]
                self.master.grid_slaves(row=sor, column=oszlop)[0]["text"] = text

    def ellenorzes(self, jel):
        for sor in self.tábla:
            if all(cell == jel for cell in sor):
                return True

        for oszlop in range(3):
            if all(self.tábla[i][oszlop] == jel for i in range(3)):
                return True

        if all(self.tábla[i][i] == jel for i in range(3)) or all(self.tábla[i][2 - i] == jel for i in range(3)):
            return True

        return False

    def ures_mezok(self):
        return sum(row.count(" ") for row in self.tábla)

    def uj_jatek(self):
        for sor in range(3):
            for oszlop in range(3):
                self.tábla[sor][oszlop] = " "
        self.aktualis_jatekos = 0
        self.frissites_gombok()
        self.statusz_label.config(text=f"{self.jatekosok[self.aktualis_jatekos]} következik")


if __name__ == "__main__":
    root = tk.Tk()
    app = AmobaJatek(root)
    root.mainloop()
