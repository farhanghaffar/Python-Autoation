import datetime
from datetime import datetime
import logging
import os
from selenium import webdriver


class TestConfig:
    BROWSER = 'chrome'
    MOZ_BROWSER = 'Mozilla'

    URL = "https://test.navigo.global/apps/router"
    USERNAME = "automation@navigo-inc.com"
    PASSWORD = "1234"

    IMPLICIT_WAIT = 10


def get_logs():
    TimeStamp = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
    TimeOnly = str(datetime.now())
    LogFileName = "logs_" + f"test_{TimeStamp}.log"
    LogPath = os.path.join(os.path.abspath('NavigoPlatform/Logs'), f"{LogFileName}")
    Logger = logging.getLogger(TimeOnly)
    logging.basicConfig(datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)
    Filehandler = logging.FileHandler(LogPath, mode="w")
    Formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
    Filehandler.setFormatter(Formatter)
    Logger.addHandler(Filehandler)
    Logger.setLevel(logging.INFO)
    return Logger


def headless_chrome_browser(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    # options.add_argument('--disable-gpu')  # Required for headless mode
    # options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS'  # Set the path to Chrome 118
    context.driver = webdriver.Chrome(options=options)
    context.driver.get(TestConfig.URL)


def chrome_browser(context):
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_experimental_option("detach", True)  # Required for headless mode
    context.driver = webdriver.Chrome(options=options)
    context.driver.get(TestConfig.URL)


def chrome_with_param_browser(context, headless_mode):
    options = webdriver.ChromeOptions()
    if headless_mode:
        options.add_argument('--headless=new')
    else:
        options.add_argument('start-maximized')
        # Options.add_argument("--window-size=1920x1080")
        options.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(options=options)
    return context.driver
