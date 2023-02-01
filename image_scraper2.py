import requests
import io
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
import time

PATH = "driver/chromedriver.exe"

service_obj = Service(PATH)
driver = webdriver.Chrome(service=service_obj)

def get_images_from_google(driver, delay, max_images):

    driver.get("https://images.google.com/?gws_rd=ssl")
    search_box = driver.find_element(By.CLASS_NAME, 'gLFyf')
    search_box.send_keys('elon musk pictures')
    search_btn = driver.find_element(By.CLASS_NAME, 'Tg7LZd')
    search_btn.click()

    image_urls = set()
    
    i = 0
    thumbnails = driver.find_elements(By.CLASS_NAME, 'Q4LuWd')

    while len(image_urls) < max_images and i < len(thumbnails):
        
        # for img in thumbnails: #[len(image_urls): max_images]
        img = thumbnails[i]
        try:
            img.click()
            time.sleep(delay)
            print('clicked thumbnail')
        except:
            continue

        images = driver.find_elements(By.CLASS_NAME, 'n3VNCb')
        print(len(images))
        for image in images:
            print('looking for image')
            if image.get_attribute('src'):
                src_attr = image.get_attribute('src')
                #if 'http' in src_attr and src_attr.endswith(('.jpg', '.png')):
                if 'http' in src_attr:
                    image_urls.add(image.get_attribute('src'))
                    print('Found image ' + str(len(image_urls)))
                    print(image.get_attribute('src'))
                    break
        i += 1

    return image_urls

# def download_image(download_path, url, filename):
#     image_content = requests.get(url).content
#     image_file = io.BytesIO(image_content)
#     image = Image.open(image_file)
#     file_path = download_path + filename

#     with open(file_path, "wb") as f:
#         image.save(f, "JPEG")

#     print("success!")

def download_image(download_path, url, filename):
    try:
        image_content = requests.get(url).content
    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = download_path + filename
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")


urls = get_images_from_google(driver, 2, 5)

for i, url in enumerate(urls):
    download_image("images/", url, f"{i}.jpg")

driver.quit()
