from selenium import webdriver
import subprocess

# TODO : 環境構築のスクリプトの関数

def set_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-extensions')
    options.add_argument('--proxy-server="direct://"')
    options.add_argument('--proxy-bypass-list=*')
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument('--lang=ja')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--log-level=3")
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.page_load_strategy = 'eager'

    return options

def app_initialization():
    pip_list = subprocess.run("pip3 list", shell=True, capture_output=True, check=True)
    brew_list = subprocess.run("brew list", shell=True, capture_output=True, check=True)

    if "selenium" not in str(pip_list.stdout):
        subprocess.run("pip3 install selenium", shell=True, capture_output=True, check=True)
    if "beautifulsoup4" not in str(pip_list.stdout):
        subprocess.run("pip3 install beautifulsoup4", shell=True, capture_output=True, check=True)
    if "pandas" not in str(pip_list.stdout):
        subprocess.run("pip3 install pandas", shell=True, capture_output=True, check=True)
    if "chromedriver" not in str(brew_list.stdout):
        subprocess.run("brew reinstall --cask chromedriver", shell=True, capture_output=True, check=True)
    print("setting finished")
