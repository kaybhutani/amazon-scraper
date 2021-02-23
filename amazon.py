from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
def getProduct(url, driver):
  driver.get(url)
  title= driver.find_element_by_id('productTitle').text
  about = driver.find_element_by_id('featurebullets_feature_div').text
  imageBtn = driver.find_element_by_class_name("image")
  print(imageBtn.is_displayed())
  imageBtn.click()
  time.sleep(3)
  print(driver.find_element_by_id('ivLargeImage').find_element_by_tag_name('img').get_attribute('src'))
  imagesUrl = []
  images=driver.find_element_by_id('ivThumbs').find_elements_by_class_name("ivThumb")
  for image in images:
      if(image.is_displayed()):
          time.sleep(1)
          try:
              image.click()
              time.sleep(1)
              largeImg = driver.find_element_by_id('ivLargeImage')
              print(largeImg.is_displayed())
              imgSrc = largeImg.find_element_by_tag_name('img').get_attribute('src')
              imagesUrl.append(imgSrc)
          except Exception as err:
              print(err)
  return {
    'title': title, 'about': about, 'images': imagesUrl
  }

if __name__=="__main__":
  driver = webdriver.Chrome('/home/kartikay/Kartikay/Projects/amazon-scraper/chromedriver')
  wait = WebDriverWait(driver, 10)
  print(getProduct('https://www.amazon.in/Amazon-Brand-Solimo-Premium-Stainless/dp/B071SDYY6N/', driver))