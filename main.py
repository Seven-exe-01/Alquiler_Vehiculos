"""Aca creamos el menu de las sucursales de alquiler"""
from sucursales import Sucursal
from clientes import Cliente
from enums import TipoVehiculo, EstadoVehiculo, EstadoReserva
import os
import subprocess
from vehiculos import Vehiculo

sucursales=[]
clientes = []
vehiculos = []
reservas = []
tarifa=500

menu=True

while menu:
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print("*"*40)
    print("0. Ingresar la tarifa del dia. ")
    print("1. Crear Sucursal.")
    print("2. Listar Sucursal.")
    print("3. Crear Cliente.")
    print("4. Listar Cliente.")
    print("5. Cargar vehiculo.")
    print("6. Listar vehiculos de una sucursal.")
    print("7. Cambiar datos del vehiculo.") #cambiar estado y sucursal
    print("8. Crear una reserva.")
    print("9. Consultar reservas.")
    print("10. Confirmacion - Alquiler y Devolución de reserva.")
    print("11. Salir.")

    opcion=int(input("Elija una opcion (0-11): "))
    if opcion==0:
        tarifa=int(input("Ingrese la tarifa del dia: "))
    #Crear sucursal
    elif opcion==1:
        print("\n--- REGISTRAR SUCURSAL ---")
        codigo = input("Código: ")
        ciudad = input("Ciudad: ")
        direccion = input("Dirección: ")

        #verificar que la sucursal no se repita
        resul=Sucursal.control_suc(codigo, sucursales)
        if resul:
            print("ya existe el codigo de sucursal que quiere ingresar.")
        else:
            suc = Sucursal(codigo, ciudad, direccion)
            sucursales.append(suc)
            print(f" Sucursal '{ciudad}' creada correctamente.")

    #Ver listado de Sucursales
    elif opcion==2:
        for sucursal in sucursales:
            print("*"*40)
            print("Codigo Suc.: ",sucursal.codigo)
            print("Ciudad: ", sucursal.ciudad)
            print("Direccion: ",sucursal.direccion)
            a=input("")
    #Crear cliente
    elif opcion==3:
        print("\n--- REGISTRAR CLIENTE ---")
        ingresoNombre=input("nombre: ")
        ingresoApellido=input("apellido: ")
        ingresoDni=input("dni: ")
        ingresoTelefono=input("telefono: ")
        ingresoCorreo=input("correo: ")

        #Busca si existe el DNI en la lista
        resul=Cliente.control_dni(ingresoDni, clientes)
        if resul:
            print("el DNI del cliente ya existe.")
        else:
            cli= Cliente(ingresoNombre, ingresoApellido, ingresoDni, ingresoTelefono, ingresoCorreo)
            clientes.append(cli)
            print(f"El Cliente '{ingresoNombre} {ingresoApellido}' se ha registrado correctamente.")
        a=input("")


    #Ver listado de Clientes
    elif opcion==4:
        for cliente in clientes:
            print("="*60)
            print(f"Nombre: '{cliente.nombre}'")
            print(f"Apellido: '{cliente.apellido}'")
            print(f"DNI: '{cliente.dni}'")
            print(f"Telefono: '{cliente.telefono}'")
            print(f"Correo: '{cliente.correo}'")
            print(f"="*60)
        a=input("")
    #Cargar vehiculo
    elif opcion==5:
        print("\n--- REGISTRAR VEHICULO ---")
        ingresoPatente=input("Ingresar la patente del vehiculo: ")
        ingresoMarca=input("Ingrese la marca del vehiculo:")
        ingresoModelo=input("Ingrese la modelo del vehiculo:")
        ingresoEstado=EstadoVehiculo.DISPONIBLE
        ingresoTipo=int(input("Ingrese el tipo del vehiculo (1-AUTO , 2-CAMIONETA, 3-MOTO): "))

        if ingresoTipo == 1:
            tipo_enum = TipoVehiculo.AUTO
        elif ingresoTipo == 2:
            tipo_enum = TipoVehiculo.CAMIONETA
        elif ingresoTipo == 3:
            tipo_enum = TipoVehiculo.MOTO
        else:
            print("Tipo invalido.")
            input("")
            continue

        for mostrarsucu in sucursales:
            print("="*40)
            print(f"{mostrarsucu.codigo} - '{mostrarsucu.direccion}' - '{mostrarsucu.ciudad}'")
            print("="*40)
        ingresoSucursal= int(input("Ingrese a que sucursal pertenece este vehiculo (numeros): "))
        resul=Sucursal.control_suc(ingresoSucursal, sucursales)

        while not resul:
            ingresoSucursal = int(input("Sucursal incorrecta o inexistente, reingrese: "))
            resul = Sucursal.control_suc(ingresoSucursal, sucursales)

        if Vehiculo.control_pat(ingresoPatente, vehiculos):
            print("La patente del vehiculo ya existe. Vuelva a ingresar los datos.")
        else:
            vehiNuevo = Vehiculo(ingresoPatente, ingresoMarca, ingresoModelo, tarifa, ingresoEstado, tipo_enum, ingresoSucursal)
            vehiculos.append(vehiNuevo)
            print("Vehiculo registrado correctamente.")
        input("")

        #Ver lista Clientes
    elif opcion==6:
        cod_buscar = int(input("Ingrese el codigo de sucursal a listar: "))
        for vehi in vehiculos:
            if int(vehi.sucursal) == cod_buscar:
                print("=" * 60)
                print(f"Patente: '{vehi.patente}'")
                print(f"Marca: '{vehi.marca}'")
                print(f"Modelo: '{vehi.modelo}'")
                print(f"Estado: '{vehi.estado.value}'")
                print(f"Tipo: '{vehi.tipo.value}'")
                print(f"Sucursal: '{vehi.sucursal}'")
                print("=" * 60)
        input("")

        #Cambiar datos del vehiculo.
    elif opcion==7:
        IngresarPatente=input("Ingrese la patente del vehiculo que quiere modificar. ")
        vehiculo_encontrado=Vehiculo.buscar_pat(IngresarPatente, vehiculos)
        if vehiculo_encontrado is not None:
            print("="*40)
            print("1. Estado del vehiculo.")
            print("2. Sucursal del vehiculo")
            sub_opcion=int(input("Ingrese la opcion (1-2): "))
            if sub_opcion==1:
                print("Estados 1- DISPONIBLE 2- RESERVADO 3- EN ALQUILER 4- FUERA DE SERVICIO")
                opcionEstado=int(input("ingrese el estado que desea establecer."))
                if opcionEstado==1:
                    vehiculo_encontrado.estado=EstadoVehiculo.DISPONIBLE
                    print(f"El vehiculo cambio el estado exitosamente a {vehiculo_encontrado.estado.value}")
                elif opcionEstado==2:
                    vehiculo_encontrado.estado=EstadoVehiculo.RESERVADO
                    print(f"El vehiculo cambio el estado exitosamente a {vehiculo_encontrado.estado.value}")
                elif opcionEstado==3:
                    vehiculo_encontrado.estado=EstadoVehiculo.EN_ALQUILER
                    print(f"El vehiculo cambio el estado exitosamente a {vehiculo_encontrado.estado.value}")
                elif opcionEstado==4:
                    vehiculo_encontrado.estado=EstadoVehiculo.FUERA_DE_SERVICIO
                    print(f"El vehiculo cambio el estado exitosamente a {vehiculo_encontrado.estado.value}")
                else:
                    print("Estado invalido.")
            elif sub_opcion == 2:
                nueva_suc = int(input("Ingrese el codigo de la nueva sucursal del vehiculo: "))
                if Sucursal.control_suc(nueva_suc, sucursales):
                    vehiculo_encontrado.sucursal = nueva_suc
                    print("Sucursal actualizada correctamente.")
                else:
                    print("La sucursal ingresada no existe.")
            else:
                print("Opcion invalida.")
        else:
            print("No se encontro ningun vehiculo con esa patente.")
        a=input("")
        #Crear una reserva.
    elif opcion==8:
        print("\n--- CREAR RESERVA ---")
        dni_cli = input("Ingrese el DNI del cliente: ")
        cliente_sel = None
        for cliente in clientes:
            if cliente.dni == dni_cli:
                cliente_sel = cliente
                break

        pat_vehi = input("Ingrese la Patente del vehiculo: ")
        vehi_sel = Vehiculo.buscar_pat(pat_vehi, vehiculos)

        if cliente_sel is None or vehi_sel is None:
            print("Cliente o vehiculo no encontrado.")
            input("")
            continue

        try:
            dias = int(input("Cantidad de dias de alquiler: "))
            if dias <= 0:
                raise ValueError("La cantidad de dias debe ser mayor a cero.")

            costo = vehi_sel.tarifa * dias
            if costo < 0:
                raise ValueError("El costo total no puede ser negativo.")

            reserva = {
                "id": len(reservas) + 1,
                "cliente": cliente_sel,
                "vehiculo": vehi_sel,
                "dias": dias,
                "costo": costo,
                "estado": EstadoReserva.SOLICITADA,
                "historial": [f"Reserva creada en estado {EstadoReserva.SOLICITADA.value}"]
            }
            reservas.append(reserva)
            print(f"Reserva #{reserva['id']} creada. Costo estimado: ${costo}")
        except ValueError as e:
            print(f"Error al crear reserva: {e}")
        input("")

        #Consultar reservas.")
    
    elif opcion==9:
        print("\n--- CONSULTAR RESERVAS ---")
        for r in reservas:
            print("=" * 50)
            print(f"ID: {r['id']} | Cliente: {r['cliente'].nombre} {r['cliente'].apellido}")
            print(f"Vehiculo: {r['vehiculo'].patente} | Dias: {r['dias']} | Costo: ${r['costo']}")
            print(f"Estado: {r['estado'].value}")
            print("Historial:")
            for h in r["historial"]:
                print(f"  - {h}")
        input("")

        #Confirmacion - Alquiler y Devolución de reserva.
    elif opcion==10:
        print("\n--- GESTIONAR ESTADO DE RESERVA ---")
        id_res = int(input("Ingrese el ID de la reserva: "))
        reserva_sel = None
        for r in reservas:
            if r["id"] == id_res:
                reserva_sel = r
                break

        if reserva_sel is None:
            print("Reserva no encontrada.")
            input("")
            continue

        print(f"Estado actual: {reserva_sel['estado'].value}")
        print("1. Confirmar reserva")
        print("2. Iniciar alquiler (EN_CURSO)")
        print("3. Finalizar reserva")
        print("4. Cancelar reserva")
        opcion = int(input("Elija una opcion: "))

        try:
            if opcion == 1:
                if reserva_sel["vehiculo"].estado != EstadoVehiculo.DISPONIBLE:
                    raise ValueError("No se puede confirmar una reserva si el vehiculo no esta disponible.")
                reserva_sel["estado"] = EstadoReserva.CONFIRMADA
                reserva_sel["vehiculo"].estado = EstadoVehiculo.RESERVADO
                reserva_sel["historial"].append("Reserva CONFIRMADA")
                print("Reserva confirmada.")
            elif opcion == 2:
                reserva_sel["estado"] = EstadoReserva.EN_CURSO
                reserva_sel["vehiculo"].estado = EstadoVehiculo.EN_ALQUILER
                reserva_sel["historial"].append("Alquiler EN_CURSO")
                print("Alquiler iniciado.")
            elif opcion == 3:
                if reserva_sel["estado"] == EstadoReserva.SOLICITADA:
                    raise ValueError("Una reserva SOLICITADA no puede pasar directamente a FINALIZADA.")
                reserva_sel["estado"] = EstadoReserva.FINALIZADA
                reserva_sel["vehiculo"].estado = EstadoVehiculo.DISPONIBLE
                reserva_sel["historial"].append("Reserva FINALIZADA")
                print("Reserva finalizada.")
            elif opcion == 4:
                reserva_sel["estado"] = EstadoReserva.CANCELADA
                if reserva_sel["vehiculo"].estado == EstadoVehiculo.RESERVADO:
                    reserva_sel["vehiculo"].estado = EstadoVehiculo.DISPONIBLE
                reserva_sel["historial"].append("Reserva CANCELADA")
                print("Reserva cancelada.")
        except ValueError as e:
            print(f"Operacion invalida: {e}")
        input("")

        #Salir
    elif opcion==11:
        menu=False
