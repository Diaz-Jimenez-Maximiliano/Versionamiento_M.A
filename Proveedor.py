import tkinter as tk;
from tkinter import ttk;
from tkinter import messagebox;

def Abrir_Proovedor(inicio):
    # configurar el estilo ya sea color de las letra y fondo 
    style = ttk.Style()
    style.theme_use("default")
    
    inicio.withdraw()
    ventana_proovedor=tk.Toplevel()
    ventana_proovedor.title("Proovedor")
    ventana_proovedor.geometry("700x700")
    btn_regresar=tk.Button(ventana_proovedor,text="Regresar",command=lambda:regresar_inicio(ventana_proovedor,inicio))
    btn_regresar.pack(pady=10,padx=10)

    style.map("TNotebook.Tab",background=[("selected","#402CF3")],foregroud=[("selected","#FF0000")])#en el bg=[lo que se selecione mediante el click cambiara a un color por el momento es azul], fg=[intuitivamente marcara la ventana selecionada (<esto se aplica cunado son colores claros y fuerte>)]

    notebook=ttk. Notebook(ventana_proovedor)#Mostramos en que ventana se mostrara
    notebook.pack(padx=10,pady=10,fill='both',expand=True)
    frame1=ttk.Frame(notebook,padding="10",style="TFrame")#La creaacion de ventanas estos pueden depender para que usarlos
    frame2=ttk.Frame(notebook,padding="10",style="TFrame")
    frame3=ttk.Frame(notebook,padding="10",style="TFrame")

    notebook.add(frame1,text="Mesanjes de pedidos")#El enunciado que va a decir la ventana
    notebook.add(frame2,text="Productos")
    notebook.add(frame3,text="Pedidos entregados y cancelados")

    etiqueta=tk.Label(frame1,text="Mesjage")#en este caso le vamos a pedir que lo muestre en la ventana <frame1>
    etiqueta.pack(pady=15)#Y esto va aplicar para el contenido que vamos a mostrar
    lista=tk.Listbox(frame1,font=("Arial",14),width=50,fg="#00715A",bg="#FFFFFF")#Una Lsita 
    lista.pack(pady=10)
    lista.insert(1,"Mensaje 1")#Insertar texto
    lista.insert(2,"Mensaje 2")
    lista.insert(3,"Mensaje 3")
    lista.insert(5,"Mensaje 5")
    lista.insert(6,"Mensaje 6")

    etiqueta=tk.Label(frame2,text="Tardes")
    etiqueta.pack(pady=20)

    etiqueta=tk.Label(frame3,text="Noches")
    etiqueta.pack(pady=20)
def regresar_inicio(inicio,ventana_proovedor):
    inicio.destroy()
    ventana_proovedor.deiconify()
def main():      
    inicio=tk.Tk()
    inicio.title("inicio")
    inicio.geometry("400x400")
    btn_is=tk.Button(inicio,text="Iniciar sesion",command=lambda:Abrir_Proovedor(inicio),font=("Arial",14))
    btn_is.pack(pady=10)
    btn_cont=tk.Button(inicio,text="Contactos",command=lambda:Abrir_Proovedor(inicio),font=("Arial",14))
    btn_cont.pack(pady=10)
    inicio.mainloop()
if __name__=="__main__":
    main()