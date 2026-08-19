import pytest
import os
os.makedirs("screenshots", exist_ok=True)

@pytest.fixture
def respostas_api():
    return [
        {"status": 200, "endpoint": "/login"},
        {"status": 404, "endpoint": "/utilizadores"},
        {"status": 201, "endpoint": "/registo"},
    ]

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")