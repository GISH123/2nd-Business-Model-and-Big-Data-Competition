# Using merge.csv from Preprocessing folder
# Fit a CatBoost model without any further feature engineering
tried hyperparameter tuning "manually"

# Train/Test split :
Using 5 months(201807 ~ 201811) to predict last month(201812)
so train set = 5 months, test set = 1 month

# Achieved F1Score around 0.1257(best atm)
此結果為跟最後一個月(201812)做對比,輸出檔案為這邊的csv檔 : pred_proba(f1Score = 0.1258)
