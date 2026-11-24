import sys
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch()
    pagina = navegador.new_page()
    pagina.goto("https://www.saucedemo.com")
    titulo = pagina.title()
    navegador.close()

if titulo == "Swag Labs":
    print("PASA: el título es correcto")
else:
    print(f"FALLA: se esperaba 'Swag Labs' y llegó '{titulo}'")
    sys.exit(1)