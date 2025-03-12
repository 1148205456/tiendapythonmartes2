nombreVendedor=None 
productos=[]
producto={}

opcion=100

print("Mercado")
print("********")
print("1. Crear lista mercado")
print("2. Ver Lista de mercado")
print("3. Editar producto de la lista")
print("4. Retirar producto de la lista")
print("Presiona 5 para salir")
while opcion != 5:
    opcion=int(input("Digita una opcion: "))
    if opcion == 1:
        print("Bienvenido a la creacion de tu lista de mercado")
        
        #creando claves y valores de un diccionario
        producto["id"]=5
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["precio"]=int(input("Digita el precio del producto: "))
        producto["cantidad"]=int(input("Cuantos elementos de este producto vas a llevar: "))
        producto["presentacion"]=input("Cual presentacion llevaras? ")
        
        #mostrando mi diccionario
        #print(producto)
        
        #poblando una lista (agrgando elementos a una lista)
        productos.append(producto)
        print(productos)
        
        
        
    elif opcion==2:

        #Utilizando ciclos FOR en python para recorrer LISTAS
        for productoSeleccionado in productos:
            print(productoSeleccionado["nombre"])

    elif opcion==3:
       #0. PREGUNTAR A QUIEN SE QUIERE ELIMINAR  
       productoCambio=int(input("Digita el id del producto a editar: "))
       #1. ENCONTRAR EL ELEMENTO
       for productoBuscado in productos:
           if productoBuscado["id"]==productoCambio:
              print("OE LO ENCONTRE")
           else:
               print("NO LO ENCONTRE")
       #2. SELECCIONAR EL ELEMENTO
       #3. ACEDO A LAS PROPIEDADES O ATRIBUTOS QUE QUIERO O PUEDO MODIFICAR
       
    elif opcion==4:
        print("estoy en la 4")
    else:
        print("Opcion no valida")
        