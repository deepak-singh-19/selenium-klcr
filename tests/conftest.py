import sys
import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# --- Add project root to sys.path so "pages" can be imported ---
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture()
def driver():
    """Fixture to launch and quit Chrome browser."""
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
