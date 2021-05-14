#!/usr/bin/env python3


from tkinter import*
import math



root=Tk()
root.title("SOURDOUGH CALCULATOR")
miFrame=Frame(root)
miFrame.pack()
barMenu=Menu(root) #creacion del menu
miFrame.config(bg="#2d572c")
root.config(menu=barMenu, width=300, height=300, bg="#2d572c") #ancho y largo de la ventana



def calcular():
        
    # Función para validar datos y calcular dentro de la misma funcion    
    datos = True
    try:
        calculoAgua = ra.set( float( nH.get() ) * float(nA.get() )/100 )
        calculoMM = rmm.set( ( float(nH.get()) * 200 )/1000 ) 
        calculoSal = rs.set( ( float(nH.get())  * 20 )/1000 )
    except:
        datos = False
        


nH=StringVar()
nA=StringVar()
ra=StringVar()
rmm=StringVar()
rs=StringVar()

#-------------- titles-----------------------------

cuadroHarina=Label(miFrame, text="Cantidad de Harina: ",bg="#2d572c")
cuadroHarina.grid(row=0,column=0, sticky="e", pady=10, padx=10)

cuadroHidratacion=Label(miFrame, text="Porcentaje de Hidratación: ",bg="#2d572c")
cuadroHidratacion.grid(row=1,column=0, sticky="e", pady=10, padx=10)

cuadroAgua=Label(miFrame, text="Agua: ",bg="#2d572c")
cuadroAgua.grid(row=3,column=0, sticky="e", pady=10, padx=10)

cuadroMM=Label(miFrame, text="Masa Madre: ",bg="#2d572c")
cuadroMM.grid(row=4,column=0, sticky="e", pady=10, padx=10)

cuadroSal=Label(miFrame, text="Sal: ",bg="#2d572c")
cuadroSal.grid(row=5,column=0, sticky="e", pady=10, padx=10)

cuadroGramos=Label(miFrame, text="g",bg="#2d572c")
cuadroGramos.grid(row=0,column=3, sticky="e", pady=10, padx=10)

cuadroPorcentaje=Label(miFrame, text="%",bg="#2d572c")
cuadroPorcentaje.grid(row=1,column=3, sticky="e", pady=10, padx=10)


#---------------- entry--------------------

pantallaHarina=Entry(miFrame, textvariable=nH)
pantallaHarina.grid(row=0, column=1, padx=10, pady=10, columnspan=2) #columnspan estira la pantalla a lo ancho
pantallaHarina.config(background="black", fg="#03f943", justify="right")

pantallaHidratacion=Entry(miFrame, textvariable=nA)
pantallaHidratacion.grid(row=1, column=1, padx=10, pady=10, columnspan=2) #columnspan estira la pantalla a lo ancho
pantallaHidratacion.config(background="black", fg="#03f943", justify="right")

#---------------- Salida resultados --------------------


resultadoAgua=Entry(miFrame, textvariable=ra)
resultadoAgua.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

resultadoMM=Entry(miFrame, textvariable=rmm)
resultadoMM.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

resultadoSal=Entry(miFrame, textvariable=rs)
resultadoSal.grid(row=5, column=1, padx=10, pady=10, columnspan=2)
#------------------button--------------------------


botonCalculo=Button(root, text="Calculo", command=calcular)
botonCalculo.pack()



root.mainloop()