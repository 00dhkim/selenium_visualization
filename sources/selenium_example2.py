from selenium import webdriver
import time
import selenium_visualization

driver_path = '/home/skeep194/selenium_visualization/sources/chromedriver'
if __name__ == '__main__':
    driver = webdriver.Chrome(driver_path)
    driver.get("http://lms.knu.ac.kr")
    mbox = driver.find_element_by_xpath("//div[@class='m-box2']")
    selenium_visualization.tree(mbox, max_depth=2, show_text=True)
