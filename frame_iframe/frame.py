print('...frame/iframe 练习...')
'''
1. frame标签定义了放置在每个框架中的HTML文档
2. iframe标签用于在网页中显示网页，嵌套网页
3. 
'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)   ##隐式等待5秒钟
driver.get('https://music.163.com/#/discover/toplist/')
'''
切换到frame/iframe中 :推荐方法1
方法1. driver.switch_to.frame('xxx') ## frame_reference= ? 
      frame_reference值为name属性或ID属性
方法2. 索引值(从0开始)：0
方法3. frame对应的webElement：driver.find_element_by_tag_name('iframe')
'''
# driver.switch_to.frame('contentFrame')  ##使用iframe的name属性
driver.switch_to.frame('g_iframe')  ##使用iframe的id属性
top100 = driver.find_element_by_id('song-list-pre-cache')
print(top100.text)
'''
切换回HTML页面中，从frame/iframe中切回来
'''
## 跳出当前一级表单
driver.switch_to.parent_frame()
## 多级表单时，跳回最外层的页面
# driver.switch_to.default_content()
backto = driver.find_element_by_id('g-topbar')
print(backto.text)

driver.quit()
