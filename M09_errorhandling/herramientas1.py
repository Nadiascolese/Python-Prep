class Herramientas:
    def __init__(self, lista_numeros): #importamos el modulo herramientas de la clase amterior
        if type (lista_numeros) != list : #como es una lista decximos que si la lista de numeros es distinto al tipo de lista, entonces :
         self.list=[] #creamos una lista vacia en donde se almacenen
         raise ValueError ("Se creo una lista vacia. se esperaba una lista de numeros enteros") #con raise salvamos el error y valuerror porque es un error de valor
        else :
         self.lista = lista_numeros


    def verifica_primo(self):
        lista_primos=[]#cremos una lista vacia donde almacenar los nros primos
        for i in self.lista: #por cada elemento en la lista vemos si es o no primo
            if (self.__verifica_primo(i)):
               # print('El elemento', i, 'SI es un numero primo') "aca donde antes habia un print ahora lem vamos a pedir que nos de un true o false que era lo que nos pedian"
                lista_primos.append(True)# retornaria la lista de primos y le apendamos true
            else:
               # print('El elemento', i, 'NO es un numero primo') "LO MISMO PASA EN ELSE, PERO LE APPENDAMOS FALSE"
                lista_primos.append(False)

    def conversion_grados(self, origen, destino): #evaluamos si el origen y el destino son los que nosotros espermos 
        parametros_esperados= ["celsius", "farenheit", "kelvin"] #lo hacemos con una lista
        lista_conversion = [] #creamos una lista para guardar los resultados de la conversion
        if str(origen) not in parametros_esperados : #hacemos un loop para saber si el origen esta o no en parametros esperados
            print("Los parametros de origen esperados son: "(parametros_esperados))
            return lista_conversion #en este caso retornaria una lista vacia porque los valores ingresados no funcionaron
        if str(destino) not in parametros_esperados :
            print("Los parametros de destino esperados son: "(parametros_esperados))
            return lista_conversion

        for i in self.lista:
            lista_conversion.append(self.__conversion_grados(i, origen, destino)) #pasamos los valores de origen y destino a la lista de conversion
            return lista_conversion
        

    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))

    def __verifica_primo(self, nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo

    def valor_modal(self, menor):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo

    def __conversion_grados(self, valor, origen, destino):
        valor_destino = None
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino

    def __factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        return numero