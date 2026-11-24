saldo = 3000
transferencia = 500

saldo_final = saldo - transferencia

# El monto no está entre 1 y 5000 
if not(1 <= transferencia <= 5000):
    print(f"S/{transferencia}: Monto fuera de rango")
elif (transferencia > saldo): #El monto es mayor que el saldo
    print("Saldo insuficiente")
else:# Si no se cumple ninguna, Es transferencia aprobada
    print(f"Transferencia aprobada. Saldo Final: S/{saldo_final}")

