print('---css选择器高级用法上---30:00时间---功能实现---')
print('---访问51job，按内容和地区搜索并将搜索结果返回---')
print('--------------------------------------------')
print('对于输入框自动提示掩盖住了下面的选择框，可以先点击空白处的某个元素，之后在接着操作')
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get('https://www.51job.com')
driver.maximize_window()    ## 窗口全屏显示
driver.find_element_by_id('kwdselectid').send_keys("web自动化测试")
driver.find_element_by_id('work_position_input').click()
time.sleep(1)
cityEles = driver.find_elements_by_css_selector(
    '#work_position_click_center_right_list_000000 em'
)
for city in cityEles:
    cityName = city.text
    selected = city.get_attribute('class') == 'on'

    if(cityName == '上海' and not selected) or (cityName != '上海' and selected):
        city.click()
citySelectedName = driver.find_elements_by_css_selector(
    '#work_position_click_multiple_selected > span > span'
)
for selectedName in citySelectedName:
    if selectedName.text != '上海':
        selectedName.click()

driver.find_element_by_id('work_position_click_bottom_save').click()
driver.find_element_by_css_selector('.ush button').click()

jobs = driver.find_elements_by_css_selector('.dw_table div.el')
for job in jobs[1:]:
    contents = job.find_elements_by_tag_name('span')
    print('|'.join([content.text for content in contents]))

driver.quit()
