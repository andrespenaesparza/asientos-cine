def crear_sala(filas, columnas):
    return [["L" for _ in range(columnas)] for _ in range(filas)]

def mostrar_sala(sala):
    for fila in sala:
        print(" ".join(fila))

def reservar_asiento(sala):
    f = int(input("Fila: ")) - 1
    c = int(input("Columna: ")) - 1
    if f < 0 or f >= len(sala) or c < 0 or c >= len(sala[0]):
        print("Asiento inválido.")
        return
    if sala[f][c] == "X":
        print("El asiento ya está ocupado.")
    else:
        sala[f][c] = "X"
        print("Asiento reservado.")

def liberar_asiento(sala):
    f = int(input("Fila: ")) - 1
    c = int(input("Columna: ")) - 1
    if f < 0 or f >= len(sala) or c < 0 or c >= len(sala[0]):
        print("Asiento inválido.")
        return
    if sala[f][c] == "L":
        print("El asiento ya está libre.")
    else:
        sala[f][c] = "L"
        print("Asiento liberado.")

def contar_asientos(sala):
    libres = 0
    ocupados = 0
    for fila in sala:
        for asiento in fila:
            if asiento == "L":
                libres += 1
            else:
                ocupados += 1
    print("Asientos libres:", libres)
    print("Asientos ocupados:", ocupados)

def menu():
    filas = int(input("Número de filas: "))
    columnas = int(input("Número de columnas: "))
    sala = crear_sala(filas, columnas)

    while True:
        print("\n--- CINE ---")
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Liberar asiento")
        print("4. Contar asientos")
        print("5. Salir")
        op = input("Opción: ")

        if op == "1":
            mostrar_sala(sala)
        elif op == "2":
            reservar_asiento(sala)
        elif op == "3":
            liberar_asiento(sala)
        elif op == "4":
            contar_asientos(sala)
        elif op == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

menu()
