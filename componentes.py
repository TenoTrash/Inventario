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
# ~ (codigo, tipo, subtipo, valor, cantidad, gabeta, descripcion, notas)
# ~  TEXT    TEXT  TEXT     TEXT   TEXT      TEXT    TEXT         TEXT
# ~ # insertar un dato

# cursor.execute("INSERT INTO inventario VALUES('LED1','Led','Difuso','Rojo','30','Trasp1','Led difuso rojo','Comprados en ELab Shop')")
# cursor.execute("INSERT INTO inventario VALUES('LED2','Led','Difuso','Verde','30','Trasp1','Led difuso verde','Comprados en ELab Shop')")
# cursor.execute("INSERT INTO inventario VALUES('LED3','Led','Difuso','Amarillo','30','Trasp1','Led difuso amarillo','Comprados en ELab Shop')")
# cursor.execute("INSERT INTO inventario VALUES('RES220','Resistor','Comun','220 ohm','30','Trasp1','Resistor 220 ohm','Para proyecto de leds')")
# conn.commit()

def listar():
	for codigo, tipo, subtipo, valor, cantidad, gabeta, desc, notas in inventario:
		# renglon=item[0]+" - "+item[1]+" - "+item[2]+" - "+item[3]+" - "+item[4]+" - "+item[5]+" - "+item[6]+" - "+item[7],
		# lista1.insert(tk.END,item[::])
		renglon=codigo+" - "+tipo+" - "+subtipo+" - "+valor+" - "+cantidad+" - "+gabeta+" - "+desc+" - "+notas
		lista1.insert(tk.END,renglon)


try:
	cursor.execute(
		"CREATE TABLE inventario (codigo TEXT, tipo TEXT, subtipo TEXT, valor TEXT, cantidad TEXT, gabeta TEXT, descripcion TEXT, notas TEXT);")
except sqlite3.OperationalError:
	pass # Base de datos abierta
else:
	print("Base creada con éxito")
	conn.commit()

cursor.execute("SELECT * FROM inventario")
inventario = cursor.fetchall()

# ventana principal
componentes = tk.Tk()
componentes.title("Inventario de componentes electrónicos")
componentes.config(width=800,height=500)

lista1 = tk.Listbox()
lista1.place(x=20,y=100,width=760,height=380)
listar()

componentes.mainloop()
