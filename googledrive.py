from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)  # leave my browser open

driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.get("https://drive.google.com/drive/u/0/my-drive")
