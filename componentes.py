#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import sqlite3
import tkinter as tk
from tkinter import messagebox

# Base de datos
conn = sqlite3.connect("componentes.db")
cursor = conn.cursor()

# verificacion de existencia de la base y su correspondiente creacion en caso que no exista
# ~ Base de datos (campos):
# ~ Codigo (del componente)
# ~ Tipo (LED)
# ~ Subtipo (difuso, alto brillo, RGB, etc)
# ~ Valor (rojo, amarillo, ultravioleta, 220 ohm, 40pF)
# ~ Cantidad (20)
# ~ Gabeta (gabeta 1, 2, 33)
# ~ Descripcion (led comprado en ML)
# ~ Notas (este led viene bien para proyectos donde etc...)

try:
	cursor.execute(
		"CREATE TABLE inventario (codigo TEXT, tipo TEXT, subtipo TEXT, valor TEXT, cantidad INTEGER, gabeta TEXT, descripcion TEXT, notas TEXT);")
except sqlite3.OperationalError:
	pass # Base de datos abierta
else:
	print("Base creada con éxito")
	conn.commit()


# ventana principal
componentes = tk.Tk()
componentes.title("Inventario de componentes electrónicos")
componentes.config(width=500,height=400)



componentes.mainloop()
