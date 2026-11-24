saldo_cuenta = 10000
transferencia = 100

saldo_final = saldo_cuenta - transferencia
monto_valido = 1 <= transferencia <= 5000

print(f"Saldo final: S/{saldo_final}")
print(f"El monto es valido:{monto_valido}")