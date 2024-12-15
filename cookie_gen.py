from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime

def real_time():
    now=datetime.now()
    start_time = int(now.strftime("%M"))
    start_time=start_time * 60
    start_time=start_time+int(now.strftime("%S"))
    return start_time


options = Options()

options.add_experimental_option("detach",True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_button=driver.find_element(By.XPATH,'//*[@id="cookie"]')


items=[]

def filter(list):
    list=list.split('-')[-1].strip()
    return list
cookie_details = driver.find_elements(By.ID,'store')

def events():
    new_list = []
    new_list2 = []
    current_cookie_size=driver.find_element(By.XPATH,value='//*[@id="money"]')
    current_cookie_size=int(current_cookie_size.text.replace(',', ''))

    new_list2.clear()
    if len(new_list)>0 or len(new_list)==0:
        new_list.clear()
        cursor_Price=driver.find_element(By.XPATH,value='//*[@id="buyCursor"]/b')
        cursor_Price=int(filter(cursor_Price.text))

        cursor_price_click=driver.find_element(By.XPATH,value='//*[@id="buyCursor"]')

        new_list.append(cursor_Price)

        grandma_price=driver.find_element(By.XPATH,value='//*[@id="buyGrandma"]/b')
        grandma_price=int(filter(grandma_price.text))
        grandma_price_click=driver.find_element(By.XPATH,value='//*[@id="buyGrandma"]')

        new_list.append(grandma_price)

        factory_price=driver.find_element(By.XPATH,value='//*[@id="buyFactory"]/b')
        factory_price=int(filter(factory_price.text).replace(',',''))

        factory_price_click=driver.find_element(By.XPATH,value='//*[@id="buyFactory"]')

        new_list.append(factory_price)
        mine_price=driver.find_element(By.XPATH,value='//*[@id="buyMine"]/b')
        mine_price=int(filter(mine_price.text).replace(',',''))

        mine_price_click=driver.find_element(By.XPATH,value='//*[@id="buyMine"]')

        new_list.append(mine_price)

        shipment_price = driver.find_element(By.XPATH,value='//*[@id="buyShipment"]/b')
        shipment_price=int(filter(shipment_price.text).replace(',',''))

        shipment_price_click=driver.find_element(By.XPATH,value='//*[@id="buyShipment"]')

        new_list.append(shipment_price)

        alcamey_lab_price= driver.find_element(By.XPATH,value='//*[@id="buyAlchemy lab"]/b')
        alcamey_lab_price=int(filter(alcamey_lab_price.text).replace(',',''))

        alcamey_lab_price_click=driver.find_element(By.XPATH,value='//*[@id="buyAlchemy lab"]')
        new_list.append(alcamey_lab_price)

        portal_price=driver.find_element(By.XPATH,value='//*[@id="buyPortal"]/b')

        portal_price=int(filter(portal_price.text).replace(',',''))

        portal_price_click=driver.find_element(By.XPATH,value='//*[@id="buyPortal"]')

        new_list.append(portal_price)
        time_machine_price = driver.find_element(By.XPATH,value='//*[@id="buyTime machine"]/b')
        time_machine_price=int(filter(time_machine_price.text).replace(',',''))
        time_machine_price_click=driver.find_element(By.XPATH,value='//*[@id="buyTime machine"]')
        new_list.append(time_machine_price)

    for check in new_list:

        if current_cookie_size>=check:
            new_list2.append(check)
    if len(new_list2)!=0:
        high_item=max(new_list2)

        if high_item ==cursor_Price:
            cursor_price_click.click()
        elif high_item==grandma_price:
             grandma_price_click.click()
        elif high_item== factory_price:
            factory_price_click.click()
        elif high_item==mine_price:
            mine_price_click.click()
        elif high_item==shipment_price:
            shipment_price_click.click()
        elif high_item== alcamey_lab_price:
            alcamey_lab_price_click.click()
        elif high_item==time_machine_price:
            time_machine_price_click.click()
        elif high_item==portal_price:
            portal_price_click.click()

duration = 5*60

new_time=real_time()+duration
i=5

new_time1=real_time()+5

time_s=real_time()

while(real_time()<new_time):
    cookie_button.click()

    if real_time()>new_time1+i:
        events()
        i+=5
        new_time1=real_time()+5





