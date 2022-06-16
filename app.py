from time import time
import pandas as pd
import streamlit as st
from joblib import load
#import os, sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import bs4
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from selenium.webdriver.common.keys import Keys
import numpy as np
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.edge.service import Service
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.service import Service
import geckodriver_autoinstaller

clf = load('clf_model.joblib')
st.title('Aibuilder-Project')
st.header('Fake product detect')
st.subheader('โมเดลนี้เป็นโมเดลสำหรับแยกของปลอม ของแท้ และของไม่มีแบรนด์')
st.write('มีวัตถุประสงค์ให้คนไม่ถูกหลอกในการซื้อของปลอมจาก shopee โปรเจกต์นี้เป็นส่วนหนึ่งของโครงการ AI Builders GEN 2 จากความร่วมมือระหว่าง VISTEC, AIResearch และ Central Digital และผู้สนับสนุนเพิ่มเติมจาก VISAI, Krungsri Nimble, AWS, AIA, DELL และ Kasikorn Bank')

opts = FirefoxOptions()
opts.add_argument("--headless")
service = Service('./geckodriver')
driver = webdriver.Firefox(
    options=opts,
    service=service,
)

wait=WebDriverWait(driver, 10) #ไว้ wait
def k_and_m_to_float(txt):
    "ฟังก์ชันเพื่อเปลี่ยน k เป็น 1000 เปลี่ยน m เป็น 1000000 เปลี่ยนเป็น float"
    if txt[-1]=="k":
        txt=(float(txt[:-1])*1000)
    elif txt[-1]=="m":
        txt=(float(txt[:-1])*1000000)
    else:
        txt=(float(txt))
    return txt

def hours_convert(txt):
    "ฟังก์เพื่อเปลี่ยนทุกหน่วยเป็นหน่วยชั่วโมง"
    if txt[-10:]==' years ago':
        txt=float(txt[:-10])*360*24
    elif txt[-10:]==' hours ago':
        txt=float(txt[:-10])
    elif txt[-11:]==' months ago':
        txt=float(txt[:-11])*30*24
    elif txt[-9:]==' days ago':
        txt=float(txt[:-9])*24
    else:
        txt=(float(0))
    return txt

def data_scraping(datatype,positiondata,tag,attribute,L):
    try:
        wait.until(EC.visibility_of_element_located((datatype,positiondata)))
        soup=bs4.BeautifulSoup(driver.page_source)
        L.append(soup.find(tag,{'class':attribute}).text)
    except:
        L.append("None")

def scrape():
    w=(url_L[0])
    new_url_L.append(w)
    #st.write(len(new_url_L))
    driver.get(w)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,f"/html/body/div[2]/div[1]/div[1]/div/div[3]/div[2]/button")))
    eng_button=driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[1]/div/div[3]/div[2]/button")
    eng_button.click()

    driver.set_context("chrome")
    win = driver.find_element(By.TAG_NAME, "html")
    win.send_keys(Keys.CONTROL + "-" + "-" + "-"+ "-"+ "-"+ "-"+ "-" + "-"+ "-"+ "-"+ "-")
    driver.set_context("content") 
    driver.execute_script("window.scrollTo(0, 1000)") 
    #ชื่อสิ้นค้า
    data_scraping(By.CSS_SELECTOR,".VCNVHn",'div','VCNVHn',name_L)
    #ราคา
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,f".pmmxKx")))
        soup=bs4.BeautifulSoup(driver.page_source)
        try:
            price_L.append(float(soup.find('div',{'class':'pmmxKx'}).text.replace(",",'').replace("฿","")))
        except:
            price_L.append(float((soup.find('div',{'class':'pmmxKx'}).text.replace(",",'').replace("฿","")).partition(' - ')[0]))
    except:
        price_L.append("None")
    #จำนวนที่ขาย
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,f"._45NQT5")))
        soup=bs4.BeautifulSoup(driver.page_source)
        sold=(soup.find('div',{'class':'_45NQT5'}).text)
        sold_L.append(k_and_m_to_float(sold))
    except:
        sold_L.append('None')
    #จำนวนคนรีวิว
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,f"div.HXGLyo:nth-child(2) > div:nth-child(1)")))
        soup=bs4.BeautifulSoup(driver.page_source)
        amount_reviewer=(((soup.find_all('div',{'class':'MrYJVA'}))[1]).text)
        amount_reviewer_L.append(k_and_m_to_float(amount_reviewer))
    except:
        amount_reviewer_L.append(float(0))
    #จำนวนคนรีวิวร้านค้าทั้งหมด
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,f"div.MSPJbO:nth-child(1) > div:nth-child(1) > span:nth-child(2)")))
        soup=bs4.BeautifulSoup(driver.page_source)
        all_store_reviewer=((soup.find_all('span',{'class':'_32ZDbL'}))[0].text)
        all_store_reviewer_L.append(k_and_m_to_float(all_store_reviewer))
    except:
        all_store_reviewer_L.append('None')
    #จำนวนสินค้าทั้งหมดของร้านค้า
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,f".g54jiy")))
        soup=bs4.BeautifulSoup(driver.page_source)
        all_product_store_L.append(k_and_m_to_float((soup.find('span',{'class':'_32ZDbL g54jiy'}).text)))
    except:
        all_product_store_L.append('None')
    #อัตราการตอบกลับของร้านค้า
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,f"div.MSPJbO:nth-child(2) > div:nth-child(1) > span:nth-child(2)")))
        soup=bs4.BeautifulSoup(driver.page_source)
        response_rate_L.append(float((soup.find_all('span',{'class':'_32ZDbL'}))[2].text.replace('%','')))
    except:
        response_rate_L.append('None')
    #จำนวนผู้ติดตาม
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,f"div.MSPJbO:nth-child(3) > div:nth-child(2) > span:nth-child(2)")))
        soup=bs4.BeautifulSoup(driver.page_source)
        follower_L.append(k_and_m_to_float((soup.find_all('span',{'class':'_32ZDbL'}))[5].text))
    except:
        follower_L.append('None')
    #เข้าร่วมเมื่อกี่ชั่วโมงแล้ว
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,f"div.pHNb7U:nth-child(1) > span:nth-child(2)")))
        soup=bs4.BeautifulSoup(driver.page_source)
        joined_L.append(hours_convert((soup.find_all('span',{'class':'_32ZDbL'}))[4].text))
    except:  
        joined_L.append('None')
    #rating
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,f".Ga-lTj")))
        soup=bs4.BeautifulSoup(driver.page_source)
        rating_L.append(float((soup.find('div',{'class':'MrYJVA Ga-lTj'})).text))
    except:
        rating_L.append(float(0))

with st.form("my_form",True):
    title = st.text_input('Please enter the shopee url', '',placeholder="Link shopee product")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        url_L=[]
        name_L=[]
        price_L=[]
        sold_L=[]
        amount_reviewer_L=[]
        all_store_reviewer_L=[]
        all_product_store_L=[]
        response_rate_L=[]
        follower_L=[]
        joined_L=[]
        rating_L=[]
        new_url_L=[]
        t0 = time.time()
        url_L.append(title)
        scrape()
        shopee=pd.DataFrame([new_url_L,name_L,price_L,sold_L,amount_reviewer_L,all_store_reviewer_L,all_product_store_L,response_rate_L,follower_L,joined_L,rating_L]).transpose()
        shopee.columns=['url','name','price','sold','amount reviewer','all reviewer of store','amount product','response rate','follower','joined','rating']
        st.write(shopee)
        chaper=clf.predict_proba(shopee.drop(['url','name'],axis=1))
        st.write(chaper)
        cha=clf.predict(shopee.drop(['url','name'],axis=1))
        st.write(cha)
        st.write(f'### มีโอกาสเป็นของปลอม {round(chaper[0,0]*100)} %')
        st.write(f'### มีโอกาสเป็นของแท้ {round(chaper[0,1]*100)} %')
        st.write(f'### มีโอกาสเป็นของไม่มีแบรนด์ {round(chaper[0,2]*100)} %')
        type_L=['ปลอม','แท้','ไม่มีแบรนด์']
        st.write(f'## มีโอกาสเป็นของ{type_L[cha[0]]}มากที่สุด')
        t1 = time.time()
        st.write('เวลาในการคำนวณ: %f'%(t1-t0))
        driver.quit()
