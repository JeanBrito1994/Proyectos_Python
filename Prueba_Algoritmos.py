from os import system
validador = True
total_A = 0
total_B = 0
total_C = 0
total_D = 0
recargo_a = 0
recargo_b = 0
recargo_c = 0
recargo_d = 0
acumulador_a = 0
acumulador_b = 0
acumulador_c = 0
acumulador_d = 0
lista_indice = [10,9,8,7,6,5,4,3,2,1]
lista_deptoA = [0,0,0,0,0,0,0,0,0,0]
lista_deptoB = [0,0,0,0,0,0,0,0,0,0]
lista_deptoC = [0,0,0,0,0,0,0,0,0,0]
lista_deptoD = [0,0,0,0,0,0,0,0,0,0]
lista_depto = []
lista_comprador = []
def menu(lista_indice,lista_deptoA,lista_deptoB,lista_deptoC,lista_deptoD):
	partida_indice=0
	contador = 0
	print("|    |  TIPO |")
	print("|PISO|A|B|C|D|")

	while contador < len(lista_indice):
		if lista_indice[partida_indice] == 10:
			print("| " + str(lista_indice[contador]) + " |" + str(lista_deptoA[contador]) +"|"+ str(lista_deptoB[contador]) +"|"+ str(lista_deptoC[contador])+"|"+str(lista_deptoD[contador])+"|")
			contador = contador + 1
			partida_indice = partida_indice + 1

		else:
			print("|  " + str(lista_indice[contador]) + " |" + str(lista_deptoA[contador]) +"|"+ str(lista_deptoB[contador]) +"|"+ str(lista_deptoC[contador])+"|"+str(lista_deptoD[contador])+"|")
			contador = contador + 1

def opcion_1(lista_comprador,lista_deptoA,lista_deptoB,lista_deptoC,lista_deptoD,lista_indice):
	global acumulador_a
	global acumulador_b
	global acumulador_c
	global acumulador_d
	global total_A
	global total_B
	global total_C
	global total_D
	global recargo_a
	global recargo_b
	global recargo_c
	global recargo_d
	global depto
	validador_5 = True
	validador2 = True
	



	
	print("Ingrese su rut")

	rut = input()
	rut = rut.replace(".","")
	rut = rut.replace("-","")



	lista_comprador.append(rut)
	print("En que piso quiere comprar: ")
	print("")
	while validador_5 == True:
		seleccion_piso = int(input())
		if seleccion_piso > 10:
			print("INGRESE UN NUMERO CORRECTO ( PISO 1 AL 10)")
			validador_5 = True
		else:
			validador_5 = False
	
		piso = 10 - seleccion_piso
		print("Que tipo de habitación quiere: ")
		print("[A] Tipo A:    3.800 UF")
		print("[B] Tipo B:    3.000 UF")
		print("[C] Tipo C:    2.800 UF")
		print("[D] Tipo D:    3.500 UF")
		while validador2 == True:
			tipo_habitacion = str.upper(input())
			if tipo_habitacion =="A":
				validador2 = False
				acumulador_a = acumulador_a + 1
				if seleccion_piso > 2:#nuevo
					total_A = total_A + 3800#nuevo
					recargo_a = recargo_a + int(piso -2) * 100#nuevo
				else:#nuevo
					total_A = total_A + 3800#nuevo
				if lista_deptoA[piso] == 0:
					ocupadoA = "X"
					lista_deptoA[piso] = ocupadoA
				
			elif tipo_habitacion =="B":
				validador2 = False
				acumulador_b = acumulador_b + 1
				if seleccion_piso > 2:#nuevo
					total_B = total_B + 3000#nuevo
					recargo_b = recargo_b + int(piso -2) * 100#nuevo
				else:#nuevo
					total_B = total_B + 3000#nuevo
				if lista_deptoB[piso] == 0:
					ocupadoB = "X"
					lista_deptoB[piso] = ocupadoB
			elif tipo_habitacion =="C":
				validador2 = False
				acumulador_c = acumulador_c + 1
				if seleccion_piso > 2:#nuevo
					total_C = total_C + 2800#nuevo
					recargo_c = recargo_c +int(piso -2) * 100#nuevo
				else:#nuevo
					total_C = total_C + 2800#nuevo
				if lista_deptoC[piso] == 0:
					ocupadoC = "X"
					lista_deptoC[piso] = ocupadoC
			elif tipo_habitacion =="D":
				validador2 = False
				acumulador_d = acumulador_d + 1
				if seleccion_piso > 2:#nuevo
					total_D = total_D + 3500#nuevo
					recargo_d = recargo_d + int(piso -2) * 100#nuevo
				else:#nuevo
					total_D = total_D + 3500#nuevo
				if lista_deptoD[piso] == 0:
					ocupadoD = "X"
					lista_deptoD[piso] = ocupadoD

			else:
				print("Ingrese una opción valida")
				validador2 = True
			depto = tipo_habitacion + str(seleccion_piso)
			

		if depto in lista_depto:
			print("Departamento no disponible")
			print("Intente nuevamente")

		else:
			lista_depto.append(depto)
			print("Usted ha seleccionado " + depto)
	return 

def opcion_3(lista_comprador):
	print("Compradores hasta el momento: ")
	print("")
	contador2 = 0
	while contador2 < len(lista_comprador):
		lista_comprador.sort()
		print(lista_comprador[contador2])
		contador2 = contador2 + 1

def opcion_4(lista_comprador):
	print("Ingrese rut de comprador: ")
	consultar_comprador = input()
	if consultar_comprador in lista_comprador:
		print("Comprador de encuentra en la lista")
	else:
		print("No se encuentra rut")

def opcion_5(lista_depto,lista_comprador):
	print("Ingrese departamento a modificar comprador:")
	depto_modificar = str.upper(input())
	print("Ingrese nuevo comprador:")
	nuevo_comprador = str(input())
	contador3 = 0
	while contador3 < len(lista_depto):
		if depto_modificar == lista_depto[contador3]:
			lista_comprador[contador3] = nuevo_comprador
			print("SERVICIO MODIFICADO CORRECTAMENTE")
			break
		else:
			contador3 = contador3 + 1

print(" |__|__|__|__|__|__|__|__|__|__|")
print(" |___|__|__|__|__|__|__|__|__|_|")
print(" |__|__|__|__|__|__|__|__|__|__|")
print(  " |BIENVENIDO A LA INMOBILIARIA |")
print (" |         MURITO              |")
print( " |_____________________________|")
print(" |__|__|__|__|__|__|__|__|__|__|")
print(" |___|__|__|__|__|__|__|__|__|_|")
print(" |__|__|__|__|__|__|__|__|__|__|")
print("")
print("")

while validador == True:
	print("Ingrese una opción:")
	print("------------------")
	print("[1] Comprar departamento")
	print("[2] Mostrar departamentos disponibles")
	print("[3] Ver listado de compradores")
	print("[4] Buscar comprador")
	print("[5] Reasignar comprar")
	print("[6] Mostrar ganancias totales")
	print("[7] Salir")
	opcion = str(input())
	system("cls")

	if opcion =="1":#COMPRA DE DEPA
		opcion_1(lista_comprador,lista_deptoA,lista_deptoB,lista_deptoC,lista_deptoD,lista_depto)
		menu(lista_indice, lista_deptoA,lista_deptoB,lista_deptoC,lista_deptoD)
		input()
		system("cls")

	if opcion =="2":#MOSTRAR DEPARTAMENTOS
		menu(lista_indice, lista_deptoA,lista_deptoB,lista_deptoC,lista_deptoD)
		input()
		system("cls")

	if opcion =="3":#VER LISTADO DE COMPRADORES
		opcion_3(lista_comprador)
		input()
		system("cls")

	if opcion =="4":#BUSCAR COMPRADOR
		opcion_4(lista_comprador)
		input()
		system("cls")

	if opcion =="5": #REASIGNAR COMPRA
		opcion_5(lista_depto,lista_comprador)
		input()
		system("cls")			

	if opcion =="6":#MOSTRAR LAS GANANCIAS

		print("")
		print("TIPO DE DEPTO     | CANTIDAD  | TOTAL   | RECARGO POR PISO |")
		print("-----------------------------------------------------------")
		print("Tipo A  3.800 UF  |  "+str(acumulador_a).zfill(2)+"       | "+str(total_A).zfill(5)+"   | " + str(recargo_a).zfill(5)+"            |")
		print("Tipo B  3.000 UF  |  "+str(acumulador_b).zfill(2)+"       | "+str(total_B).zfill(5)+"   | " + str(recargo_b).zfill(5)+"            |")
		print("Tipo C  2.800 UF  |  "+str(acumulador_c).zfill(2)+"       | "+str(total_C).zfill(5)+"   | " + str(recargo_c).zfill(5)+"            |")
		print("Tipo D  3.500 UF  |  "+str(acumulador_d).zfill(2)+"       | "+str(total_D).zfill(5)+"   | " + str(recargo_d).zfill(5)+"            |")
		print("-----------------------------------------------------------")
		print("TOTALES           |  "+str(acumulador_a+acumulador_b+acumulador_c+acumulador_d).zfill(2)+"       | "+str(total_A+total_B+total_C+total_D).zfill(5)+"   | " + str(recargo_a+recargo_b+recargo_c+recargo_d).zfill(5)+"            |")
		input()
		system("cls")
		
	if opcion =="7":#SALIR
		print("Presione enter para salir")
		validador=False

input()
