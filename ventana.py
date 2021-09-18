import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from GraphDijkstra import GraphD
from GraphBellmanFord import GraphB

class ventana:
    def mostrar(self, event=None):
        self.labelNodoInicial.place(x=50,y=130)
        self.labelNodoFinal.place(x=50,y=170)
        self.labelPesoArista.place(x=50,y=210)
        self.nodoInicial.place(x=220, y=130)
        self.nodoFinal.place(x=220, y=170)
        self.pesoArista.place(x=220, y=210)
        self.botonEdge.place(x=380, y=210)

    def ocultar(self, event=None):
        self.labelNodoInicial.place_forget()
        self.labelNodoFinal.place_forget()
        self.labelPesoArista.place_forget()
        self.nodoInicial.place_forget()
        self.nodoFinal.place_forget()
        self.pesoArista.place_forget()
        self.botonEdge.place_forget()
    
    def crearGrafo(self):
        if self.nodos.get() == "" or self.aristas.get() == "":
            messagebox.showerror("Error", "La cantidad de nodos no puede ser vacia")
        else:
            self.contador = 0
            self.grafoD = GraphD(int(self.nodos.get()))
            self.grafoB = GraphB(int(self.nodos.get()))
            self.mostrar()

    def agregarArista(self):
        if self.nodoInicial.get() == "" or self.nodoFinal.get() == "" or self.pesoArista.get() == "":
            messagebox.showerror("Error", "Los campos no pueden estar vacios")
        else:
            a = int(self.nodoInicial.get())
            b = int(self.nodoFinal.get())
            c = int(self.pesoArista.get())
                
            self.grafoD.add_edge(a,b,c)
            self.grafoB.add_edge(a,b,c)
            
            self.contador += 1

            if self.contador == int(self.aristas.get()):
                self.ocultar()
                
            
    def __init__(self):   
        self.ventana = tk.Tk()
        self.ventana.geometry("500x500")

        labelNombre = tk.Label(self.ventana, text = "Proyecto final")
        labelNodos = tk.Label(self.ventana, text = "Inserte la cantidad de nodos")
        self.labelNodoInicial = tk.Label(self.ventana, text = "Nodo inicial")
        self.labelNodoFinal = tk.Label(self.ventana, text = "Nodo final")
        self.labelPesoArista = tk.Label(self.ventana, text = "Peso de la arista")
        self.labelAristas = tk.Label(self.ventana, text = "Digite la cantidad de aristas")
        labelNombre.place(x=200,y=10)
        labelNodos.place(x=50, y=50)
        self.labelAristas.place(x=50, y=90)

        validate_entry = lambda text: text.isdecimal()

        self.nodos  = ttk.Entry(self.ventana, validate="key",validatecommand=(self.ventana.register(validate_entry), "%S"))
        self.nodos.place(x=220,y=50)
        self.aristas  = ttk.Entry(self.ventana, validate="key",validatecommand=(self.ventana.register(validate_entry), "%S"))
        self.aristas.place(x=220,y=90)
        self.nodoInicial = ttk.Entry(self.ventana, validate="key", validatecommand=(self.ventana.register(validate_entry), "%S"))
        self.nodoFinal = ttk.Entry(self.ventana, validate="key", validatecommand=(self.ventana.register(validate_entry), "%S"))
        self.pesoArista = ttk.Entry(self.ventana, validate="key", validatecommand=(self.ventana.register(validate_entry), "%S"))

        self.boton = tk.Button(self.ventana, text = "Insertar nodos", command = self.crearGrafo)
        self.boton.place(x=380,y=50)
        self.botonEdge = tk.Button(self.ventana, text = "Insertar arista", command = self.agregarArista)


        

