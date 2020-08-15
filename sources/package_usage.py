from selenium import webdriver
import time
import selenium_visualization as sele_vis

driver_path = 'chromedriver_83.exe'
if __name__ == '__main__':
    driver = webdriver.Chrome(driver_path)
    driver.get("http://lms.knu.ac.kr")
    mbox = driver.find_element_by_xpath("//div[@class='m-box2']")

    sele_vis.tree(mbox, max_depth=2, show_text=True)
    selected_node = sele_vis.select_node(6)
    print(repr(selected_node.text))
