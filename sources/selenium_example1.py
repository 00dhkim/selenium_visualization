import time
from selenium import webdriver

element_list = []
idx = 0

def tree2(node, depth, max_depth, show_text):
    global element_list
    global idx
    
    if max_depth != -1 and depth > max_depth:
        return
    
    print(' '*depth*2,'',node.tag_name, '[',idx,'] ', sep='', end='')
    if show_text:
        print(repr(node.text[:20]),sep='', end='')
    print()
    
    element_list.append(node)
    idx += 1
    
    sub_nodes = node.find_elements_by_xpath("child::*")
    if not sub_nodes:
        return
    for nd in sub_nodes:
        tree2(nd, depth+1, max_depth, show_text)

def tree(node, max_depth = -1, show_text = False):
    global element_list
    global idx
    element_list = []
    idx = 0
    
    tree2(node, 0, max_depth, show_text)

def select_node(idx):
    return element_list[idx]


driver = webdriver.Chrome("chromedriver_83.exe")

driver.get("http://lms.knu.ac.kr")

login_btn = driver.find_element_by_xpath("//div[@class='header_login_img']")
login_btn.click()
driver.implicitly_wait(10)

driver.find_element_by_id("usr_id").send_keys("ID")
driver.find_element_by_id("usr_pwd").send_keys("PASSWORD")
driver.find_element_by_id("login_btn").click()
time.sleep(1)

driver.switch_to.alert.accept()
driver.get("http://lms.knu.ac.kr")

logo = driver.find_element_by_id("logo_link")
print(logo.get_attribute("style"))

mbox = driver.find_element_by_xpath("//div[@class='m-box2']")

# tree(mbox, max_depth = 2, show_text = True)
