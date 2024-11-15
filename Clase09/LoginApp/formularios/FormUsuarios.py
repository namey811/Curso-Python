import tkinter as tk
import json
from tkinter import messagebox, ttk
import webbrowser
import util.generic as utl
from formularios.Login import *
class FormUsuarios(tk.Tk):
    def __init__(self, parent):
            self.tipo_action ="Guardar"
            self.tipo_user = ""
            self.frame = ttk.Frame(parent)
            self.frame.pack(fill="both", expand=True, padx=20, pady=20)

            labelform = tk.Label(self.frame,text="\uf0c9 REGISTRO DE USUARIOS", font=('Times',16),fg="#9fa8da")
            labelform.place(x=70, y=30)
            
            labelcedula = tk.Label(self.frame,text="Cedula:", font=('Times',14))
            labelcedula.place(x=70, y=100)
            self.ccedula = tk.Entry(self.frame, width=40)
            self.ccedula.place(x=220, y=100)

            labelnombre = tk.Label(self.frame,text="Nombre completo:", font=('Times',14))
            labelnombre.place(x=70, y=130)
            self.cnombre = tk.Entry(self.frame, width=40)
            self.cnombre.place(x=220, y=130)

            labelusuario = tk.Label(self.frame,text="Username:", font=('Times',14))
            labelusuario.place(x=70,y=160)
            self.cusuario = tk.Entry(self.frame, width=40)
            self.cusuario.place(x=220,y=160)

            labelclave = tk.Label(self.frame,text="Contraseña:", font=('Times',14))
            labelclave.place(x=500,y=100)
            self.cclave = tk.Entry(self.frame, width=40, show="*")
            self.cclave.place(x=600, y=130)

            labelcorreo = tk.Label(self.frame,text="Correo:", font=('Times',14))
            labelcorreo.place(x=500,y=160)
            self.ccorreo = tk.Entry(self.frame, width=40)
            self.ccorreo.place(x=600, y=160)

            labeltipo = tk.Label(self.frame, text="Rol:", font=('Times',14))
            labeltipo.place(x=500,y=160)
            self.listatipo = tk.Listbox(self.frame, selectmode="Single", width=40, height=2)
            self.listatipo.place(x=600,y=160)
            self.listatipo.insert(1, "Administrador")
            self.listatipo.insert(2, "Vendedor")

            btnguardar = tk.Button(self.frame, text="\uf0c7 GUARDAR", font=('Times',14), command=self.save_user)
            btnguardar.place(x=870, y=130)

            self.listar_usuarios()

    def listar_usuarios(self):

        tk.Label(self.frame,text="\uf00b LISTADO DE USUARIOS", font=('Times',16),fg="#9fa8da").place(x=70, y=200)
        self.tablausuarios = ttk.Treeview(self.frame, columns=("NombreCompleto", "Username", "Email", "Rol"))
        self.tablausuarios.heading("#0", text="Cedula")
        self.tablausuarios.heading("NombreCompleto", text="Nombre Completo")
        self.tablausuarios.heading("Username", text="Usuario")
        self.tablausuarios.heading("Email", text="Email")
        self.tablausuarios.heading("Rol", text="Rol")
        with open(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPOPROG2\Clase09\LoginApp\db_users.json", "r", encoding='utf-8') as self.file:
                self.db_users = json.load(self.file)
                for usuarios in self.db_users["users"]:
                    self.tablausuarios.insert("", "end", text=f'{usuarios["id"]}',values=(f'{usuarios["name"]}',f'{usuarios["username"]}',f'{usuarios["email"]}', f'{usuarios["role"]}'))
        self.tablausuarios.place(x=70, y=250)
        btneliminar = tk.Button(self.frame, text="\uf0c7 Eliminar", font=('Times',14), command=self.delete_user)
        btneliminar.place(x=70, y=520)
        btnupdate = tk.Button(self.frame, text="\uf0c7 Actualizar", font=('Times',14), command=self.update_user)
        btnupdate.place(x=200, y=520)

    def save_user(self):
        for index in self.listatipo.curselection():
            self.tipo_user = self.listatipo.get(index)
        if self.ccedula.get() =="" or self.cnombre.get() == "" or self.cusuario.get() == "" or self.ccorreo.get() == "" or self.cclave.get() == "" or self.tipo_user == "":
            messagebox.showinfo('Info',"Debe llenar todos los campos",parent=self.frame)
            return 
        else:
                with open(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPOPROG2\Clase09\LoginApp\db_users.json", "r", encoding='utf-8') as self.file:
                        self.db_users = json.load(self.file)

                        if self.tipo_action == "Actualizar":

                            for usuarios in self.db_users["users"]:
                                if usuarios["id"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                                    usuarios["name"] = self.cnombre.get()
                                    usuarios["username"] = self.cusuario.get()
                                    usuarios["password"] =  self.cclave.get()
                                    usuarios["email"] = self.ccorreo.get()
                                    usuarios["role"] = self.tipo_user
                                    with open(r'D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPOPROG2\Clase09\LoginApp\db_users.json', 'w') as jf: 
                                        json.dump(self.db_users, jf, indent=4, ensure_ascii=True)
                                        messagebox.showinfo('Info',"Usuario actualizado con exito",parent=self.frame)
                                        self.limpiar_panel(self.frame)
                    
                        else:
                            self.db_users["users"].append({
                                            'id': self.ccedula.get(),
                                            'name': self.cnombre.get(),
                                            'username': self.cusuario.get(),
                                            'password': self.cclave.get(),
                                            'email': self.ccorreo.get(),
                                            'role':self.tipo_user
                                            })
                            with open(r'D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPOPROG2\Clase09\LoginApp\db_users.json', 'w') as jf: 
                                json.dump(self.db_users, jf, indent=4, ensure_ascii=True)
                                messagebox.showinfo('Info',"Usuario registrado con exito",parent=self.frame)
                                self.limpiar_panel(self.frame) 
                                self.listar_usuarios()


    def delete_user(self):
        with open(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPOPROG2\Clase09\LoginApp\db_users.json", "r", encoding='utf-8') as self.file:
                self.db_users = json.load(self.file)
                for usuarios in self.db_users["users"]:
                    if usuarios["id"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.db_users["users"].remove(usuarios)
                        with open(r'D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPOPROG2\Clase09\LoginApp\db_users.json', 'w') as jf:
                            json.dump(self.db_users, jf, indent=4, ensure_ascii=True)
                            messagebox.showinfo('Info',"Usuario eliminado con exito",parent=self.frame)
                            self.limpiar_panel(self.frame)
                            break



    def update_user(self):
        with open(r"D:\_EMPRESARIAL\_TECNAR\CLASES\PROGRAMACION\REPOPROG2\Clase09\LoginApp\db_users.json", "r", encoding='utf-8') as self.file:
                self.db_users = json.load(self.file)
                for usuarios in self.db_users["users"]:
                    if usuarios["id"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.ccedula.delete(0, tk.END)
                        self.ccedula.insert(0, usuarios["id"])
                        self.ccedula.config(state="disabled")
                        self.cnombre.delete(0, tk.END)
                        self.cnombre.insert(0,usuarios["name"])
                        self.cusuario.delete(0, tk.END)
                        self.cusuario.insert(0,usuarios["username"])
                        self.cclave.delete(0, tk.END)
                        self.cclave.insert(0,usuarios["password"])
                        self.ccorreo.delete(0, tk.END)
                        self.ccorreo.insert(0,usuarios["email"])
                        self.tipo_action = "Actualizar"

    def limpiar_panel(self,panel):
    # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()