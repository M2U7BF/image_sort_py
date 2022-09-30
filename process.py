import datetime
import os.path
import time
from initial_process import *
from const import *
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib.request
import requests
import re

print(os.getcwd())

texts = []
urls = []

# 初期化
# スクレイピング
def scraping():
    # urlの用意
    file_urls = get_file_urls()

    driver = webdriver.Chrome(options = set_options())
    driver.implicitly_wait(STANDBY_TIME)

    # google画像検索にアクセス
    driver.get(WEBSITE_URL)

    # 画像アップロード
    try:
        camera_button = driver.find_elements(By.CLASS_NAME, "nDcEnd")[0]

        # クリック
        camera_button.click()
    except:
        raise Exception

    ## url入力欄の取得
    try:
        url_input = driver.find_elements(By.CLASS_NAME, "cB9M7")[0]
        url_input.send_keys(file_urls[0])
    except:
        raise Exception

    try:
        search_button = driver.find_elements(By.CLASS_NAME, "Qwbd3")[0]
        search_button.click()
    except:
        raise Exception

    try:
        result_top_title = driver.find_elements(By.CLASS_NAME, "DeMn2d")[0].text
        print(result_top_title)
        result_top_desc = driver.find_elements(By.CLASS_NAME, "XNTym")[0].text
        print(result_top_desc)
        site_title_elems = driver.find_elements(By.CLASS_NAME, "UAiK1e")
        for elem in site_title_elems:
            print(elem.text)
    except:
        raise Exception

    time.sleep(100)
    ## 検索
    ## 上位5件を見るa
    ## ヒットした｢サイトタイトル｣を取得

def get_file_urls():
    # 画像のローカルのパス取得
    file_names_str = str(subprocess.run("ls " + IMAGE_SOURCE_PATH , shell=True, capture_output=True, check=True).stdout)
    file_names_str = file_names_str.replace('\'','') # 引用符を除去
    file_names_str = file_names_str[1:] # 先頭に謎の'b'という文字が入っていたため除去
    file_names = file_names_str.split('\\n')

    file_names.remove('') # 空の要素を削除

    file_urls = [GCP_BACKET_URL + file_name for file_name in file_names]
    # for url in file_urls:
    #     print(url)
    return file_urls