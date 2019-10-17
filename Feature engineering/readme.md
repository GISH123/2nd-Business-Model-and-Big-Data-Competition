# 做特徵
目前做了持有資產每個月與上個月的變化量(as_flows)

## 使用
先做於上一個Preprocessing資料夾生出來的merged.csv  
用merged.csv才能跑feature engineering  

# 可生成兩個檔，merged(all features).csv與merged(without redundant).csv
# 目前最新model使用為merged(without redundant).csv
without redundant刪掉一些我認為沒必要的資料，詳細怎麼做請看code裡面的註解
