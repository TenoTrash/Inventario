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
	lista1.delete(0,tk.END)
	for codigo, tipo, subtipo, valor, cantidad, gaveta, desc, notas in inventario:
		# renglon=item[0]+" - "+item[1]+" - "+item[2]+" - "+item[3]+" - "+item[4]+" - "+item[5]+" - "+item[6]+" - "+item[7],
		# lista1.insert(tk.END,item[::])
		renglon=codigo+" - "+tipo+" - "+subtipo+" - "+valor+" - "+cantidad+" - "+gaveta+" - "+desc+" - "+notas
		lista1.insert(tk.END,renglon)

def agregar():
	cursor.execute(	"INSERT INTO inventario VALUES (?,?,?,?,?,?,?,?)",(caja_codigo.get(),caja_tipo.get(),caja_subtipo.get(),caja_valor.get(),caja_cantidad.get(),caja_gaveta.get(),caja_desc.get(),caja_notas.get()))
	conn.commit()

def salir():
	exit()

try:
	cursor.execute(
		"CREATE TABLE inventario (codigo TEXT, tipo TEXT, subtipo TEXT, valor TEXT, cantidad TEXT, gaveta TEXT, descripcion TEXT, notas TEXT);")
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

# listado principal
lista1 = tk.Listbox()
lista1.place(x=5,y=120,width=790,height=375)

boton_listar = tk.Button(text="Listar", command=listar)
boton_listar.place(x=755, y=5,width=35, height=25) #Si no pongo tamaño, lo toma por largo de texto

boton_salir = tk.Button(text="Salir", command=salir)
boton_salir.place(x=755, y=45,width=35, height=25) #Si no pongo tamaño, lo toma por largo de texto

etiqueta_codigo = tk.Label(text="Código:", fg="#ffffff",bg="#00ff00")
etiqueta_codigo.place(x=5, y=5)
caja_codigo = tk.Entry()
caja_codigo.place(x=5, y=25, width=100, height=25)

etiqueta_tipo = tk.Label(text="Tipo:", fg="#ffffff",bg="#00ff00")
etiqueta_tipo.place(x=110, y=5)
caja_tipo = tk.Entry()
caja_tipo.place(x=110, y=25, width=100, height=25)

etiqueta_subtipo = tk.Label(text="Subtipo:", fg="#ffffff",bg="#00ff00")
etiqueta_subtipo.place(x=215, y=5)
caja_subtipo = tk.Entry()
caja_subtipo.place(x=215, y=25, width=100, height=25)

etiqueta_valor = tk.Label(text="Valor:", fg="#ffffff",bg="#00ff00")
etiqueta_valor.place(x=320, y=5)
caja_valor = tk.Entry()
caja_valor.place(x=320, y=25, width=100, height=25)

etiqueta_cantidad = tk.Label(text="Cantidad:", fg="#ffffff",bg="#00ff00")
etiqueta_cantidad.place(x=425, y=5)
caja_cantidad = tk.Entry()
caja_cantidad.place(x=425, y=25, width=100, height=25)

etiqueta_gaveta = tk.Label(text="Gaveta:", fg="#ffffff",bg="#00ff00")
etiqueta_gaveta.place(x=530, y=5)
caja_gaveta = tk.Entry()
caja_gaveta.place(x=530, y=25, width=100, height=25)

etiqueta_desc = tk.Label(text="Descripción:", fg="#ffffff",bg="#00ff00")
etiqueta_desc.place(x=5, y=65)
caja_desc = tk.Entry()
caja_desc.place(x=5, y=85, width=205, height=25)

etiqueta_notas = tk.Label(text="Notas:", fg="#ffffff",bg="#00ff00")
etiqueta_notas.place(x=215, y=65)
caja_notas = tk.Entry()
caja_notas.place(x=215, y=85, width=415, height=25)

boton_agregar = tk.Button(text="Agregar", command=agregar)
boton_agregar.place(x=735, y=90,width=55, height=25) #Si no pongo tamaño, lo toma por largo de texto

componentes.mainloop()
