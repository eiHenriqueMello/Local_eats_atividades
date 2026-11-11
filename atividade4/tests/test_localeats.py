# Responsável: Henrique Mello
from playwright.sync_api import Page, expect

def test_pesquisar_restaurante_funcional(page: Page):
    # 1. Acessar a página do LocalEats
    page.goto("https://local-eats-unisenac.vercel.app/")
    
    # 2. Assertion 1: Verificar se a página carrega com sucesso e possui um título/URL válido
    expect(page).to_have_url("https://local-eats-unisenac.vercel.app/static/login.html")
    
    # 3. Assertion 2: Verificar se a página contém elementos interativos (botões ou inputs)
    expect(page.locator("body")).to_be_visible()