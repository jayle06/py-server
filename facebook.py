from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

def fb_down_vd(link):
    #open web 
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    driver.set_window_position(-10000,0)

    #fill username and passord into input text
    username = driver.find_element_by_name("email")
    username.send_keys('**********')               #enter your username
    password = driver.find_element_by_name('pass')
    password.send_keys('**********')               #enter your password
    password.send_keys(Keys.ENTER)
    sleep(10)
    #get source page
    page_source= driver.page_source
    #close window
    driver.close()
    #get postion of video
    SD_posi = page_source.find('"playable_url"')
    HD_posi = page_source.find('"playable_url_quality_hd"')
    HD_posi2 = page_source.find('"spherical_video_fallback_urls"')
    id1 = page_source.find('"videoId"')
    id2 = page_source.find('"isPremiere"')
    #get data
    SD_URL = page_source[SD_posi+len('"playable_url":"'):HD_posi-2].replace("\\","")
    HD_URL = page_source[HD_posi+len('"playable_url_quality_hd":"'):HD_posi2-2].replace("\\","")
    video_id = page_source[id1+len('"videoId":"'):id2-2]
    #generate
    x = {
    "Video ID" : video_id,
    "Download" :{
        "Video HD" : HD_URL,
        "Video SD" : SD_URL,
        }
    }
    return x