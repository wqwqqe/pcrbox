from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from zhconv import convert
import urllib.request as ur
from tqdm import tqdm
import json

url = "https://pcredivewiki.tw/Character"
browser = webdriver.Chrome()
browser.get(url)
path = './source/character/'
headers = {"User-Agent",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}

opener = ur.build_opener()
opener.addheaders = [headers]
character = {}
ur.install_opener(opener)
id = 1
for i in range(2, 5, 1):
    for j in tqdm(range(1, 100, 1)):
        xpath = "".join(['//*[@id="app"]/div[2]/div/div/div/div/div/div[', str(i), ']/div[', str(j), ']/a/div/div'])
        elements = browser.find_elements_by_xpath(xpath)
        if len(elements) == 0:
            break
        temp = {}
        for element in elements:
            name = element.text
            new_name = convert(name, 'zh-cn')
            temp["new_name"] = name
            temp["name"] = name
            temp['id'] = id
            temp['origin_star'] = 5 - i
            character[name] = temp
            id += 1
        xpath = "".join([xpath, "/img"])
        elements = browser.find_elements_by_xpath(xpath)
        for element in elements:
            img_url = element.get_attribute('src')
            img_data = ur.urlopen(img_url).read()
            save_path = "".join([path, name, ".png"])
            f = open(save_path, 'wb')
            f.write(img_data)
            f.close()
fw = open("".join([path, "id.json"]), 'w', encoding='utf-8')
fw.write(json.dumps(character, ensure_ascii=False) + '\n')
fw.close()
