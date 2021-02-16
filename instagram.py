from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import json

def insta_down(link):
    #open browser
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    driver.set_window_position(-10000,0)
    sleep(5)
    #input username and password
    username = driver.find_element_by_name('username')
    username.send_keys('**********')               #enter your username
    password = driver.find_element_by_name('password')
    password.send_keys('**********')               #enter your password
    password.send_keys(Keys.ENTER)
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
    #get data from graphql
    data = driver.find_element_by_xpath('/html/body/script[12]').get_attribute('innerHTML')
    content = json.loads(data[59:-3])
    #get detail information
    user = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a').text
    post_ID = content.get('shortcode_media').get('shortcode')
    caption = content.get('shortcode_media').get('edge_media_to_caption').get('edges')[0].get('node').get('text')
    video_url = content.get('shortcode_media').get('video_url')
    #Close Browser
    driver.close()
    x = {
        "Username" : user,
        "Post ID" : post_ID,
        "Caption" : caption,
        "Video" : video_url
    }
    y = json.dumps(x)
    return y