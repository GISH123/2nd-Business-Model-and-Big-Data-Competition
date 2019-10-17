# 第二屆 商業模式與大數據分析競賽-人工智慧挑戰賽  
## 本次競賽主題：「最適金融商品預測」。參賽隊伍需由台新銀行提供2018年下半年各月信用卡消費及持有資產狀態等個人金融行為擬真資料中，預測於2019年1月，是否會申辦信用貸款與申購基金產品。  

# To view codes, please use NBViewer online.

# To know what ive done,please refer to the folders,each folder has its readme, read it there. Thank you!

流程圖(2019.10.17)：
1. Data preprocessing
https://github.com/GISH123/2nd-Business-Model-and-Big-Data-Competition/tree/master/Preprocessing 
 把raw data四個表融合成一個表，沒處理sr_1.csv這個每筆消費的資料

2. Feature Engineering
https://github.com/GISH123/2nd-Business-Model-and-Big-Data-Competition/tree/master/Feature%20engineering  
這邊主要生成各種資產類別as_X的變化量(該月減掉上個月)，後來用另一個方法快很多，已經算出來了
3. Catboost Modeling

https://github.com/GISH123/2nd-Business-Model-and-Big-Data-Competition/tree/master/catboost%20modeling/version2(f1%20score%20=%200.1514)  

想請老師直接看code，很短而且我刪掉了沒必要的code其實就只是把前面生出的csv檔，弄成catboost可以吃的形式餵進去學習目前我直接把時間刪掉，還沒想出有關時間的feature根據新的as變化量features，下去學這樣f1 score為0.1514

後續想法：首先我應該會試一下LightGBM這演算法再來如果還有時間我將會使用emsemble的Stacking方法，目前想法大概是做兩層，第一層就是catboost + LightBGM ( + 有時間的話我甚至還想專門處理sr_1.csv這的檔案，專門用NLP演算法來處理 ，或是簡單的計算RFM也可以)第二層就一個logistic regression把這兩個或三個演算法集合起來
再來Feature engineering的部分我也覺得還可以再加強，但實在是目前想不到更有意義的feature
