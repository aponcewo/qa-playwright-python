saldo = 10000
montos = [0, 1, 2500, 5000, 5001]



for monto in montos:
    saldo_final = saldo - monto
    if not(1 <= monto <= 5000):
        print(f"S/{monto}: Monto fuera de rango")
    elif (monto > saldo): #El monto es mayor que el saldo
        print("Saldo insuficiente")
    else:# Si no se cumple ninguna, Es transferencia aprobada
        print(f"Transferencia aprobada. Saldo Final: S/{saldo_final}")