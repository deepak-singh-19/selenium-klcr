## conftest.py  (project root)

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Current setup: New browser for every test (best for beginners)
@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    drv = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    drv.implicitly_wait(10)
    yield drv
    drv.quit()

"""
# Future option: Single browser session for the entire test run (faster but advanced)
# Uncomment this and comment the above one when ready.
@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    drv = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    drv.implicitly_wait(10)
    yield drv
    drv.quit()
"""
