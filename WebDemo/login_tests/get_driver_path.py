from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from robot.api.deco import keyword

_DRIVERS_MAP = {'chrome': ChromeDriverManager, 'edge': IEDriverManager, 'firefox': GeckoDriverManager}


# class WebDriverPath:
#     """ A method for setting the driver path and download it automatically"""
#
#     ROBOT_LIBRARY_SCOPE = 'GLOBAL'
#     ROBOT_LIBRARY_DOC_FORMAT = 'REST'

@keyword
def get_driver_path(driver_name):
    path = _DRIVERS_MAP[driver_name.lower()]().install()
    print(f'######### DRIVER PATH #############: {path}')
    return path
