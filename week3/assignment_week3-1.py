# 要求一 ok
import urllib.request as request
import json # 要做json的資料解析
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response) # 利用 json 模組，處理 json 資料格式

list = data["result"]["results"]
# print(list)
import csv
with open("week3/data.csv","w", encoding="utf-8-sig", newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['景點名稱','區域','經度','緯度','第一張圖檔網址'])
    for listItem in list:

        date = int(listItem['xpostDate'][0:4])
        if  date>=2015:
            changeImg = listItem['file'].replace(".JPG",".jpg") # 將檔名的大小寫改成一致
            # print(changeImg)
            img = changeImg.split('.jpg') # 以.jpg切割，把圖片一個個分開，split()回傳之後，會形成一個List
            # print(img[0]+".jpg")
            # print(listItem['stitle'], listItem['address'][4:8], listItem['longitude'], listItem['latitude'], img[0]+".jpg")
            dataList = [listItem['stitle'], listItem['address'][4:8], listItem['longitude'], listItem['latitude'], img[0]+".jpg"]
            writer.writerow(dataList)

