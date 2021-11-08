""" %%capture
import sys
!pip install selenium
#!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver') """

pip install pytube==11.0.1

import os
from pytube import YouTube
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

ROOT_DIR = os.getcwd()

def get_youtube_url(name):
    """
    This functions gets youtube video links
    Args:
        name: The name of the object
    Returns:
        video_links: A list of video links sourced from youtube
    """
    video_links = []

    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    #driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

    driver = webdriver.Chrome(
       '/home/samuel/Downloads/Compressed/chromedriver')
    
    query = f"https://www.youtube.com/results?search_query={name}"
    driver.get(query)

    try:
        links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, "thumbnail")))
    except:
        pass
    for link in links:
        video_links.append(link.get_attribute("href"))

    return video_links


def get_youtube_video(url, vid_name):

    """
    This function downloads a youtube video to the local directory
    Args:
        url: A youtube video URL link
        vid_name: A name to save the video
    Retunrs:
        None
    """
    
    count = 0
    new_path = os.path.join(ROOT_DIR, "ytube_videos")
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    
    rname_vid_path = '%s/%s.mp4' % (new_path, vid_name)
    if os.path.exists(rname_vid_path):
        nrname_vid_path = '%s/%s%s.mp4' % (new_path, vid_name, count)
        os.rename(rname_vid_path, nrname_vid_path)
         
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download(new_path)

    new_fname = '%s/%s' % (new_path, ys.default_filename)
    os.rename(new_fname, rname_vid_path)