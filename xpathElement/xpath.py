print('-----------xpath----------')
'''
方法1.使用单斜杠 / ，若存在多个相同元素，定位其中一个时，下标从1开始
        如：  /html/body/div/div[4]/div/div/p/a[1]
方法2.使用双斜杠 //xxx ，表示从根节点/开始，选择所有为xxx的元素
        如：  //div[4]/div/div/p/a[2]
方法3.使用多组合的双斜杠 //aa//bb ，表示从根节点开始所有aa元素下的bb元素
        如：  //div[4]//p[2]//a[2]
方法4.//div/*[1]  表示div下的所有类型元素的第一个
方法5.//div/span[last()]  表示选择div下的span标签元素的最后一个，倒数第二个为 last()-1
扩展方法6.//*[@id='kw']//*[position()<=2] 表示选择所有id为kw下的前两个元素
扩展方法6.//*[@id='kw']//*[position()>last()-3] 表示选择所有id为kw下的最后三个元素

根据属性选择：
1.//*[@style]                       表示所有具有style属性的元素
2.//p[@spec='len2']                 表示所有p元素中具有spec值为len2的元素
3.//div[@id='kw']                   表示所有div元素中具有id值为kw的元素
4.//div[@class='bg s_btn_wr']       表示所有div元素中具有id值为kw的元素

组选择：
css 用,隔开    如： p,button         consoles中使用方法：$("p,button")，依次找p，button
xpath 用|隔开  如： //p | //button   consoles中使用方法：$x("//p | //button")，先找p，后找button

扩展使用：
//*[@id='food']/following-sibling::div  表示id为food的后边的类型为div的兄弟节点
//*[@id='food']/preceding-sibling::div  表示id为food的前边的类型为div的兄弟节点

food=driver.find_element_by_id("food")
eles=food.find_element_by_xpath(".//p")
## .// 表示在当前food元素之后找p，如果不加.则表示从根目录/开始找p




'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get('https://www.baidu.com')

ele1 = driver.find_element_by_xpath('/html/body/div/div[4]/div/div/p/a[1]')
print(ele1.text)

ele2 = driver.find_element_by_xpath('//div[4]/div/div/p/a[2]')
print(ele2.text)

ele3 = driver.find_element_by_xpath('//div[4]//p[2]//a[2]')
print(ele3.text)
'''
1.//*[@style]           表示所有具有style属性的元素
2.//p[@spec='len2']     表示所有p元素中具有spec值为len2的元素
3.//div[@id='kw']       表示所有div元素中具有id值为kw的元素
4.//div[@class='bg s_btn_wr']       表示所有div元素中具有id值为kw的元素
'''
ele4 = driver.find_element_by_xpath('//input[@name="wd"]')
print(ele4.get_attribute('name'))

ele5 = driver.find_element_by_xpath('//span[@class="tools"]//div')
print(ele5.get_attribute('id'))

ele6 = driver.find_element_by_xpath('//div[4]//p[2]//a[last()]')
print('使用last()定位最后一个元素：'+ele6.text)

ele7 = driver.find_element_by_xpath('//div[4]//p[2]//a[last()-1]')
print('使用last()-1 定位倒数第二个元素：'+ele7.text)




driver.quit()

