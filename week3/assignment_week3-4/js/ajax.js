// 網頁一載入就執行連線的function
document.body.onload = insertData;

function insertData() {

    // 利用 fetch 連線，並取得資料
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response){
        return response.json(); // json 格式的資料，要用json()去做資料解讀
    }).then(function(data){

        // 已經取得資料 data
        // console.log(data.result.results); // 物件 > 物件 > 陣列
        let dataArray = data.result.results; // 取得陣列
        // console.log(dataArray.length); //共58筆資料
        // 用 for 迴圈，把陣列的物件，一個一個讀出來

        //titlebox的部分 迴圈 1
        for(let i=0; i < 2; i++){
            let attraction = dataArray[i];
            
            // 景點名稱
            // console.log(attraction.stitle); // 物件 成員stitle
            
            // 第一張圖片
            // JPG 轉換 jpg，並做字串切割，找到第一張圖檔名
            let file = attraction.file;
            let regJpg = new RegExp(/JPG/g); // 正則表達式，把JPG找出來，g 是全域搜尋
            newFile = file.replace(regJpg,"jpg"); // 把 JPG 換成 jpg
            // console.log(newFile);
            splitFile = newFile.split(".jpg"); // 切割圖檔名稱，把.jpg拿掉
            // console.log(splitFile); // 形成陣列
            // console.log(splitFile[0]+".jpg"); // 找出陣列的第一張，印出jpg
            
            // 建立節點，不破壞原本結構
            let titlebox = document.getElementsByClassName("titlebox")[0];
            let box = document.createElement("div");
            let boxphoto = document.createElement("div");
            let boxtitle = document.createElement("div");
            let boxphotoImg = document.createElement("img");
            box.className = "box";
            boxphoto.className = "boxphoto";
            boxtitle.className = "boxtitle";
            titlebox.appendChild(box);
            box.appendChild(boxphoto);
            box.appendChild(boxtitle);
            boxphoto.appendChild(boxphotoImg);
            

            // 放資料
            boxphotoImg.src = splitFile[0]+".jpg"; //圖片
            let titleText = document.createTextNode(attraction.stitle);  //標題
            boxtitle.appendChild(titleText);

        };
        
        // photobox的部分 迴圈 2 
        for(let i = 2; i < 10; i++) {
            let attraction = dataArray[i]; // 物件

            // 景點名稱
            // console.log(attraction.stitle); // 物件中的成員 stitle

            // 第一張圖片
            let file = attraction.file;
            let regJpg = new RegExp(/JPG/g); // 正則表達式，把JPG找出來，g 是全域搜尋
            newFile = file.replace(regJpg,"jpg"); // 把 JPG 換成 jpg
            splitFile = newFile.split(".jpg"); // 切割圖檔名稱，把.jpg拿掉
            // console.log(splitFile[0]+".jpg");


            // 建立節點，不破壞原本結構
            let content = document.getElementsByClassName("content")[0];
            let photobox = document.createElement("div");
            let photo = document.createElement("div");
            let photo_text = document.createElement("div");
            let starImg = document.createElement("img");
            let photoImg = document.createElement("img");
            photobox.className = "photobox";
            photo.className = "photo";
            photo_text.className = "photo_text";

            content.appendChild(photobox);
            photobox.appendChild(starImg);
            photobox.appendChild(photo);
            photobox.appendChild(photo_text);
            photo.appendChild(photoImg);


            //放資料
            starImg.src = "./images/04_star.png";
            photoImg.src = splitFile[0]+".jpg";
            let photo_text_title = document.createTextNode(attraction.stitle);
            photo_text.appendChild(photo_text_title);
        };

        // 按鈕增加資料
        let btn = document.getElementById("btn");
        let start = 2;
        let end = 10;
        let photoboxAdd = 8;
        btn.addEventListener("click",addphotobox);
        function addphotobox() {
            start = start + photoboxAdd;
            end = end + photoboxAdd;
            // console.log(start);
            // console.log(end);
            if ( end >= 58 ) {
                // 達到第58個資料時，按鈕即無法再按
                btn.style.display = "none";
                // btn.disabled = true;
            }

            for(let i = start; i < end; i++) {
                let attraction = dataArray[i]; // 物件
    
                // 景點名稱
                // console.log(attraction.stitle); // 物件中的成員 stitle
    
                // 第一張圖片
                let file = attraction.file;
                let regJpg = new RegExp(/JPG/g); // 正則表達式，把JPG找出來，g 是全域搜尋
                newFile = file.replace(regJpg,"jpg"); // 把 JPG 換成 jpg
                splitFile = newFile.split(".jpg"); // 切割圖檔名稱，把.jpg拿掉
                // console.log(splitFile[0]+".jpg");
    
    
                // 建立節點，不破壞原本結構
                let content = document.getElementsByClassName("content")[0];
                let photobox = document.createElement("div");
                let photo = document.createElement("div");
                let photo_text = document.createElement("div");
                let starImg = document.createElement("img");
                let photoImg = document.createElement("img");
                photobox.className = "photobox";
                photo.className = "photo";
                photo_text.className = "photo_text";
    
                content.appendChild(photobox);
                photobox.appendChild(starImg);
                photobox.appendChild(photo);
                photobox.appendChild(photo_text);
                photo.appendChild(photoImg);
    
    
                //放資料
                starImg.src = "./images/04_star.png";
                photoImg.src = splitFile[0]+".jpg";
                let photo_text_title = document.createTextNode(attraction.stitle);
                photo_text.appendChild(photo_text_title);
            };
        };
    });



};
