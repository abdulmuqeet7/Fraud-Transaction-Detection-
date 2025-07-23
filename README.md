# Fraud-Transaction-Detection
Helps in detecting fraud transactions made , by taking important features as input.

Try out here https://fraudtransactionabdulmuqeet.streamlit.app/

Link to the dataset used - https://www.kaggle.com/datasets/marusagar/bank-transaction-fraud-detection/code

### 📊 Column Descriptions for Fraud Detection Dataset

1. **Customer_Name**: The name of the consumer making the transaction.  
2. **Gender**: The gender of the consumer (e.g., Male, Female, Other).  
3. **Age**: The age of the consumer at the time of the transaction.  
4. **State**: The nation in which the patron resides.  
5. **City**: The metropolis wherein the client is living.  
6. **Bank_Branch**: The specific financial institution branch wherein the consumer holds their account.  
7. **Account_Type**: The kind of account held by the customer (e.g., Savings, Checking).  
8. **Transaction_ID**: A unique identifier for each transaction.  
9. **Transaction_Date**: The date on which the transaction occurred.  
10. **Transaction_Time**: The specific time the transaction was initiated.  
11. **Transaction_Amount**: The financial value of the transaction.  
12. **Merchant_ID**: A unique identifier for the merchant involved in the transaction.  
13. **Transaction_Type**: The nature of the transaction (e.g., Withdrawal, Deposit, Transfer).  
14. **Merchant_Category**: The category of the merchant (e.g., Retail, Online, Travel).  
15. **Account_Balance**: The balance of the customer's account after the transaction.  
16. **Transaction_Device**: The device used by the consumer to perform the transaction (e.g., Mobile, Desktop).  
17. **Transaction_Location**: The geographical location (e.g., latitude, longitude) of the transaction.  
18. **Device_Type**: The type of device used for the transaction (e.g., Smartphone, Laptop).  
19. **Is_Fraud**: A binary indicator (1 or 0) indicating whether the transaction is fraudulent.  
20. **Transaction_Currency**: The currency used for the transaction (e.g., USD, EUR).  
21. **Customer_Contact**: The contact number of the client.  
22. **Transaction_Description**: A brief description of the transaction (e.g., purchase, transfer).  
23. **Customer_Email**: The email address associated with the consumer's account.  

> These column descriptions provide a clear understanding of the data used for fraud detection analysis.

Some unnecessary columns have been dropped in the ipynb file.

### 🧠 Model Overview

This project leverages a machine learning model to detect fraudulent financial transactions based on various customer and transaction-level features.

#### 🔍 Objectives:
- Identify suspicious or fraudulent transactions in real time.
- Minimize false positives while ensuring high fraud detection accuracy.
- Utilize interpretable features for model explainability.

#### 🛠️ Model Pipeline:
1. **Data Preprocessing**:  
   - Handling missing values  
   - Encoding categorical variables (Label Encoding, One-Hot Encoding)  
   - Feature scaling (e.g., StandardScaler or MinMaxScaler)

2. **Feature Engineering**:  
   - Derived variables like `transaction_hour`, `transaction_day`, or device risk score  
   - Aggregated features like average transaction amount per customer  

3. **Model Training**:  
   - Algorithms used: `Random Forest`, `XGBoost`(based on best performance)  
   - Evaluation using metrics such as Accuracy, Precision, Recall, F1-Score, and AUC-ROC  
   - Threshold tuning for fraud probability classification

4. **Prediction Logic**:  
   - `predict_proba()` is used to compute the probability of fraud  
   - Custom threshold (e.g., 0.45) is applied to classify transactions as Fraud or Not Fraud  

5. **Deployment**:  
   - Deployed using **Streamlit** for an interactive fraud detection dashboard  
   - Users input transaction details and get instant fraud classification

#### ✅ Output:
- **Predicted Class**: `Fraud` or `Not Fraud`
- **Fraud Probability Score**: Probability value between 0 and 1
- **Confidence Threshold**: Tunable value (default = 0.45)

---

> The model is optimized for financial environments where timely and accurate fraud detection is crucial to preventing losses and ensuring customer trust.


##### 4. 🧠 Model Selection & Training
- Algorithms tested:
  - `Random Forest`
  - `XGBoost`

- **Best Performing Model**: XGBoost (based on AUC, Precision, and Recall)
- **Cross-Validation**: Stratified K-Fold (k=5) to ensure balanced fraud class across folds.

---

##### 5. ⚙️ Hyperparameter Tuning
- Used  **Random Search** to tune key parameters:
  - For XGBoost: `n_estimators`, `max_depth`, `learning_rate`, `subsample`
  - Scored by: **F1-Score** and **ROC-AUC**

---

##### 6. 📈 Evaluation Metrics
Evaluated using multiple metrics due to class imbalance:
- **Accuracy** – 0.20
- **Precision** – 0.95
- **Recall (Sensitivity)** – 0.84
- **F1-Score** – 0 - 0.28, 1 - 0.10
- **AUC-ROC** – Overall ranking performance for binary classification.

> Threshold tuning: Instead of using the default 0.5 threshold, we applied a custom threshold (e.g., 0.45) to improve fraud recall while controlling false positives.

---

##### 7. 🧪 Final Testing
- The final model was tested on the held-out test set to ensure no data leakage.
- Feature importance was reviewed to ensure interpretability and compliance.

---

