import time
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
wd=webdriver.Chrome()
wd.get('http://www.baidu.com')

wd.find_element(By.ID,'kw').send_keys('we')
#element.send_keys('we\n')
aa=wd.find_element(By.ID,'kw')
aaa=aa.get_attribute('value')
print(aaa)
red=wd.find_element(By.CSS_SELECTOR,'script')
print(red.get_attribute('outerHTML'))



ele_list=wd.find_element(By.CLASS_NAME,'animal')
print(ele_list.text)
tag_list=wd.find_elements(By.TAG_NAME,'span')
for t in tag_list:
    print(t.text)

#一直等待到元素出现的列子
while True: #一直循环
    try:
        w=wd.find_element(By.ID,'ddd')
        print(w)
        break #跳出循环
    except:
        time.sleep(5) 异常时休息5秒



#隐式等待
wd.implicitly_wait(10)

wd=webdriver.Chrome()
wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')

wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR,'[width="300"]'))
elements=wd.find_elements(By.CSS_SELECTOR,'.plant')
for element in elements:
    print(element.text)
    print(element.get_attribute('outerHTMl'))

wd.switch_to.default_content()
'''
