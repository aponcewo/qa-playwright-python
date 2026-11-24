saldo = 10000
montos = [0, 1, 2500, 5000, 5001]

def evaluar_transferencia(saldo,monto):
        saldo_final = saldo - monto
        if not(1 <= monto <= 5000):
            return(f"S/{monto}: Monto fuera de rango")
        elif (monto > saldo): #El monto es mayor que el saldo
             return("Saldo insuficiente")
        else:# Si no se cumple ninguna, Es transferencia aprobada
            return(f"Transferencia aprobada. Saldo Final: S/{saldo_final}")

print(evaluar_transferencia(10000, 2500))
print(evaluar_transferencia(10000, 0))


