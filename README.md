決賽 :  
2019/12/11 上傳決賽之Code 在"決賽"這個資料夾  
執行順序：  
preprocess_and_eda.ipynb -> sr_X feature engineering.ipynb -> Catboost_Modeling.ipynb(純粹拿來試驗參數與模型建置，不跑這個也沒關係)  
-> Catboost_final_to_predict_201901.ipynb -> combine_predictions.ipynb



以下為初賽的東西  
# 第二屆 商業模式與大數據分析競賽-人工智慧挑戰賽  
## 本次競賽主題：「最適金融商品預測」。參賽隊伍需由台新銀行提供2018年下半年各月信用卡消費及持有資產狀態等個人金融行為擬真資料中，預測於2019年1月，是否會申辦信用貸款與申購基金產品。  

# To view codes, please use NBViewer online.

# To know what ive done,please refer to the folders,each folder has its readme, read it there. Thank you!

## 流程圖(2019.10.17)：
1. Data preprocessing
https://github.com/GISH123/2nd-Business-Model-and-Big-Data-Competition/tree/master/Preprocessing 
 把raw data四個表融合成一個表，沒處理sr_1.csv這個每筆消費的資料

2. Feature Engineering
https://github.com/GISH123/2nd-Business-Model-and-Big-Data-Competition/tree/master/Feature%20engineering  
這邊主要生成各種資產類別as_X的變化量(該月減掉上個月)，後來用另一個方法快很多，已經算出來了

3. Catboost Modeling (can skip this process, its just for my own evaluation of the model)

https://github.com/GISH123/2nd-Business-Model-and-Big-Data-Competition/tree/master/catboost%20modeling/version2(f1%20score%20=%200.1514)  

我刪掉了沒必要的code，其實就只是把前面生出的csv檔，弄成catboost可以吃的形式餵進去學習  
目前我直接把時間刪掉，還沒想出有關時間的feature根據新的as變化量features，下去學這樣f1 score為0.1514

後續想法：首先我應該會試一下LightGBM這演算法再來如果還有時間我將會使用emsemble的Stacking方法，目前想法大概是做兩層，第一層就是catboost + LightBGM ( + 有時間的話我甚至還想專門處理sr_1.csv這的檔案，專門用NLP演算法來處理 ，或是簡單的計算RFM也可以)第二層就一個logistic regression把這兩個或三個演算法集合起來
再來Feature engineering的部分我也覺得還可以再加強，但實在是目前想不到更有意義的feature


## 流程圖(2019.10.21): 
## 所有程式都在better method(2019.10.21) folder下執行

發現如果要預測201901的購買行為，我必須調整我的y的定義  
因此我把每個row的y往上移一格。  
此作法即讓修改後的y1與y2，代表了該row(該消費者當月)有沒有在"下一個月"購買y1或y2，一樣是0=false,1=true  

所以把之前preprocess跟feature_engineering跑完生成之merged(all features).csv檔案，拿去在重複process一次  
即執行Reprocess data這個資料夾之preprocess_y_last_month.ipynb  
之後生成y = last month(without redundant)這個檔案。


------------------------------------------------------------------------------------------------------------------------
(此步驟可跳過)
在把y = last month(without redundant)這個檔案拿去Modeling資料夾，執行Catboost_modeling.ipynb程式。
此程式主要用前四個月201807~201810的資料來訓練，用第五個月201811的資料來評估F1-score，發現其實跟之前算出來的沒差很多，y1都是0.15左右。

------------------------------------------------------------------------------------------------------------------------

把y = last month(without redundant)這個檔案拿去Modeling資料夾，執行Catboost_to_predict_201901.ipynb程式。
此程式以前五個月的資料來訓練，在把第六個月(201812)資料當作test來預測y值(即201901會不會購買)

生成兩個檔案submit_pred_proba_y1(threshold = 0.62).csv  和   submit_pred_proba_y2(threshold = 0.9).csv

最後在此資料夾有一個Combine for submission，主要就是把這兩個csv融合成比賽需要的submission格式。

大功告成。
