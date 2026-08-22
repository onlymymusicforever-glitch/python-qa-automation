from playwright.sync_api import Page, expect
from pages.playwright_page import PlaywrightPage
import os
import pytest

@pytest.mark.ui
def test_abre_browser(page: Page):
    page.goto("https://google.com")
    print(page.title())
    assert page.title() == "Google"

@pytest.mark.ui
def test_pesquisa_duckduckgo(page: Page):
    page.goto("https://duckduckgo.com")
    page.locator("[name='q']").fill("pytest")
    page.keyboard.press("Enter")
    page.wait_for_timeout(2000)
    assert "pytest" in page.title()

@pytest.mark.ui
def test_validar_titulo(page: Page):
    page.goto("https://playwright.dev")
    expect(page.locator("h1")).to_be_visible()

@pytest.mark.ui
def test_validar_botao(page: Page):
    page.goto("https://playwright.dev")
    expect(page.get_by_role("link", name="Get started")).to_be_visible()

@pytest.mark.ui    
def test_validar_click_botao(page: Page):
    page.goto("https://playwright.dev")
    page.get_by_role("link", name="Get started").click()
    assert "/docs/intro" in page.url
    expect(page.locator("h1")).to_be_visible()
    expect(page.locator("h1")).to_contain_text("Installation")

@pytest.mark.ui
def test_get_started_pom(page: Page):
    p = PlaywrightPage(page)
    p.ir_para()
    p.clicar_get_started()
    expect(p.titulo).to_be_visible()

@pytest.mark.ui
def test_espera_navegacao(page: Page):
    page.goto("https://playwright.dev")
    page.get_by_role("link", name="Get started").click()
    page.wait_for_url("**/docs/intro")
    expect(page.locator("h1")).to_contain_text("Installation")

@pytest.mark.ui
def test_screenshot(page: Page):
    page.goto("https://playwright.dev")
    page.get_by_role("link", name="Get started").click()
    page.wait_for_url("**/docs/intro")
    expect(page.locator("h1")).to_contain_text("Installation")
    os.makedirs("screenshots", exist_ok=True)
    page.screenshot(path="screenshots/playwright_docs.png")
    assert os.path.exists("screenshots/playwright_docs.png")

@pytest.mark.ui
def test_login_invalido(page: Page, base_url):
    page.goto(f"{base_url}/login")
    page.get_by_role("textbox", name="Username").fill("admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name=" Login").click()
    expect(page.get_by_text("Your username is invalid!")).to_be_visible()


@pytest.mark.smoke
@pytest.mark.ui
def test_login_valido_logout(page: Page, base_url):
    page.goto(f"{base_url}/login")
    page.get_by_role("textbox", name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name=" Login").click()
    expect(page.get_by_text("You logged into a secure area")).to_be_visible()
    expect(page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()
    logout = page.get_by_role("link", name="Logout")
    expect(logout).to_be_visible()
    logout.click()

