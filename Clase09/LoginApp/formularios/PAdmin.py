import tkinter as tk
import json
from tkinter import messagebox, ttk
import webbrowser
import util.generic as utl
from formularios.Login import *
from formularios.FormUsuarios import *
class PAdmin(tk.Tk):
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        super().__init__()
        self.title("Panel Administrativo")
        self.resizable(False, False)
        # Obtener las dimensiones de la pantalla
        self.ancho_pantalla = self.winfo_screenwidth() #método para obtener Ancho
        self.alto_pantalla = self.winfo_screenheight() #método para obtener Alto

        # Establecer el tamaño completo de la ventana
        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")
        
        menubar = tk.Menu(self)  
        menuuser = tk.Menu(menubar, tearoff=0)  
        menuuser.add_command(label="Administracion de Usuarios", command=self.main_usuarios)  
        menubar.add_cascade(label="Usuarios", menu=menuuser)  

        menuclientes = tk.Menu(menubar, tearoff=0)
        menuclientes.add_command(label="Administracion de Cliente")  
        menubar.add_cascade(label="Clientes", menu=menuclientes)

        menucategorias = tk.Menu(menubar, tearoff=0)
        menucategorias.add_command(label="Administracion de Categorias")   
        menubar.add_cascade(label="Categorias", menu=menucategorias)   

        menuproducto = tk.Menu(menubar, tearoff=0)
        menuproducto.add_command(label="Administracion de Productos")    
        menubar.add_cascade(label="Productos", menu=menuproducto)

        menuventas = tk.Menu(menubar, tearoff=0)
        menuventas.add_command(label="Administracion de Ventas")  
        menubar.add_cascade(label="Ventas", menu=menuventas)

        self.config(menu=menubar)

        # frame user_info

        self.frame_user_info = tk.Frame(self, bd=0,relief=tk.SOLID, width=200)
        self.frame_user_info.pack(side=tk.LEFT, padx=4, pady=5,fill="y")
        texto=tk.Label(self.frame_user_info, text="PANEL ADMINISTRATIVO", font=('Times', 20))
        texto.pack(padx=20,pady=4)
        self.usrimg = utl.leer_imagen(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPOPROG2\Clase09\LoginApp\imagenes\userinfo.png", (128, 128))
        self.imgfacebook = utl.leer_imagen(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPOPROG2\Clase09\LoginApp\imagenes\face.png", (32, 32))
        self.imglinkedin = utl.leer_imagen(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPOPROG2\Clase09\LoginApp\imagenes\linkedin.png", (32, 32))
        self.imgwebsite = utl.leer_imagen(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPOPROG2\Clase09\LoginApp\imagenes\website.png", (32, 32))
        self.imglogout = utl.leer_imagen(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPOPROG2\Clase09\LoginApp\imagenes\logout.png", (32, 32))
        tk.Label(self.frame_user_info,image=self.usrimg).pack(padx=30,pady=4)
        tk.Label(self.frame_user_info, text=self.name, font=('Times', 14)).pack(padx=40,pady=4)
        tk.Label(self.frame_user_info, text=self.email, font=('Times', 14)).pack(padx=50,pady=4)
        tk.Button(self.frame_user_info,image=self.imgfacebook, command=self.abrirface).place(x=100,y=300)
        tk.Button(self.frame_user_info,image=self.imglinkedin, command=self.abrirlink).place(x=140,y=300)
        tk.Button(self.frame_user_info,image=self.imgwebsite, command=self.abrirweb).place(x=180,y=300)
        tk.Button(self.frame_user_info,image=self.imglogout, command=self.logout).place(x=220,y=300)
        
        #frame_data
        
        self.frame_data = tk.Frame(self, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)
        textobienvenida=tk.Label(self.frame_data, text="BIENVENIDO AL SISTEMA", font=('Times', 20))
        textobienvenida.pack(padx=20,pady=4)

        #frame_dinamyc
        self.frame_dinamyc = tk.Frame(self.frame_data, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_dinamyc.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)

    def main_usuarios(self):
        self.limpiar_panel(self.frame_dinamyc)
        FormUsuarios(self.frame_dinamyc)
        #self.formulario_usuario()
        #self.listar_usuarios()
    
    
    def limpiar_panel(self,panel):
    # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()
    def logout(self):
        self.destroy()

    def abrirface(self):
        url="https://www.facebook.com"
        webbrowser.open_new_tab(url)
    def abrirlink(self):
        url="https://www.linkedin.com"
        webbrowser.open_new_tab(url)
    def abrirweb(self):
        url= "https://itcloud.com.co"
        webbrowser.open_new_tab(url)        