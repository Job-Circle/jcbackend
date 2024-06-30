from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import TimeoutException

def postToFacebook(post):
    username = 'BOT_EMAIL'
    password = 'BOT_PASSWORD'

    # Setup WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        driver.get('https://www.facebook.com')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        ).send_keys(username)
        driver.find_element(By.ID, 'pass').send_keys(password)
        driver.find_element(By.ID, 'pass').send_keys(Keys.RETURN)
        time.sleep(1)
        group_url = 'https://www.facebook.com/groups/1313622915846329'
        driver.get(group_url)
        time.sleep(1)

        # Finds the button element to create a post
        input_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, './/span[.="Write something..."]'))
        )
        grandparent_div = input_element.find_element(By.XPATH, './ancestor::div[@class="x1i10hfl x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou"]')
        grandparent_div.click()
        # Finds the textbox element to create a post
        time.sleep(1)
        try:
            # Try to find and click the element with aria-label "Create a public post…"
            create_post_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Create a public post…"]'))
            )
            create_post_element.send_keys(post.get('content'))
        except TimeoutException:
            try:
                # If the first element is not found, try to find and click the element with aria-label "Write something..."
                write_something_element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Write something..."]'))
                )
                write_something_element.send_keys(post.get('content'))
            except TimeoutException:
                print("Neither of the elements was found.")
        # Finds the post button element to create a post

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Post"]'))
        ).click()
    except Exception as e:
        return e
    finally:
        driver.quit()