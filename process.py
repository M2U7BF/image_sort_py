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
    driver = webdriver.Chrome(options = set_options())
    driver.implicitly_wait(STANDBY_TIME)

    # google画像検索にアクセス
    driver.get(WEBSITE_URL)

    # 画像のローカルのパス取得
    image_path_list = subprocess.run("ls " + IMAGE_SOURCE_PATH , shell=True, capture_output=True, check=True)
    print(image_path_list.stdout)

    # 画像アップロード
    # https://xn--eckl3qmbc2cv902cnwa746d81h183l.com/instructor-blog/210825how-to-upload-a-file-in-python/

    # 検索

    # 上位5件を見る

    # ヒットした｢サイトタイトル｣を取得
