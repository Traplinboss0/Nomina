import re

Respuesta = "s"
while not Respuesta != "s":

    print("Cordial saludo empleado\n")

    Documento = input("Digite su numero de identificacion \n")
    while not re.findall("\d",Documento):
        Documento = input("Por favor digite un valor valido\n")

    Nombre = input("Digite su Nombre \n")
    while not re.findall("\w",Nombre):
        Nombre = input("Por favor digite un valor valido\n")

    Apellidos = input("Digite su Apellido \n")
    while not re.findall("\w",Apellidos):
        Apellidos = input("Por favor digite un valor valido\n")

    SalarioBase = input("Digite su Salario Base \n")
    while not re.findall("\d",SalarioBase):
        SalarioBase = input("Por favor digite un valor valido\n")

    DT = input("Digite los dias laborados \n")
    while not re.findall("\d",DT):
        DT = input("Por favor digite un valor valido\n")

    transporte = 0

    if (int(SalarioBase) <= 2000000):
        transporte = 117100

    SalarioNeto = int((int(SalarioBase)/30)*int(DT))
    pension = int((SalarioNeto*0.04))
    salud = int((SalarioNeto*0.04))
    Nomina = int(SalarioNeto-(pension+salud))
    transporte = int(transporte/30)*int(DT)
    Nomina = int(Nomina+transporte )


    YN = input("sun datos son: \nNombre: " + Nombre  + " "+ Apellidos + "\nDocumento: " + Documento + "\nSalario Base: " + SalarioBase + "\nDias Trabajados: " + DT +  "\nDigite s/n para confirmar o cancelar")
    while re.findall("[n]", YN ):
        print("Vuelva a Digitar sus datos por favor \n")
        Documento = input("Digite su numero de identificacion \n")
        while not re.findall("\d", Documento):
            Documento = input("Por favor digite un valor valido\n")

        Nombre = input("Digite su Nombre \n")
        while not re.findall("\w", Nombre):
            Nombre = input("Por favor digite un valor valido\n")

        Apellidos = input("Digite su Apellido \n")
        while not re.findall("\w", Apellidos):
            Apellidos = input("Por favor digite un valor valido\n")

        SalarioBase = input("Digite su Salario Base \n")
        while not re.findall("\d", SalarioBase):
            SalarioBase = input("Por favor digite un valor valido\n")

        DT = input("Digite los dias laborados \n")
        while not re.findall("\d", DT):
            DT = input("Por favor digite un valor valido\n")

        YN = input("Los datos digitados son correctos s/n")






    print("Su descuento por pension es:", pension)
    print("Su descuento por salud es:", salud)
    print("Su subsidio por transorte es de ", transporte)
    print("Su salario neto por trabajar", DT, "dias es de ", Nomina)
    Respuesta = input("Desea continuar con otro proceso de nomina s/n \n")
    file = open("Nomina.txt", "a")
    file.write("Bienvenido usuario \n")
    file.write("###### Nominas ##### \n")
    file.write("Empleado: " + Nombre + Apellidos + "\n")
    file.write("Documento: " + Documento + "\n")
    file.write("Su salario es: " + SalarioBase + "\n")
    file.write("Sus dias trabajados son: " + str(DT) + "\n")
    file.write("Su descuento por pension es: " + str(pension) + "\n")
    file.write("Su descuento por salud es: " + str(salud) + "\n")
    file.write("Su salario neto por trabajar " + str(DT) + "dias es de " + str(Nomina) + "\n")
    file.close()





print("Gracias por usar nuestro programa")




