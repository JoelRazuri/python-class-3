"""
    Escribir una clase Caja para representar cuánto dinero hay en una caja de un negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la 
    esquina hay 6 billetes de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2, 5, 10, 20, 50, 100, 200, 500 y 1000 pesos.
    Debe comportarse según el siguiente ejemplo:
    
    --> c = Caja({500: 6, 300: 7, 2: 4})
    ValueError: Denominación "300" no permitida
    --> c = Caja({500: 6, 100: 7, 2: 4})
    --> str(c)
    'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
    --> c.agregar({250: 2})
    ValueError: Denominación "250" no permitida
    --> c.agregar({50: 2, 2: 1})
    --> str(c)
    'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
    --> c.quitar({50: 3, 100: 1})
    ValueError: No hay suficientes billetes de denominación "50"
    --> c.quitar({50: 2, 100: 1})
    200
    --> str(c)
    'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'
"""


def exception(diccionario,billete_1,billete_2,billete_3,billete_4,billete_5,billete_6,billete_7,billete_8,billete_9,billete_10):

    try:
        error = "error"
        billetes_falsos = []
        for clave in diccionario:
            if not (clave == billete_1 or clave == billete_2 or clave == billete_3 or clave == billete_4 or clave == billete_5 or clave == billete_6 or clave == billete_7 or clave == billete_8 or clave == billete_9 or clave == billete_10):
                billetes_falsos.append(clave)
        if len(billetes_falsos)>0:
            error = int(error)
        return True
    except (ValueError):
        print(f"ValueError: Denominación {billetes_falsos} no permitida.")
        return False

def exception_2(diccionario,nuevo_dicc,billete_1,billete_2,billete_3,billete_4,billete_5,billete_6,billete_7,billete_8,billete_9,billete_10):

    billetes = []
    for clave in nuevo_dicc:
        if clave in diccionario:
            if (nuevo_dicc[clave]>diccionario[clave]):
                billetes.append(clave)
        else:
            if (clave == billete_1 or clave == billete_2 or clave == billete_3 or clave == billete_4 or clave == billete_5 or clave == billete_6 or clave == billete_7 or clave == billete_8 or clave == billete_9 or clave == billete_10):
                billetes.append(clave)
    if len(billetes)>0:
        print(f"ValueError: No hay suficientes billetes de denominación '{billetes}'.")
        return False
    else:
        return True

def sumar_caja(diccionario,total_caja):

    for clave in diccionario:
        total_caja = total_caja + (clave * diccionario[clave])

    return total_caja

def restar_caja(diccionario,total_caja):

    retirado = 0

    for clave in diccionario:
        total_caja = total_caja - (clave * diccionario[clave])
        retirado = retirado + (clave * diccionario[clave])

    return total_caja,retirado

def quitar_diccionario(diccionario,nuevo_dicc):

    for clave in nuevo_dicc:
        if clave in diccionario:
            diccionario[clave] = diccionario[clave] - nuevo_dicc[clave]
        if diccionario[clave] == 0:
            diccionario.pop(clave)

    return diccionario


def agregar_diccionario(diccionario,nuevo_dicc):

    for clave in nuevo_dicc:
        if clave in diccionario:
            diccionario[clave] = diccionario [clave] + nuevo_dicc[clave]
        else:
            diccionario[clave] = nuevo_dicc[clave]

    diccionario = ordenar_diccionario_descendente(diccionario)

    return diccionario

def ordenar_diccionario_descendente(diccionario):

    lista_claves = list(diccionario.keys())
    lista_valores = list(diccionario.values())

    for i in range(1,len(lista_claves)):     # Burbujeo
        for j in range(len(lista_claves)- i):      
            if(lista_claves[j]<lista_claves[j+1]):    
                aux=lista_claves[j] 
                lista_claves[j]=lista_claves[j+1] 
                lista_claves[j+1]=aux 
                
                aux_2=lista_valores[j]
                lista_valores[j]=lista_valores[j+1] 
                lista_valores[j+1]=aux_2 

    diccionario = dict(zip(lista_claves,lista_valores))
    
    return diccionario



class Caja:
    def __init__(self,diccionario,billete_1=1,billete_2=2,billete_3=5,billete_4=10,billete_5=20,billete_6=50,billete_7=100,billete_8=200,billete_9=500,billete_10=1000,total_caja=0):
        self.diccionario = diccionario
        self.billete_1 = billete_1
        self.billete_2 = billete_2
        self.billete_3 = billete_3
        self.billete_4 = billete_4
        self.billete_5 = billete_5
        self.billete_6 = billete_6
        self.billete_7 = billete_7
        self.billete_8 = billete_8
        self.billete_9 = billete_9
        self.billete_10 = billete_10
        self.total_caja = total_caja

        condicion = exception(self.diccionario,self.billete_1,self.billete_2,self.billete_3,self.billete_4,self.billete_5,self.billete_6,self.billete_7,self.billete_8,self.billete_9,self.billete_10)

        if condicion:
            self.total_caja = sumar_caja(self.diccionario,self.total_caja)
        else:
            self.diccionario = {}
            
    def __str__(self):
        return (f"Caja {self.diccionario} total: {self.total_caja} pesos")        

    def agregar(self,diccionario):
        condicion = exception(diccionario,self.billete_1,self.billete_2,self.billete_3,self.billete_4,self.billete_5,self.billete_6,self.billete_7,self.billete_8,self.billete_9,self.billete_10)
        if condicion:
            self.total_caja = sumar_caja(diccionario,self.total_caja)
            self.diccionario = agregar_diccionario(self.diccionario,diccionario)
    
    def quitar(self,diccionario):
        condicion = exception(diccionario,self.billete_1,self.billete_2,self.billete_3,self.billete_4,self.billete_5,self.billete_6,self.billete_7,self.billete_8,self.billete_9,self.billete_10)
        condicion_2 = exception_2(self.diccionario,diccionario,self.billete_1,self.billete_2,self.billete_3,self.billete_4,self.billete_5,self.billete_6,self.billete_7,self.billete_8,self.billete_9,self.billete_10)

        if condicion and condicion_2:
            self.total_caja,retirado = restar_caja(diccionario,self.total_caja)
            self.diccionario = quitar_diccionario(self.diccionario,diccionario)
            print(retirado)


# c = Caja({500: 6, 300: 7, 250: 7,2: 4})
# print(c)
print("----------------------------------------------------")
print("--> c = Caja(500: 6, 300: 7, 2: 4)")
c = Caja({500: 6, 300: 7, 2: 4})
print("--> c = Caja(500: 6, 100: 7, 2: 4)")
print("--> str(c)")
c = Caja({500: 6, 100: 7, 2: 4})
print(c)
print("--> c.agregar(250: 2)")
c.agregar({250: 2})
print("--> c.agregar(50: 2, 2: 1)")
c.agregar({50: 2, 2: 1})
print("--> str(c)")
print(c)
print("--> c.quitar(50: 3, 100: 4, 1000: 1, 275: 20)")
c.quitar({50: 3, 100: 4, 1000: 1, 275: 20})   
print("--> c.quitar(50: 2, 100: 4)")
c.quitar({50: 2, 100: 4})
print("--> str(c)")
print(c)
print("----------------------------------------------------")