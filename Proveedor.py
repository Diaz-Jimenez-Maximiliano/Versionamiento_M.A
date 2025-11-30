import tkinter as tk;
from tkinter import ttk;
from tkinter import messagebox;
from PIL import ImageTk, Image;
#--Contactos--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def login(inicio):
    #inicio.withdraw()
    iniciar_sesion = tk.Toplevel()
    iniciar_sesion.title("Iniciar sesión")
    iniciar_sesion.geometry("400x300")

    tk.Label(iniciar_sesion, text="Usuario").pack(pady=10)
    us = tk.Entry(iniciar_sesion, width=20)
    us.pack(pady=5)

    tk.Label(iniciar_sesion, text="Contraseña").pack(pady=10)
    c = tk.Entry(iniciar_sesion, width=20, show="*")
    c.pack(padx=5)

    def iniciar():
        usuario = us.get()
        contraseña = c.get()
        if usuario == "hector" and contraseña == "2008":
            iniciar_sesion.destroy()
            Arbir_jefe(inicio)
        elif usuario == "cbtisfs1001" and contraseña == "010909":
            # Abrir ventana proveedor directamente
            iniciar_sesion.destroy()
            Abrir_Proovedor(inicio)
        elif usuario=="nataly" and contraseña=="2009":
            messagebox.showinfo("Empleada", f"Hola {usuario}")
        elif usuario=="ibrahim" and contraseña=="2009":
            messagebox.showinfo("Ususario Final", f"Hola {usuario}")
        else:
            tk.Label(iniciar_sesion, text="Usuario o contraseña incorrecta").pack(pady=10)
            us.delete(0, tk.END)
            c.delete(0, tk.END)

    tk.Button(iniciar_sesion, text="Continuar", font=("Times New Roman", 14), command=iniciar).pack(pady=10)
    tk.Button(iniciar_sesion, text="Cancelar o volver", font=("Time New Roman", 14),
              command=lambda: regresar_inicio(inicio, iniciar_sesion)).pack(padx=10)

    tk.Label(iniciar_sesion, text="© Derechos Reservados - Guitarras Puebla",
             bg="#dac9ad", font=("Arial", 10), fg="black").pack(side="bottom", fill="x")

def regresar_inicio(inicio, ventana):
    ventana.destroy()
    inicio.deiconify()
#--Contactos--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def contactos(inicio):
    #inicio.withdraw()
    ventana_contacto=tk.Toplevel()
    ventana_contacto.title("Contactos")
    ventana_contacto.geometry("500x500")
    
    header = tk.Frame(ventana_contacto, bg="#775516", height=80)
    header.pack(fill="x")
    tk.Label(header, text="Mi Página Web", font=("Arial", 24, "bold"), fg="white", bg="#756542").place(relx=0.5, rely=0.5, anchor="center")

    etiqueta=tk.Label(ventana_contacto,text="Nombre: Maximiliano Diaz Jiménez\nNumero: 2224242958\nCorreo Electronico: cbtisfs1001@gmail.com\nUbicación: N/A")
    etiqueta.pack(pady=10)
    footer = tk.Label(ventana_contacto,text="© Derechos Reservados - Guitarras Puebla", bg="#dac9ad",font=("Arial", 10),fg="black")
    footer.pack(side="bottom", fill="x") # Pie de página
def regresar_inicio(inicio,ventana_contacto):
    ventana_contacto.destroy()
    inicio.deiconify()
#--Perfil--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def perfil(inicio):
    #inicio.withdraw()
    ventana_perfil=tk.Toplevel()
    ventana_perfil.title("Perfil")
    ventana_perfil.geometry("500x500")
    ventana_perfil.configure(bg="#80431D")
    header = tk.Frame(ventana_perfil, bg="#775516", height=80)
    header.pack(fill="x")
    tk.Label(header, text="Mi Página Web", font=("Arial", 24, "bold"), fg="white", bg="#756542").place(relx=0.5, rely=0.5, anchor="center")
    etiqueta=tk.Label(ventana_perfil,text="Nombre: Maximiliano Diaz Jimenéz\nNumero: 2224242958\nCorreo Elctronico: cbtisfs1001@gmail.com\nUbicacion: N/A")
    etiqueta.pack(pady=10)

    footer = tk.Label(ventana_perfil,text="© Derechos Reservados - Guitarras Puebla", bg="#dac9ad",font=("Arial", 10),fg="black")
    footer.pack(side="bottom", fill="x") # Pie de página
def regresar_inicio(inicio,ventana_perfil):
    ventana_perfil.destroy()
    inicio.deiconify()
#--Jefe--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Arbir_jefe():
    menu = tk.Tk()
    menu.title("Panel Principal - Guitarras Puebla")
    menu.geometry("400x400")
    menu.configure(bg="#cfcfcf")  # Gris neutro
    
    tk.Label(menu, text="Bienvenido al panel principal", bg="#cfcfcf", font=("Arial", 14)).pack(pady=20) 
#--proveedor--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Abrir_Proovedor(inicio):
    style = ttk.Style()
    style.theme_use("default")

    ventana_proveedor = tk.Toplevel()
    ventana_proveedor.title("Proveedor")
    ventana_proveedor.geometry("700x700")

    tk.Button(ventana_proveedor, text="Regresar", command=lambda: regresar_inicio(inicio, ventana_proveedor)).pack(pady=10, padx=10)

    style.map("TNotebook.Tab", background=[("selected", "#402CF3")], foreground=[("selected", "#FF0000")])

    notebook = ttk.Notebook(ventana_proveedor)
    notebook.pack(padx=10, pady=10, fill='both', expand=True)

    frame1 = ttk.Frame(notebook, padding="10")
    frame2 = ttk.Frame(notebook, padding="10")
    frame3 = ttk.Frame(notebook, padding="10")

    notebook.add(frame1, text="Mensajes de pedidos")
    notebook.add(frame2, text="Productos")
    notebook.add(frame3, text="Pedidos entregados y cancelados")

    tk.Label(frame1, text="Mensajes").pack(pady=15)
    lista = tk.Listbox(frame1, font=("Arial", 14), width=50, fg="#00715A", bg="#FFFFFF")
    lista.pack(pady=10)
    for i in range(1, 7):
        lista.insert(i, f"Mensaje {i}")

    tk.Label(frame2, text="Tardes").pack(pady=20)
    tk.Label(frame3, text="Noches").pack(pady=20)

    tk.Label(ventana_proveedor, text="© Derechos Reservados - Guitarras Puebla",
             bg="#dac9ad", font=("Arial", 10), fg="black").pack(side="bottom", fill="x")

#--Hamburgesa--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#--Inicio--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def main():
    inicio = tk.Tk()
    inicio.title("Menú Hamburguesa Animado")
    inicio.geometry("1000x700")
    inicio.configure(bg="#ffffff")
    #header
    header = tk.Frame(inicio, bg="#775516", height=80)
    header.pack(fill="x")
    tk.Label(header, text="Mi Página Web", font=("Arial", 24, "bold"), fg="white", bg="#756542").place(relx=0.5, rely=0.5, anchor="center")

    imagen =Image.open("trabajo_final\logo_oficial.jpeg")
    imagen_pil=imagen.resize((60,60))
    imagen_tk = ImageTk.PhotoImage(imagen_pil)
    label_con_imagen = tk.Label(inicio, image=imagen_tk)
    label_con_imagen.image = imagen_tk 
    label_con_imagen.place(x=130,y=10)

    menu_abierto = False
    menu_frame = tk.Frame(inicio, width=150, height=1000, bg="#00ccff")
    menu_frame.place(x=-150, y=0)

    btn_menu = tk.Button(inicio, text="≡", font=("Times New Roman", 28, "bold"),
                         background="#FFFFFF", foreground="#245861")
    btn_menu.place(x=10, y=10)

    def animar_abrir(x_actual):
        if x_actual < 0:
            x_actual += 10
            menu_frame.place(x=x_actual, y=0)
            inicio.after(10, lambda: animar_abrir(x_actual))
        else:
            menu_frame.place(x=0, y=0)

    def animar_cerrar(x_actual):
        if x_actual > -150:
            x_actual -= 10
            menu_frame.place(x=x_actual, y=0)
            inicio.after(10, lambda: animar_cerrar(x_actual))
        else:
            menu_frame.place(x=-150, y=0)

    def abrir_menu():
        nonlocal menu_abierto
        if not menu_abierto:
            menu_abierto = True
            btn_menu.place_forget()
            animar_abrir(-150)

    def cerrar_menu():
        nonlocal menu_abierto
        if menu_abierto:
            menu_abierto = False
            animar_cerrar(0)
            btn_menu.place(x=10, y=10)

    btn_cerrar = tk.Button(menu_frame, text="X", font=("Arial", 14), bg="white", command=cerrar_menu)
    btn_cerrar.place(x=110, y=10)

    tk.Button(menu_frame, text="Login", command=lambda: login(inicio)).place(x=20, y=60)
    tk.Button(menu_frame, text="Contactos", command=lambda: contactos(inicio)).place(x=20, y=100)
    tk.Button(menu_frame, text="Perfil", command=lambda: perfil(inicio)).place(x=20, y=140)

    btn_menu.config(command=abrir_menu)

    tk.Label(inicio, text="© Derechos Reservados - Guitarras Puebla",
             bg="#dac9ad", font=("Arial", 10), fg="black").pack(side="bottom", fill="x")

    inicio.mainloop()
    
if __name__ == "__main__":
    main()

