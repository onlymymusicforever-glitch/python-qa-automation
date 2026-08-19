class PlaywrightPage:
    def __init__(self, page):
        self.page = page
        self.get_started = page.get_by_role("link", name="Get started")
        self.titulo = page.locator("h1")

    def ir_para(self):
        self.page.goto("https://playwright.dev")

    def clicar_get_started(self):
        self.get_started.click()

