import os.path
import re
import time
import traceback

from initial_process import *
from const import *
from selenium.webdriver.common.by import By

class Process:
    file_paths = []
    file_urls = []
    file_names = []
    # 初期化
    driver = webdriver.Chrome(options = set_options())

    def __init__(self) -> None:
        # ファイルパスの用意
        Process.file_paths = Process.get_file_paths()
        # urlの用意
        Process.file_urls = Process.get_file_urls()
        Process.file_names = Process.get_file_names()

    # 初期化
    # スクレイピング
    def scraping(self):
        self.driver.implicitly_wait(STANDBY_TIME)

        for file_name in self.file_names:

            # google画像検索にアクセス
            self.driver.get(WEBSITE_URL)

            # 画像アップロード
            try:
                camera_button = self.driver.find_element(By.CLASS_NAME, "nDcEnd")
                # クリック
                camera_button.click()
            except:
                print(ERROR_MSG)
                traceback.print_exc()
                continue

            # ファイル名でローカルパス取得
            file_paths = [file_path for file_path in Process.get_file_paths() if file_name in file_path]
            # ファイル名でurl取得
            file_urls = [file_url for file_url in Process.get_file_urls() if file_name in file_url]

            if len(file_paths)==0:
                print(ERROR_MSG)
                traceback.print_exc()
                continue
            if len(file_urls)==0:
                print(ERROR_MSG)
                traceback.print_exc()
                continue

            try:
                self.search(file_paths[0],file_urls[0])
            except:
                print(ERROR_MSG)
                traceback.print_exc()
                continue

    def search(self, file_path, file_url):
        driver = self.driver
        ## url入力欄の取得
        try:
            url_input = driver.find_element(By.CLASS_NAME, "cB9M7")
            url_input.send_keys(file_url)
        except:
            print(ERROR_MSG)
            traceback.print_exc()

        try:
            search_button = driver.find_element(By.CLASS_NAME, "Qwbd3")
            search_button.click()
        except:
            print(ERROR_MSG)
            traceback.print_exc()

        try:
            result_top_title = driver.find_element(By.CLASS_NAME, "DeMn2d").text
            result_top_desc = driver.find_element(By.CLASS_NAME, "XNTym").text
            Process.rename(file_path, f"{result_top_title}\({result_top_desc}\)")
        except:
            try:
                site_title = driver.find_element(By.CLASS_NAME, "UAiK1e").text
                # 名前をカット
                if len(site_title) > 20:
                    site_title=site_title[:20]

                site_title = re.sub(':', '', site_title) # コロンを除去
                site_title = re.sub('|', '\|', site_title) # パイプをエスケープ
                site_title = re.sub('/', '-', site_title) # スラッシュを変換
                Process.rename(file_path, f"file\({site_title}~\)")
            except:
                print(ERROR_MSG)
                traceback.print_exc()
                raise Exception

        time.sleep(STANDBY_TIME)

    @classmethod
    def rename(cls, file_path, new_name):
        # 拡張子を取得
        extention = os.path.splitext(file_path)[-1]
        subprocess.run(f"mv {file_path} \'{IMAGE_SOURCE_PATH}{new_name}{extention}\'", shell=True, capture_output=True, check=True)
        print(f"SUCCESS : {new_name}{extention} {'¥'*5}")

    @classmethod
    def get_file_names(cls):
        file_names_str = str(subprocess.run("ls " + IMAGE_SOURCE_PATH , shell=True, capture_output=True, check=True).stdout)
        file_names_str = file_names_str.replace('\'','') # 引用符を除去
        file_names_str = file_names_str[1:] # 先頭に謎の'b'という文字が入っていたため除去
        file_names = file_names_str.split('\\n')

        file_names.remove('') # 空の要素を削除
        return file_names

    @classmethod
    def get_file_paths(cls):
        file_paths = [IMAGE_SOURCE_PATH + file_name for file_name in cls.file_names]
        return file_paths

    @classmethod
    def get_file_urls(cls):
        file_urls = [GCP_BACKET_URL + file_name for file_name in cls.file_names]
        # for url in file_urls:
        #     print(url)
        return file_urls