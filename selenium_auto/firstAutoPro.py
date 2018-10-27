'''
web自动化的操作流程：
1.选择界面元素
2.操作界面元素
    输入操作：点击、输入文字、拖拽等
    输出操作：获取元素的各个属性
3.根据界面上获取的数据进行分析和处理
'''
''''
第一个web自动化程序练习
html 页面元素
1.  <image src="d:/image.jpg" />
2.  <table>
        <thead> ### table的标题栏
        <tbody> ### table中具体的内容
            <tr>    ### table中的每一行
                <td>    ###table中的每一列
3.  <div>   ###块级元素，将元素按块区域存放布局，类似于文件夹功能
'''
'''
web元素的选择和操作
1.text属性--显示该元素在web页面显示出来的文本内容
2.get_attribute('xx')--获取元素的属性
3.get_attribute('outerHTML')--获取当前元素对应的html文本
4.get_attribute('innerHTML')--获取当前元素对应的内部部分html文本
5.Beautiful Soup 4.x.x 是一个从HTML或XML文件中提取数据的Python库
    pip install beautifulsoup4
    pip install html5lib
  soup = BeautifulSoup(alltext,"html5lib")
6. find_element_by_id
7. find_element_by_name
8. find_element_by_tag_name  <iframe src="..."> XXX </iframe>
9. find_element_by_link_text
10.find_element_by_partial_link_text
11.等待操作的三种实现方法：
    直接等待    sleep(2)
    隐式等待    driver.implicitly_wait(5) 对所有driver对象相关的find_xxx方法适用，全局性。
    显式等待    跟全局等待的时间不一致的，或多或少的，可以用显式等待。

'''
# print('---------第一个web自动化程序练习---------')
import time
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
### 使用具体路径的chromedriver.exe文件
# driver = webdriver.Chrome(r"D:\Program Files\Python\Python36\chromedriver.exe")
driver.get("http://www.baidu.com")
# find_element = driver.find_element_by_id("kw")
find_element = driver.find_element_by_id("u1")
## 练习使用get_attribute方法
# print(find_element.get_attribute('name'))
# print(find_element.get_attribute('outerHTML'))
# print(find_element.get_attribute('innerHTML'))
## 练习使用BeautifulSoup库用法
alltext = find_element.get_attribute('outerHTML')
print(alltext)
soup = BeautifulSoup(alltext,"html5lib")
## 返回一个 <class 'bs4.element.Tag'>实例
# print(soup.a.string)
# print(soup.a.get_text())
print(soup.find('a').get_text())  ##获取第一个标签为a的就返回
print(soup.find('a',href="http://v.baidu.com").get_text())  ##获取标签为a,href=xx的标签属性值
print(soup.find_all('a')[1].get_text()) ##获取指定的第二个标签a
print(soup.find_all('a')[2]['href'])    ##获取指定位置标签的属性的值

find_name = driver.find_element_by_name("wd")
# find_name = driver.find_elements_by_name("wd")  ##用 s 找所有的
print('使用find_element_by_name查找:'+ find_name.get_attribute("id"))

# find_class = driver.find_element_by_class_name("mnav")
find_class = driver.find_elements_by_class_name("mnav")  ##用 s 找所有的
for classes in find_class:
    # print(classes.get_attribute('outerHTML'))
    print(classes.get_attribute("href"))
# print(classes.__str__())

# find_tagname = driver.find_element_by_tag_name()
# time.sleep(1)
driver.implicitly_wait(5)
find_link = driver.find_element_by_link_text("新闻")
find_link.click()
# time.sleep(1)
find_partial_link = driver.find_element_by_partial_link_text("贴")
find_partial_link.click()
## 显式等待操作
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EXP
from selenium.webdriver.common.by import By
ele = WebDriverWait(driver,2).until(EXP.presence_of_element_located((By.ID,'com_userbar')))
if ele.text.startswith('今日头条一定是头条新闻...'):
    print('pass')
else:
    print('not pass')



driver.quit()
'''
find_element.send_keys("今日头条")
find_button = driver.find_element_by_id("su")
find_button.click()

import time
time.sleep(1)
find_ret_text = driver.find_element_by_id("2")
print(find_ret_text.text)
if find_ret_text.text.startswith("今日头条_百度百科"):
    print("测试通过，已经找到今日头条的百度百科！")
else:
    print("测试失败，没找到今日头条的百度百科！")

# driver.quit()

'''
