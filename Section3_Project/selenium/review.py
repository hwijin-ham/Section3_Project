from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome("/Users/hamhwijin/Section3_Project/selenium/chromedriver")
#웹 페이지 열기
driver.get("http://kko.to/a1Bd3MCRIL")

# 로딩 기다리기
driver.implicitly_wait(10)

# 팝업 창 클릭으로 제거
driver.find_element(By.CSS_SELECTOR, ".layer_body").click()

# csv 파일 생성
f = open(r"/Users/hamhwijin/Section3_Project/selenium/review_data.csv", 'w', encoding='UTF-8')
csvWriter = csv.writer(f)

for i in range(40):
    # 후기 남긴 카페 클릭
    driver.find_elements(By.CSS_SELECTOR, ".link_txt")[i].click()

    time.sleep(3)

    # 팝업 창 제거
    try:
        driver.find_element(By.CSS_SELECTOR, ".desc_coach").click()
    except:
        pass

    # 카페 상세정보 확인
    driver.find_element(By.CSS_SELECTOR, ".detail").click()
    time.sleep(3)

    # 새로운 탭으로 이동
    last_tab = driver.window_handles[-1]
    driver.switch_to.window(window_name=last_tab)

    time.sleep(3)

    # 이름
    name = driver.find_element(By.CSS_SELECTOR, ".inner_place > .tit_location").text

    # 후기 별점
    score = driver.find_elements(By.CSS_SELECTOR, ".color_b")[0].text

    # 태그
    try:
        tags = driver.find_element(By.CSS_SELECTOR, ".link_tag").text
    except:
        tags = "null"

    # 음료 가격
    try:
        price = driver.find_element(By.CSS_SELECTOR, ".price_menu").text
    except:
        price = 0

    # like point
    try:
        like = driver.find_element(By.CSS_SELECTOR, ".txt_likepoint").text
    except:
        like = "null"


    print(name)
    print(score)
    print(tags)
    print(price)
    print(like)

    # 파일 쓰기
    csvWriter.writerow([name, tags, price, like, score])
    

    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    time.sleep(3)

f.close()

driver.close()

    # assert "Python" in driver.title
    # elem = driver.find_element(By.NAME, "q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source