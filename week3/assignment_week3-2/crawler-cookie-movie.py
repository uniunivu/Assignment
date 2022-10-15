# 抓取 PTT 電影版的網頁原始碼 (HTML)

import urllib.request as req # 網路連線
movieList=[]
def getData(url):
    # 建立一個 Request 物件，附加 Request Header 的資訊
    request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")


    # 解析原始碼，取得每篇文章的標題
    import bs4 # 載入beautifulsoup 套件
    root = bs4.BeautifulSoup(data, "html.parser") # 讓 BeautifulSoup 協助我們解析 HTML 格式文件


    titles = root.find_all("div", class_="title") # 尋找所有 class="title" 的div標籤
    # find_all 可以找到全部
    # titles以列表[]的方式跑出來
    # 用for迴圈把列表裡的每個資料都讀出來
    
    for title in titles:
        if title.a !=None: 
            if title.a.string[:4]=="[好雷]" or title.a.string[:4]=="[普雷]" or title.a.string[:4]=="[負雷]":
                movieList.append(title.a.string)
            
    # 抓取上一頁的連結
    nextLink = root.find("a", string="‹ 上頁")
    # print(nextLink["href"])
    return nextLink["href"]



# 主程序: 抓取多個頁面的標題
pageURL = "https://www.ptt.cc/bbs/movie/index.html"
# 抓取多頁資料，寫一個while迴圈，把getData函式結合pageURL一直更換放進去
count=0
while count<10:
    pageURL = "https://www.ptt.cc"+getData(pageURL) # 接收getData函式裡最後面return回來的上一頁網址資料
    count +=1
# getData(pageURL) # 接著又傳進去，一直重複
# print(pageURL)



# 處理movieList排序並且寫入movie.txt

with open("week3/assignment_week3-2/movie.txt", "w", encoding="utf-8") as file:

    for mTitle in movieList:
        if mTitle[:4] == "[好雷]":
            file.write(mTitle+"\n")

    for mTitle in movieList:
        if mTitle[:4] == "[普雷]":
            file.write(mTitle+"\n")

    for mTitle in movieList:
        if mTitle[:4] == "[負雷]":
            file.write(mTitle+"\n")
