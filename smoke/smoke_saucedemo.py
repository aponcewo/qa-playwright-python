import sys
from playwright.sync_api import sync_playwright

titulo_esperado = "Swag Labs"


with sync_playwright() as p:
    navegador = p.chromium.launch()
    pagina = navegador.new_page()
    pagina.goto("https://www.saucedemo.com")
    titulo = pagina.title()
    navegador.close()

if titulo == titulo_esperado:
    print("PASA: el título es correcto")
else:
    print(f"FALLA: se esperaba '{titulo_esperado}' y llegó '{titulo}'")
    sys.exit(1)