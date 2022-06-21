# fake_product_detect
เป็นโปรเจกต์ในการตรวจสอบของปลอม ของแท้ และของโนแบรนด์
มีวัตถุประสงค์ให้คนไม่ถูกหลอกในการซื้อของปลอมจาก shopee โปรเจกต์นี้เป็นส่วนหนึ่งของโครงการ AI Builders GEN 2 จากความร่วมมือระหว่าง VISTEC, AIResearch และ Central Digital และผู้สนับสนุนเพิ่มเติมจาก VISAI, Krungsri Nimble, AWS, AIA, DELL และ Kasikorn Bank
- โดยมีแนวทางของโครงการดังนี้ https://ai-builders.github.io/orientation-2022/
- [Medium](https://medium.com/@jessadajackpranee/%E0%B8%82%E0%B8%AD%E0%B8%87%E0%B8%9B%E0%B8%A5%E0%B8%AD%E0%B8%A1%E0%B8%81%E0%B8%B1%E0%B8%9A-e-commerce-c2d1bb142e2e)
# การใช้งาน
### shopee scrape
ใครที่อยากได้ตัว scrape ให้ดูได้จากตัว notebook ข้างบนได้เลย บางทีตัวเว็บ shopee ก็มีการเปลี่ยน tag เปลี่ยน attribute บ้างดูด้วยว่ายังเป็นอันเดิมไหม
### app.py ถ้ามีการ clone ไปใช้
#### set up
- ทำการโหลด requirements.txt ให้เรียบร้อย (sudo python3 -m pip install -r requirements.txt)
- โหลด firefox (sudo apt-get install firefox)
- ให้ permission geckodriver โดยการ chmod +x geckodriver
- โมเดลเป็น .joblib ต้องโหลดเอาในตัว app.py มี RandomForestClassifier คือตัว rf_clf_model และ KNeighborsClassifier คือ knn_clf_model 
#### ใช้ window
- ให้เปลี่ยน Service (./geckodriver) > (./geckodriver.exe)
#### ใช้ ubuntu
- สามารถใช้งานได้เลย
## สุดท้ายนี้ขอบคุณทาง Ai-Builder ที่ทำให้โปรเจกต์นี้เกิดขึ้น
