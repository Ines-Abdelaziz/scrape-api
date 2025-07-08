from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
def scrape_website(url, target_img_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # run Chrome in headless mode (no GUI)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service('/usr/local/bin/chromedriver')  # path where chromedriver is installed
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get(url)
        adurl = None

        scroll_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.implicitly_wait(2)

            imgs = driver.find_elements(By.TAG_NAME, 'img')
            for img in imgs:
                if img.get_attribute("src") == target_img_url:
                    try:
                        closest_a_tag = img.find_element(By.XPATH, "./ancestor::a")
                        adurl = "https://adstransparency.google.com/" + closest_a_tag.get_attribute("href")
                        break
                    except:
                        continue

            if adurl:
                break

            new_scroll_height = driver.execute_script("return document.body.scrollHeight")
            if new_scroll_height == scroll_height:
                print("Reached the bottom of the page.")
                break
            scroll_height = new_scroll_height

        return adurl

    except Exception as e:
        print("An error occurred:", str(e))
        return None

    finally:
        driver.quit()
