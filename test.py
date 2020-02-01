from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
assert opts.set_headless
browser  = Firefox(options=opts)
browser.get('https://www.nekopost.net/manga')
# search_form = browser.find_element_by_id('project_list')
for a in browser.find_elements_by_xpath('.//ul[@id="project_list"]/a'):
    
    print ( a.find_element_by_xpath(".//b").text)
    print(a.get_attribute('href'))
    
browser.quit()

