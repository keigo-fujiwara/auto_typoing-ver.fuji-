from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time, random

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Webサイトを開く
url = "https://typing.be-engineer.tech"
driver.get(url)

# ユーザ名とパスワードを準備
username = "K5"
password = "thisistest"

time.sleep(1)
user_bar = driver.find_element("xpath", '//*[@id="id_username"]')
for user_input in username:
    user_bar.send_keys(user_input)

time.sleep(1)
pass_bar = driver.find_element("xpath", '//*[@id="id_password"]')
for pass_input in password:
    pass_bar.send_keys(pass_input)

time.sleep(0.5)
driver.find_element("class name", "login__btn").click()

time.sleep(0.5)
driver.find_element("xpath", '//*[@id="content"]/form/div[1]/label[1]').click()
time.sleep(0.5)



# 終わることのないタイピング
while True:

    # 難易度選択はランダム
    i = random.randint(1, 7)
    time.sleep(1)
    if i == 1:
        driver.find_element("xpath", '//*[@value=1]/parent::label').click()
    elif i == 2:
        driver.find_element("xpath", '//*[@value=2]/parent::label').click()
    elif i == 3:
        driver.find_element("xpath", '//*[@value=3]/parent::label').click()
    elif i == 4:
        driver.find_element("xpath", '//*[@value=4]/parent::label').click()   
    elif i == 5:
        driver.find_element("xpath", '//*[@value=5]/parent::label').click() 
    elif i == 6:
        driver.find_element("xpath", '//*[@value=6]/parent::label').click()    
    else:
        driver.find_element("xpath", '//*[@value=7]/parent::label').click()  

    time.sleep(0.5)
    driver.find_element("xpath", '//*[@id="content"]/form/input').click()


    # スペースキー入力で開始3秒前！
    time.sleep(0.5)
    input_bar = driver.find_element("xpath", '/html/body')
    input_bar.send_keys(" ")
    # 3秒後スタート
    time.sleep(3)

    t = 0
    while t < 20:
        text = driver.find_element("id", 'untyped').text
        for character in text:
            input_bar.send_keys(character)
        t += 1
    time.sleep(2)

    #スクロール前のページの高さを取得
    height = driver.execute_script("return document.body.scrollHeight")

    #スクロール開始位置を設定
    top = 1
    win_height = driver.execute_script("return window.innerHeight")
    #ページ最下部まで、徐々にスクロールしていく
    while top < height:
        top += 10
        driver.execute_script("window.scrollTo(0, %d)" % top)
    time.sleep(2)


    # 難易度選択画面へ
    driver.find_element("xpath", '/html/body/a/img').click()