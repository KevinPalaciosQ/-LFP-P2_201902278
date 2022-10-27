from ast import Delete
import tkinter
from tkinter import *
from tkinter import font 
from tkinter import ttk,  scrolledtext
import tkinter as ttk
from tkinter import filedialog
from tkinter import messagebox 
import tkinter as tk
from tkinter import ttk
from click import command
import pyautogui as pt 
import webbrowser as wb
from AnalizadorLexico import *
from AnalizadorPrueba import *
from ReporteTokens import *
from ReporteErrores import *
from Analizador3 import *
ventanaprincipal = None
textbox = None
RutaArchivo=None
lblespacio = None
VentanaAyuda=None
lblposicionx=None
lblposiciony=None
ruta=None
hola = ""
def ManualTecnico():
    wb.open_new(r"C:\Users\kevin\OneDrive\Documentos\-LFP-P2_201902278\Documentacion\ManualTecnicoProyecto2.pdf")
def ManualDeUsuario():
    wb.open_new(r"C:\Users\kevin\OneDrive\Documentos\-LFP-P2_201902278\Documentacion\ManualUsuarioProyecto2.pdf")
def posiciones():
    global x,y

    global textbox
    global lblposicionx
    global lblposiciony
    while True:
        x , y= pt.position()
        lblposicionx.configure(text=+x)
        lblposiciony.configure(text=+y)
def Ejecutar():
    global hola
    hola=analizador_lexico()
    hola.analizar(textbox.get(1.0, END))
    hola.impresion()
def Tokens():
    global hola
    try:
        GenerarArchivoDeTokens(hola.ListaTokens)
        messagebox.showinfo("Succes","Se Generó el Reporte de Tokens")
    except:
        messagebox.showwarning("Advertencia","No se pudo Generar el Reporte de Tokens, por favor analice el Archivo")
def Errores():
    global hola
    try:
        GenerarArchivoDeErrores(hola.ListaErrores)
        messagebox.showinfo("Succes","Se Generó el Reporte de Errores")
    except:
        messagebox.showwarning("Advertencia","No se pudo Generar el Reporte de Errores, por favor analice el Archivo")
def View():
    messagebox.showinfo("Succes","Por favor tomese su tiempo para poder familiarizarse con el programa :)")
def Regresar():
    global VentanaAyuda
    VentanaAyuda.destroy()
    VentanaPrincipal()
def Edicion():
    messagebox.showinfo("Succes","Para comenzar a editar debe posicionarse en el cuadro de Texto")
def Windows():
    messagebox.showinfo("Succes","Para conocer todas las opciones por favor vaya al apartado Help/ Manual de Usuario")
def Ayuda():
    global VentanaAyuda
    global ventanaprincipal
    ventanaprincipal.destroy()
    VentanaAyuda = tkinter.Tk()
    VentanaAyuda.title("Temas de Ayuda")
    VentanaAyuda.geometry("1000x400")
    VentanaAyuda.config(bg="light cyan")
    VentanaAyuda.resizable(0,0)
    #ETIQUETAS
    lbldatoscurso = Label(VentanaAyuda,text="Nombre del Curso: Lab Lenguajes Formales y de Programación          Sección B+",font="Cambria 22", fg="SteelBlue4", bg="light cyan")
    lbldatoscurso.place(x=10,y=10)
    lbldatosestudiante = Label(VentanaAyuda,text="Nombre del Estudiante: Kevin Estuardo Palacios Quiñonez",font="Cambria 22", fg="SteelBlue4", bg="light cyan")
    lbldatosestudiante.place(x=10,y=60)
    lblcarne = Label(VentanaAyuda,text="Carné del Estudiante: 201902278",font="Cambria 22", fg="SteelBlue4", bg="light cyan")
    lblcarne.place(x=10,y=110)
    
    #BOTONES AYUDA
    botonregresar= Button(VentanaAyuda,text="Regresar",fon="arial 20", fg="gray24", bg="powder blue", relief="groove", bd=9, width=14,command=Regresar)
    botonregresar.place(x=650,y=300)
    VentanaAyuda.mainloop()
def GuardarComo():
    global textbox
    global ruta
    try:
        ruta = filedialog.asksaveasfile(title="Guardar Archivo", filetypes = (("Text files", "*.gpw*"), ("all files", "*.*")))
        if ruta:
            MiTexto = textbox.get(1.0,END)
            ruta.write(MiTexto)
            ruta.close()
            messagebox.showinfo("Succes","Se Guardo el Archivo")
    except:
        messagebox.showwarning("Advertencia","No se pudo guardar el Archivo")
def Guardar():
    global RutaArchivo
    global textbox
    try:
        ruta = open(RutaArchivo,"w",encoding="utf8")
        ruta.write(textbox.get(1.0,END))
        ruta.close()
        messagebox.showinfo("Succes","Se Guardo el Archivo")
    except:
        messagebox.showwarning("Advertencia","No se pudo guardar el Archivo, por favor cargue un archivo primero")
def Nuevo():
    global RutaArchivo
    global lblespacio
    if lblespacio != "":
        resultado=messagebox.askquestion("Nuevo Documento", "¿Esta seguro?", icon="warning")
        if resultado=="yes":
            textbox.delete("1.0", "end") 
            lblespacio.configure(text="Ruta: ")
            messagebox.showinfo("Succes","Se creó un nuevo documento ")
        else:
            messagebox.showwarning("Advertencia","No se creó nuevo documento")
    elif textbox != "":
        print("hola")
def Abrir():
    global textbox
    global material
    global RutaArchivo
    global lblespacio
    try:
        RutaArchivo = filedialog.askopenfilename(title="Cargar Archivo", filetypes = (("Text files", "*.gpw*"), ("all files", "*.*")))
        ruta2 = open(RutaArchivo,"r",encoding="utf-8")
        material = ruta2.read()
        print(material)
        textbox.insert(END, str(material))
        lblespacio.configure(text="Ruta: "+RutaArchivo)
        messagebox.showinfo("Succes","Se Cargó el Archivo")
    except:
        messagebox.showwarning("Advertencia","No se pudo Cargar el Archivo")
def VentanaPrincipal():
    global ventanaprincipal
    global textbox
    global lblespacio
    global lblposicionx
    global lblposiciony
    ventanaprincipal = tkinter.Tk()
    ventanaprincipal.title("Kevin IDE")
    ventanaprincipal.geometry("900x900")
    ventanaprincipal.config(bg="SlateGray3")
    ventanaprincipal.resizable(0,0)
    ventanaprincipal.iconbitmap("icono.ico")
    #PESTAÑA
    nb = ttk.Notebook(ventanaprincipal)
    fm = tk.Frame(nb)
    nb.add(fm, text="Editor de Código")
    nb.pack(fill='both', expand=True)
    #TABLA
    tv = ttk.Treeview(ventanaprincipal,columns=("col0","col1","col2","col3"), height = 6)
    tv.column("#0",width=0)
    tv.column("col0",width=100, anchor=CENTER)
    tv.column("col1",width=180, anchor=CENTER)
    tv.column("col2",width=120, anchor=CENTER)
    tv.column("col3",width=535, anchor=CENTER)
    tv.heading("col0", text="Tipo de Error", anchor=CENTER)
    tv.heading("col1", text="Línea en que se encuentra", anchor=CENTER)
    tv.heading("col2", text="Se esperaba", anchor=CENTER)
    tv.heading("col3", text="Descripción de Error", anchor=NW)
    tv.pack()
    tv.place(x=0,y=665)
    #MENU
    menubar = Menu(ventanaprincipal)
    ventanaprincipal.config(menu=menubar)
    #CREACION DEL MENU 
    file_menu = Menu(menubar,tearoff=False)
    help_menu = Menu(menubar, tearoff=0)
    Run_menu = Menu(menubar, tearoff=0)
    Edit_menu = Menu(menubar, tearoff=0)
    View_menu = Menu(menubar, tearoff=0)
    Tool_menu = Menu(menubar, tearoff=0)
    Windows_menu = Menu(menubar, tearoff=0)
    #ITEMS DEL MENU
    file_menu.add_command(label="Abrir",command=Abrir)
    file_menu.add_command(label="Nuevo", command=Nuevo)
    file_menu.add_command(label="Guardar", command=Guardar)
    file_menu.add_command(label="Guardar Como", command=GuardarComo)
    file_menu.add_command(label="Salir",command=ventanaprincipal.destroy)
    #ITEMS DEL MENU AYUDA
    help_menu.add_command(label="Manual de Usuario", command=ManualDeUsuario)
    help_menu.add_command(label="Manual Técnico",command=ManualTecnico)
    #ITEMS DEL MENU COMPILAR
    Run_menu.add_command(label="Ejecutar", command=Ejecutar)
    #ITEMS DEL MENU EDIT
    Edit_menu.add_command(label="Edición", command=Edicion)
    #ITEMS DEL MENU VIEW
    View_menu.add_command(label="Vista", command=View)
    #ITEMS DEL MENU TOOL
    Tool_menu.add_command(label="Temas de Ayuda", command=Ayuda)
    Tool_menu.add_command(label="Reporte de Tokens", command=Tokens)
    Tool_menu.add_command(label="Reporte de Errores", command=Errores)
    #ITEMS DEL MENU WINDOWS
    Windows_menu.add_command(label="Windows", command=Windows)
    #AÑADIR ITEMS A LA BARRA
    menubar.add_cascade(label="File",menu=file_menu)
    menubar.add_cascade(label="Edit",menu=Edit_menu)
    menubar.add_cascade(label="View",menu=View_menu)
    menubar.add_cascade(label="Tools",menu=Tool_menu)
    menubar.add_cascade(label="Windows",menu=Windows_menu)
    menubar.add_cascade(label="Help",menu=help_menu)
    menubar.add_cascade(label="Compilar",menu=Run_menu)
    #ETIQUETAS
    lblespacio= Label(ventanaprincipal,text="Ruta:",font="Cambria 12", fg="gray17")
    lblespacio.place(x=255,y=0)
    lblL= Label(ventanaprincipal,text="Línea:",font="Cambria 12", fg="gray17")
    lblL.place(x=610,y=635)
    lblposicionx= Label(ventanaprincipal,text="",font="Cambria 12", fg="gray17")
    lblposicionx.place(x=665,y=635)
    lblC= Label(ventanaprincipal,text="Columna:",font="Cambria 12", fg="gray17")
    lblC.place(x=715,y=635)
    lblposiciony= Label(ventanaprincipal,text="",font="Cambria 12", fg="gray17")
    lblposiciony.place(x=800,y=635)
    lblestado= Label(ventanaprincipal,text="Status",font="Cambria 12", fg="gray17")
    lblestado.place(x=0,y=825)
    #TEXTBOX
    textbox = scrolledtext.ScrolledText(ventanaprincipal, width=80, height=30,bg="lavender")
    textbox.place(x=40,y=30)
    def callBackLeft(event):
        lblposicionx.configure(text="" +str(event.x ))
        lblposiciony.configure(text="" +str(event.y))

    def callBackRight(event):
        lblposicionx.configure(text="" +str(event.x ))
        lblposiciony.configure(text="" +str(event.y))
    textbox.bind("<Button-1>",callBackLeft)
    textbox.bind("<Button-3>",callBackRight)
    #BOTONES
    photo = PhotoImage(file = r"C:\Users\kevin\OneDrive\Documentos\-LFP-P2_201902278\new.png")
    boton = Button(ventanaprincipal,text="Contar", image=photo, height=20, width=20, command=Nuevo)
    boton.place(x=120,y=0)
    photo2 = PhotoImage(file = r"C:\Users\kevin\OneDrive\Documentos\-LFP-P2_201902278\abrir.png")
    boton2 = Button(ventanaprincipal,text="Contar", image=photo2, height=20, width=20,command=Abrir)
    boton2.place(x=147,y=0)
    photo3 = PhotoImage(file = r"C:\Users\kevin\OneDrive\Documentos\-LFP-P2_201902278\save.png")
    boton3 = Button(ventanaprincipal,text="Contar", image=photo3, height=20, width=20, command=Guardar)
    boton3.place(x=174,y=0)
    photo4 = PhotoImage(file = r"C:\Users\kevin\OneDrive\Documentos\-LFP-P2_201902278\search2.png")
    boton4 = Button(ventanaprincipal,text="Contar", image=photo4, height=20, width=20)
    boton4.place(x=201,y=0)
    photo5 = PhotoImage(file = r"C:\Users\kevin\OneDrive\Documentos\-LFP-P2_201902278\help.png")
    boton5 = Button(ventanaprincipal,text="Contar", image=photo5, height=20, width=20)
    boton5.place(x=228,y=0)

    ventanaprincipal.mainloop()
    #posiciones()

VentanaPrincipal()
