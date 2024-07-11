import csv
import os
import time
import random
l = ('-'*30)
sul = random.randint(300000 , 2500000)
trabajadores = ["Juan Pérez”, ”María García”, ”Carlos López”, ”Ana Martínez”, ”Pedro Rodríguez”, ”Laura Hernández”, ”Miguel Sánchez”, ”Isabel Gómez”, ”Francisco Díaz”, ”Elena Fernández"]
lis = []
sueldo = []
#establece los elementos a trabajar
#se crea menu
def menu():
    print(f"{l}\n1. Asignar sueldos aleatorios \n2. Clasificar sueldos \n3. Ver estadísticas. \n4. Reporte de sueldos \n5. Salir del programa \n{l}")

def clasificar(trabajadores,sueldo):
    sul_menor = []
    sul_medio = []
    sul_mayor = []
    con_menor = 0
    con_medio = 0
    con_mayor = 0
    
    for i in trabajadores:
        for ele in sueldo:
            if ele < 800000:
                sul_menor.append(i, sul)
                con_menor += 1
            elif  ele < 800000 and ele > 2000000:
                sul_medio.append(i, sul)
                con_medio += 1
            elif ele < 2000000:
                sul_mayor.append(i, sul)
                con_mayor += 1
    return(sul_menor,sul_medio,sul_mayor, con_mayor, con_medio, con_menor)

def esta(sueldo):
    suma = sum(sueldo)
    can = len(sueldo)
    promedio = (suma/can)
    for i in lis:#realmente se me olvido calcuar media geometrica
        maximo = max(i)
        minimo = min(i)
        can = 1
        
    return(promedio, maximo, minimo)
def reporte(trabajadores,lis):
    cs = []
    for i in trabajadores:
        for ele in lis:
            salud = round(ele * 0.07)
            afp = round(ele * 0.12)
            liquido = ele - (salud+afp)
            cs.append([i,ele,salud,afp,liquido])
        with open ('archivo.csv', 'w',newline='') as archivo:
            whi = csv.writer(archivo)
            whi.writerow(['Nombre empleado',  'Sueldo Base',  'Descuento Salud',  "Descuento AFP" , "Sueldo Líquido"])
            whi.writerows(cs)


while True:
    os.system("cls")
    menu()
    op = input("Selecione: ")
    if op == "1":
        os.system("cls")
        for i in trabajadores:
            sul = random.randint(300000 , 2500000)
            lis.append([i, sul])
            sueldo.append([sul])
        print("elementos completados")
        time.sleep(0.3)
    if op == "2":
        os.system("cls")
        clasificar(trabajadores,lis)
        sul_menor,sul_medio,sul_mayor, con_mayor, con_medio, con_menor = clasificar(lis)
        print(f"Sueldos menores a $800.000 TOTAL:  {con_menor}\nNombre        Sueldo")
        for i in sul_menor(i):
            for ele in sul_menor(sul):
                print(i,        ele)
        print(f"Sueldos entre $800.000 y $2.000.000:  {con_medio}\nNombre        Sueldo")
        for i in sul_medio(i):
            for ele in sul_medio(sul):
                print(i,        ele)
        print(f"Sueldos entre $800.000 y $2.000.000:  {con_mayor}\nNombre        Sueldo")
        for i in sul_mayor(i):
            for ele in sul_mayor(sul):
                print(i,        ele)
    elif op == "3":
        esta()
        promedio, maximo, minimo = esta()
        print(f"Sueldo más alto{maximo} \nSueldo más bajo{minimo} \nPromedio de sueldos: {promedio:.2} \n Media geométrica: ")
    elif op == "4": 
        reporte(trabajadores,lis)
        
    elif op == "5":
        print("Finalizando programa… \nDesarrollado por Leandro Marin \nRUT 21944178-9")
        break
    else:
        print("Error: Utiliza las opciones mostradas")
        time.sleep(0.4)