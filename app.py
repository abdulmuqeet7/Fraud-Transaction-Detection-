import datetime
import streamlit as st
import numpy as np
import joblib
import datetime
import pickle

model = joblib.load('model/model.pkl')
st.title("Fraud Transactions detection model")

#input features
Age = st.number_input("Age")
Gender = st.selectbox('Select your gender',options = ['Male','Female'])
account_type = st.selectbox('Select Account Type : ',options = ['Savings','Business','Checking'],index=1)
# Manual encoding
if account_type == 'Savings':
    account_type = 2
elif account_type == 'Business':
    account_type = 0
else:  # Checking
    account_type = 1

transaction_type = st.selectbox('Select Transaction Type : ',options = ['Transfer', 'Bill Payment', 'Debit', 'Withdrawal', 'Credit'],index=1)

# Manual encoding using if-elif
if transaction_type == 'Bill Payment':
    transaction_type = 0
elif transaction_type == 'Credit':
    transaction_type = 1
elif transaction_type == 'Debit':
    transaction_type = 2
elif transaction_type == 'Transfer':
    transaction_type = 3
else:  # Withdrawal
    transaction_type = 4

merchant_category = st.selectbox('Select Merchant Type : ',options = ['Restaurant', 'Groceries', 'Entertainment', 'Health', 'Clothing','Electronics'],index=1)
if merchant_category == 'Clothing':
    merchant_category = 0
elif merchant_category == 'Electronics':
    merchant_category = 1
elif merchant_category == 'Entertainment':
    merchant_category = 2
elif merchant_category == 'Groceries':
    merchant_category = 3
elif merchant_category == 'Health':
    merchant_category = 4
else:  # Restaurant
    merchant_category = 5
device = st.selectbox('Select Device Type : ',options = ['POS', 'Desktop', 'Mobile', 'ATM'],index=1)
if device == 'ATM':
    device = 0
elif device == 'Desktop':
    device = 1
elif device == 'Mobile':
    device = 2
else:  # POS
    device = 3

state = st.selectbox('Select State : ',options = ['Kerala', 'Maharashtra', 'Bihar', 'Tamil Nadu', 'Punjab',
       'Gujarat', 'Delhi', 'Andaman and Nicobar Islands',
       'Madhya Pradesh', 'Chhattisgarh', 'Mizoram', 'West Bengal',
       'Sikkim', 'Dadra and Nagar Haveli and Daman and Diu',
       'Uttar Pradesh', 'Odisha', 'Tripura', 'Assam', 'Manipur',
       'Karnataka', 'Andhra Pradesh', 'Goa', 'Haryana', 'Lakshadweep',
       'Jharkhand', 'Meghalaya', 'Arunachal Pradesh',
       'Nagaland', 'Telangana', 'Rajasthan', 'Himachal Pradesh',
        'Uttarakhand'],index=1)

#Manually one hot encoding state
# Initialize all state one-hot encoded variables to 0
Kerala = 0
Maharashtra = 0
Bihar = 0
Tamil_Nadu = 0
Punjab = 0
Gujarat = 0
Delhi = 0
Andaman_and_Nicobar_Islands = 0
Madhya_Pradesh = 0
Chhattisgarh = 0
Mizoram = 0
West_Bengal = 0
Sikkim = 0
Dadra_and_Nagar_Haveli_and_Daman_and_Diu = 0
Uttar_Pradesh = 0
Odisha = 0
Tripura = 0
Assam = 0
Manipur = 0
Karnataka = 0
Andhra_Pradesh = 0
Goa = 0
Haryana = 0
Lakshadweep = 0
Jharkhand = 0
Meghalaya = 0
Arunachal_Pradesh = 0
Nagaland = 0
Telangana = 0
Rajasthan = 0
Himachal_Pradesh = 0
Uttarakhand = 0
# Manual one-hot encoding
if state == 'Kerala':
    Kerala = 1
elif state == 'Maharashtra':
    Maharashtra = 1
elif state == 'Bihar':
    Bihar = 1
elif state == 'Tamil Nadu':
    Tamil_Nadu = 1
elif state == 'Punjab':
    Punjab = 1
elif state == 'Gujarat':
    Gujarat = 1
elif state == 'Delhi':
    Delhi = 1
elif state == 'Andaman and Nicobar Islands':
    Andaman_and_Nicobar_Islands = 1
elif state == 'Madhya Pradesh':
    Madhya_Pradesh = 1
elif state == 'Chhattisgarh':
    Chhattisgarh = 1
elif state == 'Mizoram':
    Mizoram = 1
elif state == 'West Bengal':
    West_Bengal = 1
elif state == 'Sikkim':
    Sikkim = 1
elif state == 'Dadra and Nagar Haveli and Daman and Diu':
    Dadra_and_Nagar_Haveli_and_Daman_and_Diu = 1
elif state == 'Uttar Pradesh':
    Uttar_Pradesh = 1
elif state == 'Odisha':
    Odisha = 1
elif state == 'Tripura':
    Tripura = 1
elif state == 'Assam':
    Assam = 1
elif state == 'Manipur':
    Manipur = 1
elif state == 'Karnataka':
    Karnataka = 1
elif state == 'Andhra Pradesh':
    Andhra_Pradesh = 1
elif state == 'Goa':
    Goa = 1
elif state == 'Haryana':
    Haryana = 1
elif state == 'Lakshadweep':
    Lakshadweep = 1
elif state == 'Jharkhand':
    Jharkhand = 1
elif state == 'Meghalaya':
    Meghalaya = 1
elif state == 'Arunachal Pradesh':
    Arunachal_Pradesh = 1
elif state == 'Nagaland':
    Nagaland = 1
elif state == 'Telangana':
    Telangana = 1
elif state == 'Rajasthan':
    Rajasthan = 1
elif state == 'Himachal Pradesh':
    Himachal_Pradesh = 1
elif state == 'Uttarakhand':
    Uttarakhand = 1
city = st.selectbox('Select Nearest City : ',options = ['Thiruvananthapuram', 'Nashik', 'Bhagalpur', 'Chennai', 'Amritsar',
       'Ahmedabad', 'New Delhi', 'Port Blair', 'Bhopal', 'Jagdalpur',
       'Vadodara', 'Chandigarh', 'Champhai', 'Korba', 'Kolkata', 'Gaya',
       'Jorethang', 'Silvassa', 'Kanpur', 'Nagpur', 'Bhubaneswar',
       'Ambassa', 'Jorhat', 'Diglipur', 'Salem', 'Durg', 'Churachandpur',
       'Kottayam', 'Varanasi', 'Imphal', 'Belgaum', 'Agra', 'Durgapur',
       'Daman', 'Bilaspur', 'Nellore', 'Patiala', 'Jabalpur', 'Mapusa',
       'Agartala', 'Aurangabad', 'Gurugram', 'Vijayawada', 'Kavaratti',
       'Bokaro', 'Siliguri', 'Udaipur', 'Nongstoin', 'Tirupati',
       'Jamshedpur', 'Ludhiana', 'Aizawl', 'Raipur', 'Naharlagun',
       'Trichur', 'Kohima', 'Ambala', 'Hisar', 'Nizamabad', 'Dibrugarh',
       'Karimnagar', 'Jodhpur', 'Khammam', 'Jaipur', 'Wokha', 'Mysore',
       'Hyderabad', 'Kota', 'Tawang', 'Ziro', 'Shimla', 'Kolasib',
       'West Delhi', 'Vasco da Gama', 'Namchi', 'Thoubal', 'Tura', 'Pune',
       'Diu', 'Hubli', 'Ranchi', 'Yanam', 'South Delhi', 'Mokokchung',
       'North Delhi', 'Surat', 'Dehradun', 'Hazaribagh', 'Mumbai',
       'Visakhapatnam', 'Manali', 'Rourkela', 'Car Nicobar', 'Berhampur',
       'Sambalpur', 'Ujjain', 'Meerut', 'Trichy', 'Gangtok', 'Munger',
       'Kangra', 'Patna', 'Margao', 'Muzaffarpur', 'Karaikal',
       'East Delhi', 'Guntur', 'Guwahati', 'Lunglei', 'Lucknow',
       'Shillong', 'Indore', 'Panaji', 'Cuttack', 'Faridabad', 'Haldwani',
       'Madurai', 'Jalandhar', 'Bhavnagar', 'Kozhikode', 'Rishikesh',
       'Gwalior', 'Nainital', 'Asansol', 'Mangan', 'Kochi', 'Silchar',
       'Itanagar', 'Warangal', 'Kullu', 'Bangalore', 'Haridwar', 'Rajkot',
       'Mangalore', 'Mahe', 'Kangpokpi', 'Dimapur', 'Coimbatore',
       'Howrah', 'Nagaon', 'Puducherry', 'Dharmanagar', 'Dhanbad',
       'Ajmer', 'Jowai'],index=1)
# Initialize variables
Thiruvananthapuram = 0
Nashik = 0
Bhagalpur = 0
Chennai = 0
Amritsar = 0
Ahmedabad = 0
New_Delhi = 0
Port_Blair = 0
Bhopal = 0
Jagdalpur = 0
Vadodara = 0
Chandigarh = 0
Champhai = 0
Korba = 0
Kolkata = 0
Gaya = 0
Jorethang = 0
Silvassa = 0
Kanpur = 0
Nagpur = 0
Bhubaneswar = 0
Ambassa = 0
Jorhat = 0
Diglipur = 0
Salem = 0
Durg = 0
Churachandpur = 0
Kottayam = 0
Varanasi = 0
Imphal = 0
Belgaum = 0
Agra = 0
Durgapur = 0
Daman = 0
Bilaspur = 0
Nellore = 0
Patiala = 0
Jabalpur = 0
Mapusa = 0
Agartala = 0
Aurangabad = 0
Gurugram = 0
Vijayawada = 0
Kavaratti = 0
Bokaro = 0
Siliguri = 0
Udaipur = 0
Nongstoin = 0
Tirupati = 0
Jamshedpur = 0
Ludhiana = 0
Aizawl = 0
Raipur = 0
Naharlagun = 0
Trichur = 0
Kohima = 0
Ambala = 0
Hisar = 0
Nizamabad = 0
Dibrugarh = 0
Karimnagar = 0
Jodhpur = 0
Khammam = 0
Jaipur = 0
Wokha = 0
Mysore = 0
Hyderabad = 0
Kota = 0
Tawang = 0
Ziro = 0
Shimla = 0
Kolasib = 0
West_Delhi = 0
Vasco_da_Gama = 0
Namchi = 0
Thoubal = 0
Tura = 0
Pune = 0
Diu = 0
Hubli = 0
Ranchi = 0
Yanam = 0
South_Delhi = 0
Mokokchung = 0
North_Delhi = 0
Surat = 0
Dehradun = 0
Hazaribagh = 0
Mumbai = 0
Visakhapatnam = 0
Manali = 0
Rourkela = 0
Car_Nicobar = 0
Berhampur = 0
Sambalpur = 0
Ujjain = 0
Meerut = 0
Trichy = 0
Gangtok = 0
Munger = 0
Kangra = 0
Patna = 0
Margao = 0
Muzaffarpur = 0
Karaikal = 0
East_Delhi = 0
Guntur = 0
Guwahati = 0
Lunglei = 0
Lucknow = 0
Shillong = 0
Indore = 0
Panaji = 0
Cuttack = 0
Faridabad = 0
Haldwani = 0
Madurai = 0
Jalandhar = 0
Bhavnagar = 0
Kozhikode = 0
Rishikesh = 0
Gwalior = 0
Nainital = 0
Asansol = 0
Mangan = 0
Kochi = 0
Silchar = 0
Itanagar = 0
Warangal = 0
Kullu = 0
Bangalore = 0
Haridwar = 0
Rajkot = 0
Mangalore = 0
Mahe = 0
Kangpokpi = 0
Dimapur = 0
Coimbatore = 0
Howrah = 0
Nagaon = 0
Puducherry = 0
Dharmanagar = 0
Dhanbad = 0
Ajmer = 0
Jowai = 0

# One-hot encoding
if city == 'Thiruvananthapuram':
    Thiruvananthapuram = 1
elif city == 'Nashik':
    Nashik = 1
elif city == 'Bhagalpur':
    Bhagalpur = 1
elif city == 'Chennai':
    Chennai = 1
elif city == 'Amritsar':
    Amritsar = 1
elif city == 'Ahmedabad':
    Ahmedabad = 1
elif city == 'New Delhi':
    New_Delhi = 1
elif city == 'Port Blair':
    Port_Blair = 1
elif city == 'Bhopal':
    Bhopal = 1
elif city == 'Jagdalpur':
    Jagdalpur = 1
elif city == 'Vadodara':
    Vadodara = 1
elif city == 'Chandigarh':
    Chandigarh = 1
elif city == 'Champhai':
    Champhai = 1
elif city == 'Korba':
    Korba = 1
elif city == 'Kolkata':
    Kolkata = 1
elif city == 'Gaya':
    Gaya = 1
elif city == 'Jorethang':
    Jorethang = 1
elif city == 'Silvassa':
    Silvassa = 1
elif city == 'Kanpur':
    Kanpur = 1
elif city == 'Nagpur':
    Nagpur = 1
elif city == 'Bhubaneswar':
    Bhubaneswar = 1
elif city == 'Ambassa':
    Ambassa = 1
elif city == 'Jorhat':
    Jorhat = 1
elif city == 'Diglipur':
    Diglipur = 1
elif city == 'Salem':
    Salem = 1
elif city == 'Durg':
    Durg = 1
elif city == 'Churachandpur':
    Churachandpur = 1
elif city == 'Kottayam':
    Kottayam = 1
elif city == 'Varanasi':
    Varanasi = 1
elif city == 'Imphal':
    Imphal = 1
elif city == 'Belgaum':
    Belgaum = 1
elif city == 'Agra':
    Agra = 1
elif city == 'Durgapur':
    Durgapur = 1
elif city == 'Daman':
    Daman = 1
elif city == 'Bilaspur':
    Bilaspur = 1
elif city == 'Nellore':
    Nellore = 1
elif city == 'Patiala':
    Patiala = 1
elif city == 'Jabalpur':
    Jabalpur = 1
elif city == 'Mapusa':
    Mapusa = 1
elif city == 'Agartala':
    Agartala = 1
elif city == 'Aurangabad':
    Aurangabad = 1
elif city == 'Gurugram':
    Gurugram = 1
elif city == 'Vijayawada':
    Vijayawada = 1
elif city == 'Kavaratti':
    Kavaratti = 1
elif city == 'Bokaro':
    Bokaro = 1
elif city == 'Siliguri':
    Siliguri = 1
elif city == 'Udaipur':
    Udaipur = 1
elif city == 'Nongstoin':
    Nongstoin = 1
elif city == 'Tirupati':
    Tirupati = 1
elif city == 'Jamshedpur':
    Jamshedpur = 1
elif city == 'Ludhiana':
    Ludhiana = 1
elif city == 'Aizawl':
    Aizawl = 1
elif city == 'Raipur':
    Raipur = 1
elif city == 'Naharlagun':
    Naharlagun = 1
elif city == 'Trichur':
    Trichur = 1
elif city == 'Kohima':
    Kohima = 1
elif city == 'Ambala':
    Ambala = 1
elif city == 'Hisar':
    Hisar = 1
elif city == 'Nizamabad':
    Nizamabad = 1
elif city == 'Dibrugarh':
    Dibrugarh = 1
elif city == 'Karimnagar':
    Karimnagar = 1
elif city == 'Jodhpur':
    Jodhpur = 1
elif city == 'Khammam':
    Khammam = 1
elif city == 'Jaipur':
    Jaipur = 1
elif city == 'Wokha':
    Wokha = 1
elif city == 'Mysore':
    Mysore = 1
elif city == 'Hyderabad':
    Hyderabad = 1
elif city == 'Kota':
    Kota = 1
elif city == 'Tawang':
    Tawang = 1
elif city == 'Ziro':
    Ziro = 1
elif city == 'Shimla':
    Shimla = 1
elif city == 'Kolasib':
    Kolasib = 1
elif city == 'West Delhi':
    West_Delhi = 1
elif city == 'Vasco da Gama':
    Vasco_da_Gama = 1
elif city == 'Namchi':
    Namchi = 1
elif city == 'Thoubal':
    Thoubal = 1
elif city == 'Tura':
    Tura = 1
elif city == 'Pune':
    Pune = 1
elif city == 'Diu':
    Diu = 1
elif city == 'Hubli':
    Hubli = 1
elif city == 'Ranchi':
    Ranchi = 1
elif city == 'Yanam':
    Yanam = 1
elif city == 'South Delhi':
    South_Delhi = 1
elif city == 'Mokokchung':
    Mokokchung = 1
elif city == 'North Delhi':
    North_Delhi = 1
elif city == 'Surat':
    Surat = 1
elif city == 'Dehradun':
    Dehradun = 1
elif city == 'Hazaribagh':
    Hazaribagh = 1
elif city == 'Mumbai':
    Mumbai = 1
elif city == 'Visakhapatnam':
    Visakhapatnam = 1
elif city == 'Manali':
    Manali = 1
elif city == 'Rourkela':
    Rourkela = 1
elif city == 'Car Nicobar':
    Car_Nicobar = 1
elif city == 'Berhampur':
    Berhampur = 1
elif city == 'Sambalpur':
    Sambalpur = 1
elif city == 'Ujjain':
    Ujjain = 1
elif city == 'Meerut':
    Meerut = 1
elif city == 'Trichy':
    Trichy = 1
elif city == 'Gangtok':
    Gangtok = 1
elif city == 'Munger':
    Munger = 1
elif city == 'Kangra':
    Kangra = 1
elif city == 'Patna':
    Patna = 1
elif city == 'Margao':
    Margao = 1
elif city == 'Muzaffarpur':
    Muzaffarpur = 1
elif city == 'Karaikal':
    Karaikal = 1
elif city == 'East Delhi':
    East_Delhi = 1
elif city == 'Guntur':
    Guntur = 1
elif city == 'Guwahati':
    Guwahati = 1
elif city == 'Lunglei':
    Lunglei = 1
elif city == 'Lucknow':
    Lucknow = 1
elif city == 'Shillong':
    Shillong = 1
elif city == 'Indore':
    Indore = 1
elif city == 'Panaji':
    Panaji = 1
elif city == 'Cuttack':
    Cuttack = 1
elif city == 'Faridabad':
    Faridabad = 1
elif city == 'Haldwani':
    Haldwani = 1
elif city == 'Madurai':
    Madurai = 1
elif city == 'Jalandhar':
    Jalandhar = 1
elif city == 'Bhavnagar':
    Bhavnagar = 1
elif city == 'Kozhikode':
    Kozhikode = 1
elif city == 'Rishikesh':
    Rishikesh = 1
elif city == 'Gwalior':
    Gwalior = 1
elif city == 'Nainital':
    Nainital = 1
elif city == 'Asansol':
    Asansol = 1
elif city == 'Mangan':
    Mangan = 1
elif city == 'Kochi':
    Kochi = 1
elif city == 'Silchar':
    Silchar = 1
elif city == 'Itanagar':
    Itanagar = 1
elif city == 'Warangal':
    Warangal = 1
elif city == 'Kullu':
    Kullu = 1
elif city == 'Bangalore':
    Bangalore = 1
elif city == 'Haridwar':
    Haridwar = 1
elif city == 'Rajkot':
    Rajkot = 1
elif city == 'Mangalore':
    Mangalore = 1
elif city == 'Mahe':
    Mahe = 1
elif city == 'Kangpokpi':
    Kangpokpi = 1
elif city == 'Dimapur':
    Dimapur = 1
elif city == 'Coimbatore':
    Coimbatore = 1
elif city == 'Howrah':
    Howrah = 1
elif city == 'Nagaon':
    Nagaon = 1
elif city == 'Puducherry':
    Puducherry = 1
elif city == 'Dharmanagar':
    Dharmanagar = 1
elif city == 'Dhanbad':
    Dhanbad = 1
elif city == 'Ajmer':
    Ajmer = 1
elif city == 'Jowai':
    Jowai = 1

Branch = st.selectbox('Select Nearest Branch : ',options = ['Thiruvananthapuram Branch', 'Nashik Branch', 'Bhagalpur Branch',
       'Chennai Branch', 'Amritsar Branch', 'Ahmedabad Branch',
       'New Delhi Branch', 'Port Blair Branch', 'Bhopal Branch',
       'Jagdalpur Branch', 'Vadodara Branch', 'Chandigarh Branch',
       'Champhai Branch', 'Korba Branch', 'Kolkata Branch', 'Gaya Branch',
       'Jorethang Branch', 'Silvassa Branch', 'Kanpur Branch',
       'Nagpur Branch', 'Bhubaneswar Branch', 'Ambassa Branch',
       'Jorhat Branch', 'Diglipur Branch', 'Salem Branch', 'Durg Branch',
       'Churachandpur Branch', 'Kottayam Branch', 'Varanasi Branch',
       'Imphal Branch', 'Belgaum Branch', 'Agra Branch',
       'Durgapur Branch', 'Daman Branch', 'Bilaspur Branch',
       'Nellore Branch', 'Patiala Branch', 'Jabalpur Branch',
       'Mapusa Branch', 'Agartala Branch', 'Aurangabad Branch',
       'Gurugram Branch', 'Vijayawada Branch', 'Kavaratti Branch',
       'Bokaro Branch', 'Siliguri Branch', 'Udaipur Branch',
       'Nongstoin Branch', 'Tirupati Branch', 'Jamshedpur Branch',
       'Ludhiana Branch', 'Aizawl Branch', 'Raipur Branch',
       'Naharlagun Branch', 'Trichur Branch', 'Kohima Branch',
       'Ambala Branch', 'Hisar Branch', 'Nizamabad Branch',
       'Dibrugarh Branch', 'Karimnagar Branch', 'Jodhpur Branch',
       'Khammam Branch', 'Jaipur Branch', 'Wokha Branch', 'Mysore Branch',
       'Hyderabad Branch', 'Kota Branch', 'Tawang Branch', 'Ziro Branch',
       'Shimla Branch', 'Kolasib Branch', 'West Delhi Branch',
       'Vasco da Gama Branch', 'Namchi Branch', 'Thoubal Branch',
       'Tura Branch', 'Pune Branch', 'Diu Branch', 'Hubli Branch',
       'Ranchi Branch', 'Yanam Branch', 'South Delhi Branch',
       'Mokokchung Branch', 'North Delhi Branch', 'Surat Branch',
       'Dehradun Branch', 'Hazaribagh Branch', 'Mumbai Branch',
       'Visakhapatnam Branch', 'Manali Branch', 'Rourkela Branch',
       'Car Nicobar Branch', 'Berhampur Branch', 'Sambalpur Branch',
       'Ujjain Branch', 'Meerut Branch', 'Trichy Branch',
       'Gangtok Branch', 'Munger Branch', 'Kangra Branch', 'Patna Branch',
       'Margao Branch', 'Muzaffarpur Branch', 'Karaikal Branch',
       'East Delhi Branch', 'Guntur Branch', 'Guwahati Branch',
       'Lunglei Branch', 'Lucknow Branch', 'Shillong Branch',
       'Indore Branch', 'Panaji Branch', 'Cuttack Branch',
       'Faridabad Branch', 'Haldwani Branch', 'Madurai Branch',
       'Jalandhar Branch', 'Bhavnagar Branch', 'Kozhikode Branch',
       'Rishikesh Branch', 'Gwalior Branch', 'Nainital Branch',
       'Asansol Branch', 'Mangan Branch', 'Kochi Branch',
       'Silchar Branch', 'Itanagar Branch', 'Warangal Branch',
       'Kullu Branch', 'Bangalore Branch', 'Haridwar Branch',
       'Rajkot Branch', 'Mangalore Branch', 'Mahe Branch',
       'Kangpokpi Branch', 'Dimapur Branch', 'Coimbatore Branch',
       'Howrah Branch', 'Nagaon Branch', 'Puducherry Branch',
       'Dharmanagar Branch', 'Dhanbad Branch', 'Ajmer Branch',
       'Jowai Branch'],index=1)
# Initialize all branches to 0
Thiruvananthapuram_Branch = 0
Nashik_Branch = 0
Bhagalpur_Branch = 0
Chennai_Branch = 0
Amritsar_Branch = 0
Ahmedabad_Branch = 0
New_Delhi_Branch = 0
Port_Blair_Branch = 0
Bhopal_Branch = 0
Jagdalpur_Branch = 0
Vadodara_Branch = 0
Chandigarh_Branch = 0
Champhai_Branch = 0
Korba_Branch = 0
Kolkata_Branch = 0
Gaya_Branch = 0
Jorethang_Branch = 0
Silvassa_Branch = 0
Kanpur_Branch = 0
Nagpur_Branch = 0
Bhubaneswar_Branch = 0
Ambassa_Branch = 0
Jorhat_Branch = 0
Diglipur_Branch = 0
Salem_Branch = 0
Durg_Branch = 0
Churachandpur_Branch = 0
Kottayam_Branch = 0
Varanasi_Branch = 0
Imphal_Branch = 0
Belgaum_Branch = 0
Agra_Branch = 0
Durgapur_Branch = 0
Daman_Branch = 0
Bilaspur_Branch = 0
Nellore_Branch = 0
Patiala_Branch = 0
Jabalpur_Branch = 0
Mapusa_Branch = 0
Agartala_Branch = 0
Aurangabad_Branch = 0
Gurugram_Branch = 0
Vijayawada_Branch = 0
Kavaratti_Branch = 0
Bokaro_Branch = 0
Siliguri_Branch = 0
Udaipur_Branch = 0
Nongstoin_Branch = 0
Tirupati_Branch = 0
Jamshedpur_Branch = 0
Ludhiana_Branch = 0
Aizawl_Branch = 0
Raipur_Branch = 0
Naharlagun_Branch = 0
Trichur_Branch = 0
Kohima_Branch = 0
Ambala_Branch = 0
Hisar_Branch = 0
Nizamabad_Branch = 0
Dibrugarh_Branch = 0
Karimnagar_Branch = 0
Jodhpur_Branch = 0
Khammam_Branch = 0
Jaipur_Branch = 0
Wokha_Branch = 0
Mysore_Branch = 0
Hyderabad_Branch = 0
Kota_Branch = 0
Tawang_Branch = 0
Ziro_Branch = 0
Shimla_Branch = 0
Kolasib_Branch = 0
West_Delhi_Branch = 0
Vasco_da_Gama_Branch = 0
Namchi_Branch = 0
Thoubal_Branch = 0
Tura_Branch = 0
Pune_Branch = 0
Diu_Branch = 0
Hubli_Branch = 0
Ranchi_Branch = 0
Yanam_Branch = 0
South_Delhi_Branch = 0
Mokokchung_Branch = 0
North_Delhi_Branch = 0
Surat_Branch = 0
Dehradun_Branch = 0
Hazaribagh_Branch = 0
Mumbai_Branch = 0
Visakhapatnam_Branch = 0
Manali_Branch = 0
Rourkela_Branch = 0
Car_Nicobar_Branch = 0
Berhampur_Branch = 0
Sambalpur_Branch = 0
Ujjain_Branch = 0
Meerut_Branch = 0
Trichy_Branch = 0
Gangtok_Branch = 0
Munger_Branch = 0
Kangra_Branch = 0
Patna_Branch = 0
Margao_Branch = 0
Muzaffarpur_Branch = 0
Karaikal_Branch = 0
East_Delhi_Branch = 0
Guntur_Branch = 0
Guwahati_Branch = 0
Lunglei_Branch = 0
Lucknow_Branch = 0
Shillong_Branch = 0
Indore_Branch = 0
Panaji_Branch = 0
Cuttack_Branch = 0
Faridabad_Branch = 0
Haldwani_Branch = 0
Madurai_Branch = 0
Jalandhar_Branch = 0
Bhavnagar_Branch = 0
Kozhikode_Branch = 0
Rishikesh_Branch = 0
Gwalior_Branch = 0
Nainital_Branch = 0
Asansol_Branch = 0
Mangan_Branch = 0
Kochi_Branch = 0
Silchar_Branch = 0
Itanagar_Branch = 0
Warangal_Branch = 0
Kullu_Branch = 0
Bangalore_Branch = 0
Haridwar_Branch = 0
Rajkot_Branch = 0
Mangalore_Branch = 0
Mahe_Branch = 0
Kangpokpi_Branch = 0
Dimapur_Branch = 0
Coimbatore_Branch = 0
Howrah_Branch = 0
Nagaon_Branch = 0
Puducherry_Branch = 0
Dharmanagar_Branch = 0
Dhanbad_Branch = 0
Ajmer_Branch = 0
Jowai_Branch = 0

# Manual one-hot encoding
if Branch == 'Thiruvananthapuram Branch':
    Thiruvananthapuram_Branch = 1
elif Branch == 'Nashik Branch':
    Nashik_Branch = 1
elif Branch == 'Bhagalpur Branch':
    Bhagalpur_Branch = 1
elif Branch == 'Chennai Branch':
    Chennai_Branch = 1
elif Branch == 'Amritsar Branch':
    Amritsar_Branch = 1
elif Branch == 'Ahmedabad Branch':
    Ahmedabad_Branch = 1
elif Branch == 'New Delhi Branch':
    New_Delhi_Branch = 1
elif Branch == 'Port Blair Branch':
    Port_Blair_Branch = 1
elif Branch == 'Bhopal Branch':
    Bhopal_Branch = 1
elif Branch == 'Jagdalpur Branch':
    Jagdalpur_Branch = 1
elif Branch == 'Vadodara Branch':
    Vadodara_Branch = 1
elif Branch == 'Chandigarh Branch':
    Chandigarh_Branch = 1
elif Branch == 'Champhai Branch':
    Champhai_Branch = 1
elif Branch == 'Korba Branch':
    Korba_Branch = 1
elif Branch == 'Kolkata Branch':
    Kolkata_Branch = 1
elif Branch == 'Gaya Branch':
    Gaya_Branch = 1
elif Branch == 'Jorethang Branch':
    Jorethang_Branch = 1
elif Branch == 'Silvassa Branch':
    Silvassa_Branch = 1
elif Branch == 'Kanpur Branch':
    Kanpur_Branch = 1
elif Branch == 'Nagpur Branch':
    Nagpur_Branch = 1
elif Branch == 'Bhubaneswar Branch':
    Bhubaneswar_Branch = 1
elif Branch == 'Ambassa Branch':
    Ambassa_Branch = 1
elif Branch == 'Jorhat Branch':
    Jorhat_Branch = 1
elif Branch == 'Diglipur Branch':
    Diglipur_Branch = 1
elif Branch == 'Salem Branch':
    Salem_Branch = 1
elif Branch == 'Durg Branch':
    Durg_Branch = 1
elif Branch == 'Churachandpur Branch':
    Churachandpur_Branch = 1
elif Branch == 'Kottayam Branch':
    Kottayam_Branch = 1
elif Branch == 'Varanasi Branch':
    Varanasi_Branch = 1
elif Branch == 'Imphal Branch':
    Imphal_Branch = 1
elif Branch == 'Belgaum Branch':
    Belgaum_Branch = 1
elif Branch == 'Agra Branch':
    Agra_Branch = 1
elif Branch == 'Durgapur Branch':
    Durgapur_Branch = 1
elif Branch == 'Daman Branch':
    Daman_Branch = 1
elif Branch == 'Bilaspur Branch':
    Bilaspur_Branch = 1
elif Branch == 'Nellore Branch':
    Nellore_Branch = 1
elif Branch == 'Patiala Branch':
    Patiala_Branch = 1
elif Branch == 'Jabalpur Branch':
    Jabalpur_Branch = 1
elif Branch == 'Mapusa Branch':
    Mapusa_Branch = 1
elif Branch == 'Agartala Branch':
    Agartala_Branch = 1
elif Branch == 'Aurangabad Branch':
    Aurangabad_Branch = 1
elif Branch == 'Gurugram Branch':
    Gurugram_Branch = 1
elif Branch == 'Vijayawada Branch':
    Vijayawada_Branch = 1
elif Branch == 'Kavaratti Branch':
    Kavaratti_Branch = 1
elif Branch == 'Bokaro Branch':
    Bokaro_Branch = 1
elif Branch == 'Siliguri Branch':
    Siliguri_Branch = 1
elif Branch == 'Udaipur Branch':
    Udaipur_Branch = 1
elif Branch == 'Nongstoin Branch':
    Nongstoin_Branch = 1
elif Branch == 'Tirupati Branch':
    Tirupati_Branch = 1
elif Branch == 'Jamshedpur Branch':
    Jamshedpur_Branch = 1
elif Branch == 'Ludhiana Branch':
    Ludhiana_Branch = 1
elif Branch == 'Aizawl Branch':
    Aizawl_Branch = 1
elif Branch == 'Raipur Branch':
    Raipur_Branch = 1
elif Branch == 'Naharlagun Branch':
    Naharlagun_Branch = 1
elif Branch == 'Trichur Branch':
    Trichur_Branch = 1
elif Branch == 'Kohima Branch':
    Kohima_Branch = 1
elif Branch == 'Ambala Branch':
    Ambala_Branch = 1
elif Branch == 'Hisar Branch':
    Hisar_Branch = 1
elif Branch == 'Nizamabad Branch':
    Nizamabad_Branch = 1
elif Branch == 'Dibrugarh Branch':
    Dibrugarh_Branch = 1
elif Branch == 'Karimnagar Branch':
    Karimnagar_Branch = 1
elif Branch == 'Jodhpur Branch':
    Jodhpur_Branch = 1
elif Branch == 'Khammam Branch':
    Khammam_Branch = 1
elif Branch == 'Jaipur Branch':
    Jaipur_Branch = 1
elif Branch == 'Wokha Branch':
    Wokha_Branch = 1
elif Branch == 'Mysore Branch':
    Mysore_Branch = 1
elif Branch == 'Hyderabad Branch':
    Hyderabad_Branch = 1
elif Branch == 'Kota Branch':
    Kota_Branch = 1
elif Branch == 'Tawang Branch':
    Tawang_Branch = 1
elif Branch == 'Ziro Branch':
    Ziro_Branch = 1
elif Branch == 'Shimla Branch':
    Shimla_Branch = 1
elif Branch == 'Kolasib Branch':
    Kolasib_Branch = 1
elif Branch == 'West Delhi Branch':
    West_Delhi_Branch = 1
elif Branch == 'Vasco da Gama Branch':
    Vasco_da_Gama_Branch = 1
elif Branch == 'Namchi Branch':
    Namchi_Branch = 1
elif Branch == 'Thoubal Branch':
    Thoubal_Branch = 1
elif Branch == 'Tura Branch':
    Tura_Branch = 1
elif Branch == 'Pune Branch':
    Pune_Branch = 1
elif Branch == 'Diu Branch':
    Diu_Branch = 1
elif Branch == 'Hubli Branch':
    Hubli_Branch = 1
elif Branch == 'Ranchi Branch':
    Ranchi_Branch = 1
elif Branch == 'Yanam Branch':
    Yanam_Branch = 1
elif Branch == 'South Delhi Branch':
    South_Delhi_Branch = 1
elif Branch == 'Mokokchung Branch':
    Mokokchung_Branch = 1
elif Branch == 'North Delhi Branch':
    North_Delhi_Branch = 1
elif Branch == 'Surat Branch':
    Surat_Branch = 1
elif Branch == 'Dehradun Branch':
    Dehradun_Branch = 1
elif Branch == 'Hazaribagh Branch':
    Hazaribagh_Branch = 1
elif Branch == 'Mumbai Branch':
    Mumbai_Branch = 1
elif Branch == 'Visakhapatnam Branch':
    Visakhapatnam_Branch = 1
elif Branch == 'Manali Branch':
    Manali_Branch = 1
elif Branch == 'Rourkela Branch':
    Rourkela_Branch = 1
elif Branch == 'Car Nicobar Branch':
    Car_Nicobar_Branch = 1
elif Branch == 'Berhampur Branch':
    Berhampur_Branch = 1
elif Branch == 'Sambalpur Branch':
    Sambalpur_Branch = 1
elif Branch == 'Ujjain Branch':
    Ujjain_Branch = 1
elif Branch == 'Meerut Branch':
    Meerut_Branch = 1
elif Branch == 'Trichy Branch':
    Trichy_Branch = 1
elif Branch == 'Gangtok Branch':
    Gangtok_Branch = 1
elif Branch == 'Munger Branch':
    Munger_Branch = 1
elif Branch == 'Kangra Branch':
    Kangra_Branch = 1
elif Branch == 'Patna Branch':
    Patna_Branch = 1
elif Branch == 'Margao Branch':
    Margao_Branch = 1
elif Branch == 'Muzaffarpur Branch':
    Muzaffarpur_Branch = 1
elif Branch == 'Karaikal Branch':
    Karaikal_Branch = 1
elif Branch == 'East Delhi Branch':
    East_Delhi_Branch = 1
elif Branch == 'Guntur Branch':
    Guntur_Branch = 1
elif Branch == 'Guwahati Branch':
    Guwahati_Branch = 1
elif Branch == 'Lunglei Branch':
    Lunglei_Branch = 1
elif Branch == 'Lucknow Branch':
    Lucknow_Branch = 1
elif Branch == 'Shillong Branch':
    Shillong_Branch = 1
elif Branch == 'Indore Branch':
    Indore_Branch = 1
elif Branch == 'Panaji Branch':
    Panaji_Branch = 1
elif Branch == 'Cuttack Branch':
    Cuttack_Branch = 1
elif Branch == 'Faridabad Branch':
    Faridabad_Branch = 1
elif Branch == 'Haldwani Branch':
    Haldwani_Branch = 1
elif Branch == 'Madurai Branch':
    Madurai_Branch = 1
elif Branch == 'Jalandhar Branch':
    Jalandhar_Branch = 1
elif Branch == 'Bhavnagar Branch':
    Bhavnagar_Branch = 1
elif Branch == 'Kozhikode Branch':
    Kozhikode_Branch = 1
elif Branch == 'Rishikesh Branch':
    Rishikesh_Branch = 1
elif Branch == 'Gwalior Branch':
    Gwalior_Branch = 1
elif Branch == 'Nainital Branch':
    Nainital_Branch = 1
elif Branch == 'Asansol Branch':
    Asansol_Branch = 1
elif Branch == 'Mangan Branch':
    Mangan_Branch = 1
elif Branch == 'Kochi Branch':
    Kochi_Branch = 1
elif Branch == 'Silchar Branch':
    Silchar_Branch = 1
elif Branch == 'Itanagar Branch':
    Itanagar_Branch = 1
elif Branch == 'Warangal Branch':
    Warangal_Branch = 1
elif Branch == 'Kullu Branch':
    Kullu_Branch = 1
elif Branch == 'Bangalore Branch':
    Bangalore_Branch = 1
elif Branch == 'Haridwar Branch':
    Haridwar_Branch = 1
elif Branch == 'Rajkot Branch':
    Rajkot_Branch = 1
elif Branch == 'Mangalore Branch':
    Mangalore_Branch = 1
elif Branch == 'Mahe Branch':
    Mahe_Branch = 1
elif Branch == 'Kangpokpi Branch':
    Kangpokpi_Branch = 1
elif Branch == 'Dimapur Branch':
    Dimapur_Branch = 1
elif Branch == 'Coimbatore Branch':
    Coimbatore_Branch = 1
elif Branch == 'Howrah Branch':
    Howrah_Branch = 1
elif Branch == 'Nagaon Branch':
    Nagaon_Branch = 1
elif Branch == 'Puducherry Branch':
    Puducherry_Branch = 1
elif Branch == 'Dharmanagar Branch':
    Dharmanagar_Branch = 1
elif Branch == 'Dhanbad Branch':
    Dhanbad_Branch = 1
elif Branch == 'Ajmer Branch':
    Ajmer_Branch = 1
elif Branch == 'Jowai Branch':
    Jowai_Branch = 1


Transaction_device = st.selectbox('Select the Transaction Device Type : ',options = ['Voice Assistant', 'POS Mobile Device', 'ATM', 'POS Mobile App',
       'Virtual Card', 'Mobile Device', 'Payment Gateway Device',
       'Debit/Credit Card', 'Bank Branch', 'Desktop/Laptop',
       'Self-service Banking Machine', 'ATM Booth Kiosk',
       'Biometric Scanner', 'Web Browser', 'Tablet', 'Wearable Device',
       'QR Code Scanner', 'Smart Card', 'POS Terminal', 'Banking Chatbot'],index=1)
# Initialize all transaction devices to 0
Voice_Assistant = 0
POS_Mobile_Device = 0
ATM = 0
POS_Mobile_App = 0
Virtual_Card = 0
Mobile_Device = 0
Payment_Gateway_Device = 0
Debit_Credit_Card = 0
Bank_Branch = 0
Desktop_Laptop = 0
Self_service_Banking_Machine = 0
ATM_Booth_Kiosk = 0
Biometric_Scanner = 0
Web_Browser = 0
Tablet = 0
Wearable_Device = 0
QR_Code_Scanner = 0
Smart_Card = 0
POS_Terminal = 0
Banking_Chatbot = 0

# Manual one-hot encoding
if Transaction_device == 'Voice Assistant':
    Voice_Assistant = 1
elif Transaction_device == 'POS Mobile Device':
    POS_Mobile_Device = 1
elif Transaction_device == 'ATM':
    ATM = 1
elif Transaction_device == 'POS Mobile App':
    POS_Mobile_App = 1
elif Transaction_device == 'Virtual Card':
    Virtual_Card = 1
elif Transaction_device == 'Mobile Device':
    Mobile_Device = 1
elif Transaction_device == 'Payment Gateway Device':
    Payment_Gateway_Device = 1
elif Transaction_device == 'Debit/Credit Card':
    Debit_Credit_Card = 1
elif Transaction_device == 'Bank Branch':
    Bank_Branch = 1
elif Transaction_device == 'Desktop/Laptop':
    Desktop_Laptop = 1
elif Transaction_device == 'Self-service Banking Machine':
    Self_service_Banking_Machine = 1
elif Transaction_device == 'ATM Booth Kiosk':
    ATM_Booth_Kiosk = 1
elif Transaction_device == 'Biometric Scanner':
    Biometric_Scanner = 1
elif Transaction_device == 'Web Browser':
    Web_Browser = 1
elif Transaction_device == 'Tablet':
    Tablet = 1
elif Transaction_device == 'Wearable Device':
    Wearable_Device = 1
elif Transaction_device == 'QR Code Scanner':
    QR_Code_Scanner = 1
elif Transaction_device == 'Smart Card':
    Smart_Card = 1
elif Transaction_device == 'POS Terminal':
    POS_Terminal = 1
elif Transaction_device == 'Banking Chatbot':
    Banking_Chatbot = 1

transaction_amount = st.number_input('Enter the Transaction Amount')
account_balance = st.number_input('Enter the Account Balance')
Transaction_location = st.selectbox('Select Transaction Location: ',options = ['Thiruvananthapuram, Kerala', 'Nashik, Maharashtra',
       'Bhagalpur, Bihar', 'Chennai, Tamil Nadu', 'Amritsar, Punjab',
       'Ahmedabad, Gujarat', 'New Delhi, Delhi',
       'Port Blair, Andaman and Nicobar Islands',
       'Bhopal, Madhya Pradesh', 'Jagdalpur, Chhattisgarh',
       'Vadodara, Gujarat', 'Chandigarh, Punjab', 'Champhai, Mizoram',
       'Korba, Chhattisgarh', 'Kolkata, West Bengal', 'Gaya, Bihar',
       'Jorethang, Sikkim',
       'Silvassa, Dadra and Nagar Haveli and Daman and Diu',
       'Kanpur, Uttar Pradesh', 'Nagpur, Maharashtra',
       'Bhubaneswar, Odisha', 'Ambassa, Tripura', 'Jorhat, Assam',
       'Diglipur, Andaman and Nicobar Islands', 'Salem, Tamil Nadu',
       'Durg, Chhattisgarh', 'Churachandpur, Manipur', 'Kottayam, Kerala',
       'Varanasi, Uttar Pradesh', 'Imphal, Manipur', 'Belgaum, Karnataka',
       'Agra, Uttar Pradesh', 'Durgapur, West Bengal',
       'Daman, Dadra and Nagar Haveli and Daman and Diu',
       'Bilaspur, Chhattisgarh', 'Nellore, Andhra Pradesh',
       'Patiala, Punjab', 'Jabalpur, Madhya Pradesh', 'Mapusa, Goa',
       'Agartala, Tripura', 'Aurangabad, Maharashtra',
       'Gurugram, Haryana', 'Vijayawada, Andhra Pradesh',
       'Kavaratti, Lakshadweep', 'Bokaro, Jharkhand',
       'Siliguri, West Bengal', 'Udaipur, Tripura',
       'Nongstoin, Meghalaya', 'Tirupati, Andhra Pradesh',
       'Jamshedpur, Jharkhand', 'Chandigarh, Chandigarh',
       'Ludhiana, Punjab', 'Aizawl, Mizoram', 'Raipur, Chhattisgarh',
       'Naharlagun, Arunachal Pradesh', 'Trichur, Kerala',
       'Kohima, Nagaland', 'Ambala, Haryana', 'Hisar, Haryana',
       'Nizamabad, Telangana', 'Dibrugarh, Assam',
       'Karimnagar, Telangana', 'Jodhpur, Rajasthan',
       'Khammam, Telangana', 'Jaipur, Rajasthan', 'Wokha, Nagaland',
       'Mysore, Karnataka', 'Hyderabad, Telangana', 'Kota, Rajasthan',
       'Tawang, Arunachal Pradesh', 'Ziro, Arunachal Pradesh',
       'Shimla, Himachal Pradesh', 'Kolasib, Mizoram',
       'West Delhi, Delhi', 'Vasco da Gama, Goa', 'Namchi, Sikkim',
       'Thoubal, Manipur', 'Tura, Meghalaya', 'Pune, Maharashtra',
       'Diu, Dadra and Nagar Haveli and Daman and Diu',
       'Hubli, Karnataka', 'Ranchi, Jharkhand', 'Yanam, Puducherry',
       'South Delhi, Delhi', 'Mokokchung, Nagaland', 'North Delhi, Delhi',
       'Surat, Gujarat', 'Dehradun, Uttarakhand', 'Hazaribagh, Jharkhand',
       'Mumbai, Maharashtra', 'Visakhapatnam, Andhra Pradesh',
       'Manali, Himachal Pradesh', 'Rourkela, Odisha',
       'Car Nicobar, Andaman and Nicobar Islands', 'Berhampur, Odisha',
       'Sambalpur, Odisha', 'Udaipur, Rajasthan',
       'Ujjain, Madhya Pradesh', 'Meerut, Uttar Pradesh',
       'Trichy, Tamil Nadu', 'Gangtok, Sikkim', 'Munger, Bihar',
       'Kangra, Himachal Pradesh', 'Patna, Bihar', 'Margao, Goa',
       'Muzaffarpur, Bihar', 'Karaikal, Puducherry', 'East Delhi, Delhi',
       'Guntur, Andhra Pradesh', 'Guwahati, Assam', 'Lunglei, Mizoram',
       'Lucknow, Uttar Pradesh', 'Shillong, Meghalaya',
       'Indore, Madhya Pradesh', 'Panaji, Goa', 'Cuttack, Odisha',
       'Faridabad, Haryana', 'Haldwani, Uttarakhand',
       'Madurai, Tamil Nadu', 'Jalandhar, Punjab', 'Bhavnagar, Gujarat',
       'Kozhikode, Kerala', 'Rishikesh, Uttarakhand',
       'Gwalior, Madhya Pradesh', 'Nainital, Uttarakhand',
       'Asansol, West Bengal', 'Mangan, Sikkim', 'Kochi, Kerala',
       'Silchar, Assam', 'Itanagar, Arunachal Pradesh',
       'Warangal, Telangana', 'Kullu, Himachal Pradesh',
       'Chandigarh, Haryana', 'Bangalore, Karnataka',
       'Haridwar, Uttarakhand', 'Rajkot, Gujarat', 'Mangalore, Karnataka',
       'Mahe, Puducherry', 'Kangpokpi, Manipur', 'Dimapur, Nagaland',
       'Coimbatore, Tamil Nadu', 'Howrah, West Bengal', 'Nagaon, Assam',
       'Puducherry, Puducherry', 'Dharmanagar, Tripura',
       'Dhanbad, Jharkhand', 'Ajmer, Rajasthan', 'Jowai, Meghalaya'],index=1)
Thiruvananthapuram_Kerala = 0
Nashik_Maharashtra = 0
Bhagalpur_Bihar = 0
Chennai_Tamil_Nadu = 0
Amritsar_Punjab = 0
Ahmedabad_Gujarat = 0
New_Delhi_Delhi = 0
Port_Blair_Andaman_and_Nicobar_Islands = 0
Bhopal_Madhya_Pradesh = 0
Jagdalpur_Chhattisgarh = 0
Vadodara_Gujarat = 0
Chandigarh_Punjab = 0
Champhai_Mizoram = 0
Korba_Chhattisgarh = 0
Kolkata_West_Bengal = 0
Gaya_Bihar = 0
Jorethang_Sikkim = 0
Silvassa_Dadra_and_Nagar_Haveli_and_Daman_and_Diu = 0
Kanpur_Uttar_Pradesh = 0
Nagpur_Maharashtra = 0
Bhubaneswar_Odisha = 0
Ambassa_Tripura = 0
Jorhat_Assam = 0
Diglipur_Andaman_and_Nicobar_Islands = 0
Salem_Tamil_Nadu = 0
Durg_Chhattisgarh = 0
Churachandpur_Manipur = 0
Kottayam_Kerala = 0
Varanasi_Uttar_Pradesh = 0
Imphal_Manipur = 0
Belgaum_Karnataka = 0
Agra_Uttar_Pradesh = 0
Durgapur_West_Bengal = 0
Daman_Dadra_and_Nagar_Haveli_and_Daman_and_Diu = 0
Bilaspur_Chhattisgarh = 0
Nellore_Andhra_Pradesh = 0
Patiala_Punjab = 0
Jabalpur_Madhya_Pradesh = 0
Mapusa_Goa = 0
Agartala_Tripura = 0
Aurangabad_Maharashtra = 0
Gurugram_Haryana = 0
Vijayawada_Andhra_Pradesh = 0
Kavaratti_Lakshadweep = 0
Bokaro_Jharkhand = 0
Siliguri_West_Bengal = 0
Udaipur_Tripura = 0
Nongstoin_Meghalaya = 0
Tirupati_Andhra_Pradesh = 0
Jamshedpur_Jharkhand = 0
Chandigarh_Chandigarh = 0
Ludhiana_Punjab = 0
Aizawl_Mizoram = 0
Raipur_Chhattisgarh = 0
Naharlagun_Arunachal_Pradesh = 0
Trichur_Kerala = 0
Kohima_Nagaland = 0
Ambala_Haryana = 0
Hisar_Haryana = 0
Nizamabad_Telangana = 0
Dibrugarh_Assam = 0
Karimnagar_Telangana = 0
Jodhpur_Rajasthan = 0
Khammam_Telangana = 0
Jaipur_Rajasthan = 0
Wokha_Nagaland = 0
Mysore_Karnataka = 0
Hyderabad_Telangana = 0
Kota_Rajasthan = 0
Tawang_Arunachal_Pradesh = 0
Ziro_Arunachal_Pradesh = 0
Shimla_Himachal_Pradesh = 0
Kolasib_Mizoram = 0
West_Delhi_Delhi = 0
Vasco_da_Gama_Goa = 0
Namchi_Sikkim = 0
Thoubal_Manipur = 0
Tura_Meghalaya = 0
Pune_Maharashtra = 0
Diu_Dadra_and_Nagar_Haveli_and_Daman_and_Diu = 0
Hubli_Karnataka = 0
Ranchi_Jharkhand = 0
Yanam_Puducherry = 0
South_Delhi_Delhi = 0
Mokokchung_Nagaland = 0
North_Delhi_Delhi = 0
Surat_Gujarat = 0
Dehradun_Uttarakhand = 0
Hazaribagh_Jharkhand = 0
Mumbai_Maharashtra = 0
Visakhapatnam_Andhra_Pradesh = 0
Manali_Himachal_Pradesh = 0
Rourkela_Odisha = 0
Car_Nicobar_Andaman_and_Nicobar_Islands = 0
Berhampur_Odisha = 0
Sambalpur_Odisha = 0
Udaipur_Rajasthan = 0
Ujjain_Madhya_Pradesh = 0
Meerut_Uttar_Pradesh = 0
Trichy_Tamil_Nadu = 0
Gangtok_Sikkim = 0
Munger_Bihar = 0
Kangra_Himachal_Pradesh = 0
Patna_Bihar = 0
Margao_Goa = 0
Muzaffarpur_Bihar = 0
Karaikal_Puducherry = 0
East_Delhi_Delhi = 0
Guntur_Andhra_Pradesh = 0
Guwahati_Assam = 0
Lunglei_Mizoram = 0
Lucknow_Uttar_Pradesh = 0
Shillong_Meghalaya = 0
Indore_Madhya_Pradesh = 0
Panaji_Goa = 0
Cuttack_Odisha = 0
Faridabad_Haryana = 0
Haldwani_Uttarakhand = 0
Madurai_Tamil_Nadu = 0
Jalandhar_Punjab = 0
Bhavnagar_Gujarat = 0
Kozhikode_Kerala = 0
Rishikesh_Uttarakhand = 0
Gwalior_Madhya_Pradesh = 0
Nainital_Uttarakhand = 0
Asansol_West_Bengal = 0
Mangan_Sikkim = 0
Kochi_Kerala = 0
Silchar_Assam = 0
Itanagar_Arunachal_Pradesh = 0
Warangal_Telangana = 0
Kullu_Himachal_Pradesh = 0
Chandigarh_Haryana = 0
Bangalore_Karnataka = 0
Haridwar_Uttarakhand = 0
Rajkot_Gujarat = 0
Mangalore_Karnataka = 0
Mahe_Puducherry = 0
Kangpokpi_Manipur = 0
Dimapur_Nagaland = 0
Coimbatore_Tamil_Nadu = 0
Howrah_West_Bengal = 0
Nagaon_Assam = 0
Puducherry_Puducherry = 0
Dharmanagar_Tripura = 0
Dhanbad_Jharkhand = 0
Ajmer_Rajasthan = 0
Jowai_Meghalaya = 0

# Manual one-hot encoding
if Transaction_location == 'Thiruvananthapuram, Kerala':
    Thiruvananthapuram_Kerala = 1
elif Transaction_location == 'Nashik, Maharashtra':
    Nashik_Maharashtra = 1
elif Transaction_location == 'Bhagalpur, Bihar':
    Bhagalpur_Bihar = 1
elif Transaction_location == 'Chennai, Tamil Nadu':
    Chennai_Tamil_Nadu = 1
elif Transaction_location == 'Amritsar, Punjab':
    Amritsar_Punjab = 1
elif Transaction_location == 'Ahmedabad, Gujarat':
    Ahmedabad_Gujarat = 1
elif Transaction_location == 'New Delhi, Delhi':
    New_Delhi_Delhi = 1
elif Transaction_location == 'Port Blair, Andaman and Nicobar Islands':
    Port_Blair_Andaman_and_Nicobar_Islands = 1
elif Transaction_location == 'Bhopal, Madhya Pradesh':
    Bhopal_Madhya_Pradesh = 1
elif Transaction_location == 'Jagdalpur, Chhattisgarh':
    Jagdalpur_Chhattisgarh = 1
elif Transaction_location == 'Vadodara, Gujarat':
    Vadodara_Gujarat = 1
elif Transaction_location == 'Chandigarh, Punjab':
    Chandigarh_Punjab = 1
elif Transaction_location == 'Champhai, Mizoram':
    Champhai_Mizoram = 1
elif Transaction_location == 'Korba, Chhattisgarh':
    Korba_Chhattisgarh = 1
elif Transaction_location == 'Kolkata, West Bengal':
    Kolkata_West_Bengal = 1
elif Transaction_location == 'Gaya, Bihar':
    Gaya_Bihar = 1
elif Transaction_location == 'Jorethang, Sikkim':
    Jorethang_Sikkim = 1
elif Transaction_location == 'Silvassa, Dadra and Nagar Haveli and Daman and Diu':
    Silvassa_Dadra_and_Nagar_Haveli_and_Daman_and_Diu = 1
elif Transaction_location == 'Kanpur, Uttar Pradesh':
    Kanpur_Uttar_Pradesh = 1
elif Transaction_location == 'Nagpur, Maharashtra':
    Nagpur_Maharashtra = 1
elif Transaction_location == 'Bhubaneswar, Odisha':
    Bhubaneswar_Odisha = 1
elif Transaction_location == 'Ambassa, Tripura':
    Ambassa_Tripura = 1
elif Transaction_location == 'Jorhat, Assam':
    Jorhat_Assam = 1
elif Transaction_location == 'Diglipur, Andaman and Nicobar Islands':
    Diglipur_Andaman_and_Nicobar_Islands = 1
elif Transaction_location == 'Salem, Tamil Nadu':
    Salem_Tamil_Nadu = 1
elif Transaction_location == 'Durg, Chhattisgarh':
    Durg_Chhattisgarh = 1
elif Transaction_location == 'Churachandpur, Manipur':
    Churachandpur_Manipur = 1
elif Transaction_location == 'Kottayam, Kerala':
    Kottayam_Kerala = 1
elif Transaction_location == 'Varanasi, Uttar Pradesh':
    Varanasi_Uttar_Pradesh = 1
elif Transaction_location == 'Imphal, Manipur':
    Imphal_Manipur = 1
elif Transaction_location == 'Belgaum, Karnataka':
    Belgaum_Karnataka = 1
elif Transaction_location == 'Agra, Uttar Pradesh':
    Agra_Uttar_Pradesh = 1
elif Transaction_location == 'Durgapur, West Bengal':
    Durgapur_West_Bengal = 1
elif Transaction_location == 'Daman, Dadra and Nagar Haveli and Daman and Diu':
    Daman_Dadra_and_Nagar_Haveli_and_Daman_and_Diu = 1
elif Transaction_location == 'Bilaspur, Chhattisgarh':
    Bilaspur_Chhattisgarh = 1
elif Transaction_location == 'Nellore, Andhra Pradesh':
    Nellore_Andhra_Pradesh = 1
elif Transaction_location == 'Patiala, Punjab':
    Patiala_Punjab = 1
elif Transaction_location == 'Jabalpur, Madhya Pradesh':
    Jabalpur_Madhya_Pradesh = 1
elif Transaction_location == 'Mapusa, Goa':
    Mapusa_Goa = 1
elif Transaction_location == 'Agartala, Tripura':
    Agartala_Tripura = 1
elif Transaction_location == 'Aurangabad, Maharashtra':
    Aurangabad_Maharashtra = 1
elif Transaction_location == 'Gurugram, Haryana':
    Gurugram_Haryana = 1
elif Transaction_location == 'Vijayawada, Andhra Pradesh':
    Vijayawada_Andhra_Pradesh = 1
elif Transaction_location == 'Kavaratti, Lakshadweep':
    Kavaratti_Lakshadweep = 1
elif Transaction_location == 'Bokaro, Jharkhand':
    Bokaro_Jharkhand = 1
elif Transaction_location == 'Siliguri, West Bengal':
    Siliguri_West_Bengal = 1
elif Transaction_location == 'Udaipur, Tripura':
    Udaipur_Tripura = 1
elif Transaction_location == 'Nongstoin, Meghalaya':
    Nongstoin_Meghalaya = 1
elif Transaction_location == 'Tirupati, Andhra Pradesh':
    Tirupati_Andhra_Pradesh = 1
elif Transaction_location == 'Jamshedpur, Jharkhand':
    Jamshedpur_Jharkhand = 1
elif Transaction_location == 'Chandigarh, Chandigarh':
    Chandigarh_Chandigarh = 1
elif Transaction_location == 'Ludhiana, Punjab':
    Ludhiana_Punjab = 1
elif Transaction_location == 'Aizawl, Mizoram':
    Aizawl_Mizoram = 1
elif Transaction_location == 'Raipur, Chhattisgarh':
    Raipur_Chhattisgarh = 1
elif Transaction_location == 'Naharlagun, Arunachal Pradesh':
    Naharlagun_Arunachal_Pradesh = 1
elif Transaction_location == 'Trichur, Kerala':
    Trichur_Kerala = 1
elif Transaction_location == 'Kohima, Nagaland':
    Kohima_Nagaland = 1
elif Transaction_location == 'Ambala, Haryana':
    Ambala_Haryana = 1
elif Transaction_location == 'Hisar, Haryana':
    Hisar_Haryana = 1
elif Transaction_location == 'Nizamabad, Telangana':
    Nizamabad_Telangana = 1
elif Transaction_location == 'Dibrugarh, Assam':
    Dibrugarh_Assam = 1
elif Transaction_location == 'Karimnagar, Telangana':
    Karimnagar_Telangana = 1
elif Transaction_location == 'Jodhpur, Rajasthan':
    Jodhpur_Rajasthan = 1
elif Transaction_location == 'Khammam, Telangana':
    Khammam_Telangana = 1
elif Transaction_location == 'Jaipur, Rajasthan':
    Jaipur_Rajasthan = 1
elif Transaction_location == 'Wokha, Nagaland':
    Wokha_Nagaland = 1
elif Transaction_location == 'Mysore, Karnataka':
    Mysore_Karnataka = 1
elif Transaction_location == 'Hyderabad, Telangana':
    Hyderabad_Telangana = 1
elif Transaction_location == 'Kota, Rajasthan':
    Kota_Rajasthan = 1
elif Transaction_location == 'Tawang, Arunachal Pradesh':
    Tawang_Arunachal_Pradesh = 1
elif Transaction_location == 'Ziro, Arunachal Pradesh':
    Ziro_Arunachal_Pradesh = 1
elif Transaction_location == 'Shimla, Himachal Pradesh':
    Shimla_Himachal_Pradesh = 1
elif Transaction_location == 'Kolasib, Mizoram':
    Kolasib_Mizoram = 1
elif Transaction_location == 'West Delhi, Delhi':
    West_Delhi_Delhi = 1
elif Transaction_location == 'Vasco da Gama, Goa':
    Vasco_da_Gama_Goa = 1
elif Transaction_location == 'Namchi, Sikkim':
    Namchi_Sikkim = 1
elif Transaction_location == 'Thoubal, Manipur':
    Thoubal_Manipur = 1
elif Transaction_location == 'Tura, Meghalaya':
    Tura_Meghalaya = 1
elif Transaction_location == 'Pune, Maharashtra':
    Pune_Maharashtra = 1
elif Transaction_location == 'Diu, Dadra and Nagar Haveli and Daman and Diu':
    Diu_Dadra_and_Nagar_Haveli_and_Daman_and_Diu = 1
elif Transaction_location == 'Hubli, Karnataka':
    Hubli_Karnataka = 1
elif Transaction_location == 'Ranchi, Jharkhand':
    Ranchi_Jharkhand = 1
elif Transaction_location == 'Yanam, Puducherry':
    Yanam_Puducherry = 1
elif Transaction_location == 'South Delhi, Delhi':
    South_Delhi_Delhi = 1
elif Transaction_location == 'Mokokchung, Nagaland':
    Mokokchung_Nagaland = 1
elif Transaction_location == 'North Delhi, Delhi':
    North_Delhi_Delhi = 1
elif Transaction_location == 'Surat, Gujarat':
    Surat_Gujarat = 1
elif Transaction_location == 'Dehradun, Uttarakhand':
    Dehradun_Uttarakhand = 1
elif Transaction_location == 'Hazaribagh, Jharkhand':
    Hazaribagh_Jharkhand = 1
elif Transaction_location == 'Mumbai, Maharashtra':
    Mumbai_Maharashtra = 1
elif Transaction_location == 'Visakhapatnam, Andhra Pradesh':
    Visakhapatnam_Andhra_Pradesh = 1
elif Transaction_location == 'Manali, Himachal Pradesh':
    Manali_Himachal_Pradesh = 1
elif Transaction_location == 'Rourkela, Odisha':
    Rourkela_Odisha = 1
elif Transaction_location == 'Car Nicobar, Andaman and Nicobar Islands':
    Car_Nicobar_Andaman_and_Nicobar_Islands = 1
elif Transaction_location == 'Berhampur, Odisha':
    Berhampur_Odisha = 1
elif Transaction_location == 'Sambalpur, Odisha':
    Sambalpur_Odisha = 1
elif Transaction_location == 'Udaipur, Rajasthan':
    Udaipur_Rajasthan = 1
elif Transaction_location == 'Ujjain, Madhya Pradesh':
    Ujjain_Madhya_Pradesh = 1
elif Transaction_location == 'Meerut, Uttar Pradesh':
    Meerut_Uttar_Pradesh = 1
elif Transaction_location == 'Trichy, Tamil Nadu':
    Trichy_Tamil_Nadu = 1
elif Transaction_location == 'Gangtok, Sikkim':
    Gangtok_Sikkim = 1
elif Transaction_location == 'Munger, Bihar':
    Munger_Bihar = 1
elif Transaction_location == 'Kangra, Himachal Pradesh':
    Kangra_Himachal_Pradesh = 1
elif Transaction_location == 'Patna, Bihar':
    Patna_Bihar = 1
elif Transaction_location == 'Margao, Goa':
    Margao_Goa = 1
elif Transaction_location == 'Muzaffarpur, Bihar':
    Muzaffarpur_Bihar = 1
elif Transaction_location == 'Karaikal, Puducherry':
    Karaikal_Puducherry = 1
elif Transaction_location == 'East Delhi, Delhi':
    East_Delhi_Delhi = 1
elif Transaction_location == 'Guntur, Andhra Pradesh':
    Guntur_Andhra_Pradesh = 1
elif Transaction_location == 'Guwahati, Assam':
    Guwahati_Assam = 1
elif Transaction_location == 'Lunglei, Mizoram':
    Lunglei_Mizoram = 1
elif Transaction_location == 'Lucknow, Uttar Pradesh':
    Lucknow_Uttar_Pradesh = 1
elif Transaction_location == 'Shillong, Meghalaya':
    Shillong_Meghalaya = 1
elif Transaction_location == 'Indore, Madhya Pradesh':
    Indore_Madhya_Pradesh = 1
elif Transaction_location == 'Panaji, Goa':
    Panaji_Goa = 1
elif Transaction_location == 'Cuttack, Odisha':
    Cuttack_Odisha = 1
elif Transaction_location == 'Faridabad, Haryana':
    Faridabad_Haryana = 1
elif Transaction_location == 'Haldwani, Uttarakhand':
    Haldwani_Uttarakhand = 1
elif Transaction_location == 'Madurai, Tamil Nadu':
    Madurai_Tamil_Nadu = 1
elif Transaction_location == 'Jalandhar, Punjab':
    Jalandhar_Punjab = 1
elif Transaction_location == 'Bhavnagar, Gujarat':
    Bhavnagar_Gujarat = 1
elif Transaction_location == 'Kozhikode, Kerala':
    Kozhikode_Kerala = 1
elif Transaction_location == 'Rishikesh, Uttarakhand':
    Rishikesh_Uttarakhand = 1
elif Transaction_location == 'Gwalior, Madhya Pradesh':
    Gwalior_Madhya_Pradesh = 1
elif Transaction_location == 'Nainital, Uttarakhand':
    Nainital_Uttarakhand = 1
elif Transaction_location == 'Asansol, West Bengal':
    Asansol_West_Bengal = 1
elif Transaction_location == 'Mangan, Sikkim':
    Mangan_Sikkim = 1
elif Transaction_location == 'Kochi, Kerala':
    Kochi_Kerala = 1
elif Transaction_location == 'Silchar, Assam':
    Silchar_Assam = 1
elif Transaction_location == 'Itanagar, Arunachal Pradesh':
    Itanagar_Arunachal_Pradesh = 1
elif Transaction_location == 'Warangal, Telangana':
    Warangal_Telangana = 1
elif Transaction_location == 'Kullu, Himachal Pradesh':
    Kullu_Himachal_Pradesh = 1
elif Transaction_location == 'Chandigarh, Haryana':
    Chandigarh_Haryana = 1
elif Transaction_location == 'Bangalore, Karnataka':
    Bangalore_Karnataka = 1
elif Transaction_location == 'Haridwar, Uttarakhand':
    Haridwar_Uttarakhand = 1
elif Transaction_location == 'Rajkot, Gujarat':
    Rajkot_Gujarat = 1
elif Transaction_location == 'Mangalore, Karnataka':
    Mangalore_Karnataka = 1
elif Transaction_location == 'Mahe, Puducherry':
    Mahe_Puducherry = 1
elif Transaction_location == 'Kangpokpi, Manipur':
    Kangpokpi_Manipur = 1
elif Transaction_location == 'Dimapur, Nagaland':
    Dimapur_Nagaland = 1
elif Transaction_location == 'Coimbatore, Tamil Nadu':
    Coimbatore_Tamil_Nadu = 1
elif Transaction_location == 'Howrah, West Bengal':
    Howrah_West_Bengal = 1
elif Transaction_location == 'Nagaon, Assam':
    Nagaon_Assam = 1
elif Transaction_location == 'Puducherry, Puducherry':
    Puducherry_Puducherry = 1
elif Transaction_location == 'Dharmanagar, Tripura':
    Dharmanagar_Tripura = 1
elif Transaction_location == 'Dhanbad, Jharkhand':
    Dhanbad_Jharkhand = 1
elif Transaction_location == 'Ajmer, Rajasthan':
    Ajmer_Rajasthan = 1
elif Transaction_location == 'Jowai, Meghalaya':
    Jowai_Meghalaya = 1

Transaction_Description = st.selectbox('Transaction description',options = ['Bitcoin transaction', 'Grocery delivery',
       'Mutual fund investment', 'Food delivery', 'Debt repayment',
       'Seminar registration', 'Public transport pass', 'Online shopping',
       'Vacation payment', 'Electronics purchase',
       'Streaming service subscription', 'Subscription renewal',
       'Laundry service', 'Personal loan repayment', 'Insurance premium',
       'Pet care', 'Gift for colleague', 'Smart home device purchase',
       'Beauty products', 'Car service', 'Specialty store shopping',
       'Charity donation', 'Taxi fare', 'Christmas shopping',
       'Online subscription', 'Restaurant dining',
       'Loyalty points redemption', 'Mobile phone payment',
       'Bank transfer', 'Property tax payment', 'Penalty fee',
       'School fee payment', 'Online gaming', 'Cryptocurrency purchase',
       'Team lunch', 'Credit card payment', 'Membership subscription',
       'Stock investment', 'Transportation fare', 'Jewelry purchase',
       'Corporate event ticket', 'Tech gadgets purchase',
       'Bookstore purchase', 'Tax payment', 'Doctor consultation',
       'Home repairs', 'Installment payment', 'Clinic payment',
       'Ridesharing service', 'Digital media purchase',
       'Department store shopping', 'Health insurance payment',
       'Food subscription', 'Subscription service', 'Mobile recharge',
       'Fine payment', 'Real estate payment', 'Phone accessories',
       'Car rental', 'Transfer', 'Music concert tickets', 'Pharmacy bill',
       'Shopping mall purchase', 'Online book purchase', 'Meal plan',
       'Luxury item purchase', 'Hotel booking', 'New year shopping',
       'Taxi booking', 'Online course payment', 'Fitness membership',
       'Online clothing store', 'Hiring fee', 'Subscription payment',
       'Grocery shopping', 'Camping trip', 'Withdrawal', 'Bike rental',
       'Sports equipment purchase', 'Fund transfer',
       'Online fitness class', 'Monthly installment', 'Insurance claim',
       'Gift for partner', 'Home decor', 'Medical treatment payment',
       'Business expense', 'Crowdfunding contribution', 'Freight charges',
       'Tuition fee payment', 'Birthday present',
       'Electronic gadget repair', 'Sports equipment', 'Courier charges',
       'Travel agency payment', 'Student loan repayment',
       'Home cleaning services', 'Dinner payment', 'Import duty payment',
       'E-commerce refund', 'Camping gear purchase', 'Vehicle insurance',
       'Online education', 'Investment in gold',
       'Moving services payment', 'Sports ticket', 'Parking charges',
       'Gifts and souvenirs', 'Conference fee', 'Healthcare premium',
       'Bill payment', 'Long-distance transport', 'Streaming service',
       'POS transaction', 'Hotel reservation', 'Hospital bill',
       'Subscription fee', 'Gym membership', 'Apparel purchase',
       'Tourist attraction payment', 'Wedding shopping',
       'Utility service', 'Pharmacy purchase', 'Childcare expense',
       'Document notarization', 'Senior citizen care',
       'Legal services payment', 'Training course fee', 'Home renovation',
       'Travel expenses', 'Travel insurance', 'Loan repayment',
       'Bank fee', 'Political donation', 'Furniture purchase',
       'Utility bill payment', 'Customer service charge',
       'Gifts for parents', 'Online software purchase', 'Ticket booking',
       'Spa treatment', 'Flight booking', 'Movie tickets',
       'Fuel purchase', 'Children’s clothing', 'Children’s toys',
       'Charity contribution', 'Cash deposit', 'Freelancer payment',
       'Gift for friend', 'Lunch payment', 'Personal finance consulting',
       'Consulting fee', 'Clothing purchase', 'Event ticket purchase',
       'Wedding gift', 'ATM withdrawal', 'Airline ticket',
       'Home appliance repair', 'Gift card purchase', 'Bus fare',
       'Cafe purchase', 'Loan payment', 'Contract renewal',
       'Streaming subscription', 'Gifts for family', 'Car repair service',
       'Electronics rental', 'Petroleum purchase', 'Online workshop',
       'Wedding anniversary gift', 'Subscription box'],index=1)
# Initialize all transaction descriptions to 0
Bitcoin_transaction = 0
Grocery_delivery = 0
Mutual_fund_investment = 0
Food_delivery = 0
Debt_repayment = 0
Seminar_registration = 0
Public_transport_pass = 0
Online_shopping = 0
Vacation_payment = 0
Electronics_purchase = 0
Streaming_service_subscription = 0
Subscription_renewal = 0
Laundry_service = 0
Personal_loan_repayment = 0
Insurance_premium = 0
Pet_care = 0
Gift_for_colleague = 0
Smart_home_device_purchase = 0
Beauty_products = 0
Car_service = 0
Specialty_store_shopping = 0
Charity_donation = 0
Taxi_fare = 0
Christmas_shopping = 0
Online_subscription = 0
Restaurant_dining = 0
Loyalty_points_redemption = 0
Mobile_phone_payment = 0
Bank_transfer = 0
Property_tax_payment = 0
Penalty_fee = 0
School_fee_payment = 0
Online_gaming = 0
Cryptocurrency_purchase = 0
Team_lunch = 0
Credit_card_payment = 0
Membership_subscription = 0
Stock_investment = 0
Transportation_fare = 0
Jewelry_purchase = 0
Corporate_event_ticket = 0
Tech_gadgets_purchase = 0
Bookstore_purchase = 0
Tax_payment = 0
Doctor_consultation = 0
Home_repairs = 0
Installment_payment = 0
Clinic_payment = 0
Ridesharing_service = 0
Digital_media_purchase = 0
Department_store_shopping = 0
Health_insurance_payment = 0
Food_subscription = 0
Subscription_service = 0
Mobile_recharge = 0
Fine_payment = 0
Real_estate_payment = 0
Phone_accessories = 0
Car_rental = 0
Transfer = 0
Music_concert_tickets = 0
Pharmacy_bill = 0
Shopping_mall_purchase = 0
Online_book_purchase = 0
Meal_plan = 0
Luxury_item_purchase = 0
Hotel_booking = 0
New_year_shopping = 0
Taxi_booking = 0
Online_course_payment = 0
Fitness_membership = 0
Online_clothing_store = 0
Hiring_fee = 0
Subscription_payment = 0
Grocery_shopping = 0
Camping_trip = 0
Withdrawal = 0
Bike_rental = 0
Sports_equipment_purchase = 0
Fund_transfer = 0
Online_fitness_class = 0
Monthly_installment = 0
Insurance_claim = 0
Gift_for_partner = 0
Home_decor = 0
Medical_treatment_payment = 0
Business_expense = 0
Crowdfunding_contribution = 0
Freight_charges = 0
Tuition_fee_payment = 0
Birthday_present = 0
Electronic_gadget_repair = 0
Sports_equipment = 0
Courier_charges = 0
Travel_agency_payment = 0
Student_loan_repayment = 0
Home_cleaning_services = 0
Dinner_payment = 0
Import_duty_payment = 0
E_commerce_refund = 0
Camping_gear_purchase = 0
Vehicle_insurance = 0
Online_education = 0
Investment_in_gold = 0
Moving_services_payment = 0
Sports_ticket = 0
Parking_charges = 0
Gifts_and_souvenirs = 0
Conference_fee = 0
Healthcare_premium = 0
Bill_payment = 0
Long_distance_transport = 0
Streaming_service = 0
POS_transaction = 0
Hotel_reservation = 0
Hospital_bill = 0
Subscription_fee = 0
Gym_membership = 0
Apparel_purchase = 0
Tourist_attraction_payment = 0
Wedding_shopping = 0
Utility_service = 0
Pharmacy_purchase = 0
Childcare_expense = 0
Document_notarization = 0
Senior_citizen_care = 0
Legal_services_payment = 0
Training_course_fee = 0
Home_renovation = 0
Travel_expenses = 0
Travel_insurance = 0
Loan_repayment = 0
Bank_fee = 0
Political_donation = 0
Furniture_purchase = 0
Utility_bill_payment = 0
Customer_service_charge = 0
Gifts_for_parents = 0
Online_software_purchase = 0
Ticket_booking = 0
Spa_treatment = 0
Flight_booking = 0
Movie_tickets = 0
Fuel_purchase = 0
Childrens_clothing = 0
Childrens_toys = 0
Charity_contribution = 0
Cash_deposit = 0
Freelancer_payment = 0
Gift_for_friend = 0
Lunch_payment = 0
Personal_finance_consulting = 0
Consulting_fee = 0
Clothing_purchase = 0
Event_ticket_purchase = 0
Wedding_gift = 0
ATM_withdrawal = 0
Airline_ticket = 0
Home_appliance_repair = 0
Gift_card_purchase = 0
Bus_fare = 0
Cafe_purchase = 0
Loan_payment = 0
Contract_renewal = 0
Streaming_subscription = 0
Gifts_for_family = 0
Car_repair_service = 0
Electronics_rental = 0
Petroleum_purchase = 0
Online_workshop = 0
blob1=0
blob2=0
blob3=0
blob4=0
blob5=0
Wedding_anniversary_gift = 0
Subscription_box = 0

# Manual one-hot encoding
if Transaction_Description == 'Bitcoin transaction':
    Bitcoin_transaction = 1
elif Transaction_Description == 'Grocery delivery':
    Grocery_delivery = 1
elif Transaction_Description == 'Mutual fund investment':
    Mutual_fund_investment = 1
elif Transaction_Description == 'Food delivery':
    Food_delivery = 1
elif Transaction_Description == 'Debt repayment':
    Debt_repayment = 1
elif Transaction_Description == 'Seminar registration':
    Seminar_registration = 1
elif Transaction_Description == 'Public transport pass':
    Public_transport_pass = 1
elif Transaction_Description == 'Online shopping':
    Online_shopping = 1
elif Transaction_Description == 'Vacation payment':
    Vacation_payment = 1
elif Transaction_Description == 'Electronics purchase':
    Electronics_purchase = 1
elif Transaction_Description == 'Streaming service subscription':
    Streaming_service_subscription = 1
elif Transaction_Description == 'Subscription renewal':
    Subscription_renewal = 1
elif Transaction_Description == 'Laundry service':
    Laundry_service = 1
elif Transaction_Description == 'Personal loan repayment':
    Personal_loan_repayment = 1
elif Transaction_Description == 'Insurance premium':
    Insurance_premium = 1
elif Transaction_Description == 'Pet care':
    Pet_care = 1
elif Transaction_Description == 'Gift for colleague':
    Gift_for_colleague = 1
elif Transaction_Description == 'Smart home device purchase':
    Smart_home_device_purchase = 1
elif Transaction_Description == 'Beauty products':
    Beauty_products = 1
elif Transaction_Description == 'Car service':
    Car_service = 1
elif Transaction_Description == 'Specialty store shopping':
    Specialty_store_shopping = 1
elif Transaction_Description == 'Charity donation':
    Charity_donation = 1
elif Transaction_Description == 'Taxi fare':
    Taxi_fare = 1
elif Transaction_Description == 'Christmas shopping':
    Christmas_shopping = 1
elif Transaction_Description == 'Online subscription':
    Online_subscription = 1
elif Transaction_Description == 'Restaurant dining':
    Restaurant_dining = 1
elif Transaction_Description == 'Loyalty points redemption':
    Loyalty_points_redemption = 1
elif Transaction_Description == 'Mobile phone payment':
    Mobile_phone_payment = 1
elif Transaction_Description == 'Bank transfer':
    Bank_transfer = 1
elif Transaction_Description == 'Property tax payment':
    Property_tax_payment = 1
elif Transaction_Description == 'Penalty fee':
    Penalty_fee = 1
elif Transaction_Description == 'School fee payment':
    School_fee_payment = 1
elif Transaction_Description == 'Online gaming':
    Online_gaming = 1
elif Transaction_Description == 'Cryptocurrency purchase':
    Cryptocurrency_purchase = 1
elif Transaction_Description == 'Team lunch':
    Team_lunch = 1
elif Transaction_Description == 'Credit card payment':
    Credit_card_payment = 1
elif Transaction_Description == 'Membership subscription':
    Membership_subscription = 1
elif Transaction_Description == 'Stock investment':
    Stock_investment = 1
elif Transaction_Description == 'Transportation fare':
    Transportation_fare = 1
elif Transaction_Description == 'Jewelry purchase':
    Jewelry_purchase = 1
elif Transaction_Description == 'Corporate event ticket':
    Corporate_event_ticket = 1
elif Transaction_Description == 'Tech gadgets purchase':
    Tech_gadgets_purchase = 1
elif Transaction_Description == 'Bookstore purchase':
    Bookstore_purchase = 1
elif Transaction_Description == 'Tax payment':
    Tax_payment = 1
elif Transaction_Description == 'Doctor consultation':
    Doctor_consultation = 1
elif Transaction_Description == 'Home repairs':
    Home_repairs = 1
elif Transaction_Description == 'Installment payment':
    Installment_payment = 1
elif Transaction_Description == 'Clinic payment':
    Clinic_payment = 1
elif Transaction_Description == 'Ridesharing service':
    Ridesharing_service = 1
elif Transaction_Description == 'Digital media purchase':
    Digital_media_purchase = 1
elif Transaction_Description == 'Department store shopping':
    Department_store_shopping = 1
elif Transaction_Description == 'Health insurance payment':
    Health_insurance_payment = 1
elif Transaction_Description == 'Food subscription':
    Food_subscription = 1
elif Transaction_Description == 'Subscription service':
    Subscription_service = 1
elif Transaction_Description == 'Mobile recharge':
    Mobile_recharge = 1
elif Transaction_Description == 'Fine payment':
    Fine_payment = 1
elif Transaction_Description == 'Real estate payment':
    Real_estate_payment = 1
elif Transaction_Description == 'Phone accessories':
    Phone_accessories = 1
elif Transaction_Description == 'Car rental':
    Car_rental = 1
elif Transaction_Description == 'Transfer':
    Transfer = 1
elif Transaction_Description == 'Music concert tickets':
    Music_concert_tickets = 1
elif Transaction_Description == 'Pharmacy bill':
    Pharmacy_bill = 1
elif Transaction_Description == 'Shopping mall purchase':
    Shopping_mall_purchase = 1
elif Transaction_Description == 'Online book purchase':
    Online_book_purchase = 1
elif Transaction_Description == 'Meal plan':
    Meal_plan = 1
elif Transaction_Description == 'Luxury item purchase':
    Luxury_item_purchase = 1
elif Transaction_Description == 'Hotel booking':
    Hotel_booking = 1
elif Transaction_Description == 'New year shopping':
    New_year_shopping = 1
elif Transaction_Description == 'Taxi booking':
    Taxi_booking = 1
elif Transaction_Description == 'Online course payment':
    Online_course_payment = 1
elif Transaction_Description == 'Fitness membership':
    Fitness_membership = 1
elif Transaction_Description == 'Online clothing store':
    Online_clothing_store = 1
elif Transaction_Description == 'Hiring fee':
    Hiring_fee = 1
elif Transaction_Description == 'Subscription payment':
    Subscription_payment = 1
elif Transaction_Description == 'Grocery shopping':
    Grocery_shopping = 1
elif Transaction_Description == 'Camping trip':
    Camping_trip = 1
elif Transaction_Description == 'Withdrawal':
    Withdrawal = 1
elif Transaction_Description == 'Bike rental':
    Bike_rental = 1
elif Transaction_Description == 'Sports equipment purchase':
    Sports_equipment_purchase = 1
elif Transaction_Description == 'Fund transfer':
    Fund_transfer = 1
elif Transaction_Description == 'Online fitness class':
    Online_fitness_class = 1
elif Transaction_Description == 'Monthly installment':
    Monthly_installment = 1
elif Transaction_Description == 'Insurance claim':
    Insurance_claim = 1
elif Transaction_Description == 'Gift for partner':
    Gift_for_partner = 1
elif Transaction_Description == 'Home decor':
    Home_decor = 1
elif Transaction_Description == 'Medical treatment payment':
    Medical_treatment_payment = 1
elif Transaction_Description == 'Business expense':
    Business_expense = 1
elif Transaction_Description == 'Crowdfunding contribution':
    Crowdfunding_contribution = 1
elif Transaction_Description == 'Freight charges':
    Freight_charges = 1
elif Transaction_Description == 'Tuition fee payment':
    Tuition_fee_payment = 1
elif Transaction_Description == 'Birthday present':
    Birthday_present = 1
elif Transaction_Description == 'Electronic gadget repair':
    Electronic_gadget_repair = 1
elif Transaction_Description == 'Sports equipment':
    Sports_equipment = 1
elif Transaction_Description == 'Courier charges':
    Courier_charges = 1
elif Transaction_Description == 'Travel agency payment':
    Travel_agency_payment = 1
elif Transaction_Description == 'Student loan repayment':
    Student_loan_repayment = 1
elif Transaction_Description == 'Home cleaning services':
    Home_cleaning_services = 1
elif Transaction_Description == 'Dinner payment':
    Dinner_payment = 1
elif Transaction_Description == 'Import duty payment':
    Import_duty_payment = 1
elif Transaction_Description == 'E-commerce refund':
    E_commerce_refund = 1
elif Transaction_Description == 'Camping gear purchase':
    Camping_gear_purchase = 1
elif Transaction_Description == 'Vehicle insurance':
    Vehicle_insurance = 1
elif Transaction_Description == 'Online education':
    Online_education = 1
elif Transaction_Description == 'Investment in gold':
    Investment_in_gold = 1
elif Transaction_Description == 'Moving services payment':
    Moving_services_payment = 1
elif Transaction_Description == 'Sports ticket':
    Sports_ticket = 1
elif Transaction_Description == 'Parking charges':
    Parking_charges = 1
elif Transaction_Description == 'Gifts and souvenirs':
    Gifts_and_souvenirs = 1
elif Transaction_Description == 'Conference fee':
    Conference_fee = 1
elif Transaction_Description == 'Healthcare premium':
    Healthcare_premium = 1
elif Transaction_Description == 'Bill payment':
    Bill_payment = 1
elif Transaction_Description == 'Long-distance transport':
    Long_distance_transport = 1
elif Transaction_Description == 'Streaming service':
    Streaming_service = 1
elif Transaction_Description == 'POS transaction':
    POS_transaction = 1
elif Transaction_Description == 'Hotel reservation':
    Hotel_reservation = 1
elif Transaction_Description == 'Hospital bill':
    Hospital_bill = 1
elif Transaction_Description == 'Subscription fee':
    Subscription_fee = 1
elif Transaction_Description == 'Gym membership':
    Gym_membership = 1
elif Transaction_Description == 'Apparel purchase':
    Apparel_purchase = 1
elif Transaction_Description == 'Tourist attraction payment':
    Tourist_attraction_payment = 1
elif Transaction_Description == 'Wedding shopping':
    Wedding_shopping = 1
elif Transaction_Description == 'Utility service':
    Utility_service = 1
elif Transaction_Description == 'Pharmacy purchase':
    Pharmacy_purchase = 1
elif Transaction_Description == 'Childcare expense':
    Childcare_expense = 1
elif Transaction_Description == 'Document notarization':
    Document_notarization = 1
elif Transaction_Description == 'Senior citizen care':
    Senior_citizen_care = 1
elif Transaction_Description == 'Legal services payment':
    Legal_services_payment = 1
elif Transaction_Description == 'Training course fee':
    Training_course_fee = 1
elif Transaction_Description == 'Home renovation':
    Home_renovation = 1
elif Transaction_Description == 'Travel expenses':
    Travel_expenses = 1
elif Transaction_Description == 'Travel insurance':
    Travel_insurance = 1
elif Transaction_Description == 'Loan repayment':
    Loan_repayment = 1
elif Transaction_Description == 'Bank fee':
    Bank_fee = 1
elif Transaction_Description == 'Political donation':
    Political_donation = 1
elif Transaction_Description == 'Furniture purchase':
    Furniture_purchase = 1
elif Transaction_Description == 'Utility bill payment':
    Utility_bill_payment = 1
elif Transaction_Description == 'Customer service charge':
    Customer_service_charge = 1
elif Transaction_Description == 'Gifts for parents':
    Gifts_for_parents = 1
elif Transaction_Description == 'Online software purchase':
    Online_software_purchase = 1
elif Transaction_Description == 'Ticket booking':
    Ticket_booking = 1
elif Transaction_Description == 'Spa treatment':
    Spa_treatment = 1
elif Transaction_Description == 'Flight booking':
    Flight_booking = 1
elif Transaction_Description == 'Movie tickets':
    Movie_tickets = 1
elif Transaction_Description == 'Fuel purchase':
    Fuel_purchase = 1
elif Transaction_Description == 'Children’s clothing':
    Childrens_clothing = 1
elif Transaction_Description == 'Children’s toys':
    Childrens_toys = 1
elif Transaction_Description == 'Charity contribution':
    Charity_contribution = 1
elif Transaction_Description == 'Cash deposit':
    Cash_deposit = 1
elif Transaction_Description == 'Freelancer payment':
    Freelancer_payment = 1
elif Transaction_Description == 'Gift for friend':
    Gift_for_friend = 1
elif Transaction_Description == 'Lunch payment':
    Lunch_payment = 1
elif Transaction_Description == 'Personal finance consulting':
    Personal_finance_consulting = 1
elif Transaction_Description == 'Consulting fee':
    Consulting_fee = 1
elif Transaction_Description == 'Clothing purchase':
    Clothing_purchase = 1
elif Transaction_Description == 'Event ticket purchase':
    Event_ticket_purchase = 1
elif Transaction_Description == 'Wedding gift':
    Wedding_gift = 1
elif Transaction_Description == 'ATM withdrawal':
    ATM_withdrawal = 1
elif Transaction_Description == 'Airline ticket':
    Airline_ticket = 1
elif Transaction_Description == 'Home appliance repair':
    Home_appliance_repair = 1
elif Transaction_Description == 'Gift card purchase':
    Gift_card_purchase = 1
elif Transaction_Description == 'Bus fare':
    Bus_fare = 1
elif Transaction_Description == 'Cafe purchase':
    Cafe_purchase = 1
elif Transaction_Description == 'Loan payment':
    Loan_payment = 1
elif Transaction_Description == 'Contract renewal':
    Contract_renewal = 1
elif Transaction_Description == 'Streaming subscription':
    Streaming_subscription = 1
elif Transaction_Description == 'Gifts for family':
    Gifts_for_family = 1
elif Transaction_Description == 'Car repair service':
    Car_repair_service = 1
elif Transaction_Description == 'Electronics rental':
    Electronics_rental = 1
elif Transaction_Description == 'Petroleum purchase':
    Petroleum_purchase = 1
elif Transaction_Description == 'Online workshop':
    Online_workshop = 1
elif Transaction_Description == 'Wedding anniversary gift':
    Wedding_anniversary_gift = 1
elif Transaction_Description == 'Subscription box':
    Subscription_box = 1
from datetime import time

# Take time input from user
transaction_time = st.time_input("Enter transaction time", value=time(12, 0, 0))

# Extract hour, minute, and second
transaction_hour = transaction_time.hour
transaction_minute = transaction_time.minute
transaction_second = transaction_time.second
from datetime import date
# Take date input from user
transaction_date = st.date_input("Enter transaction date", value=date.today())

# Extract day, month, and year
transaction_day = transaction_date.day
transaction_month = transaction_date.month
transaction_year = transaction_date.year



# Manual label encoding
gender_map = {'Male': 0, 'Female': 1}
gender_encoded = gender_map[Gender]



#prepare input data
input_data = np.array([[Age, account_type, transaction_amount, transaction_type, merchant_category, account_balance, device, Andhra_Pradesh, Arunachal_Pradesh, Assam, Bihar, Chhattisgarh, Dadra_and_Nagar_Haveli_and_Daman_and_Diu, Delhi, Goa, Gujarat, Haryana, Himachal_Pradesh, Jharkhand, Karnataka, Kerala, Lakshadweep, Madhya_Pradesh, Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Odisha, Punjab, Rajasthan, Sikkim, Tamil_Nadu, Telangana, Tripura, Uttar_Pradesh, Uttarakhand, West_Bengal, Agra_Branch, Ahmedabad_Branch, Aizawl_Branch, Ajmer_Branch, Ambala_Branch, Ambassa_Branch, Amritsar_Branch, Asansol_Branch, Aurangabad_Branch, Bangalore_Branch, Belgaum_Branch, Berhampur_Branch, Bhagalpur_Branch, Bhavnagar_Branch, Bhopal_Branch, Bhubaneswar_Branch, Bilaspur_Branch, Bokaro_Branch, Car_Nicobar_Branch, Champhai_Branch, Chandigarh_Branch, Chennai_Branch, Churachandpur_Branch, Coimbatore_Branch, Cuttack_Branch, Daman_Branch, Dehradun_Branch, Dhanbad_Branch, Dharmanagar_Branch, Dibrugarh_Branch, Diglipur_Branch, Dimapur_Branch, Diu_Branch, Durg_Branch, Durgapur_Branch, East_Delhi_Branch, Faridabad_Branch, Gangtok_Branch, Gaya_Branch, Guntur_Branch, Gurugram_Branch, Guwahati_Branch, Gwalior_Branch, Haldwani_Branch, Haridwar_Branch, Hazaribagh_Branch, Hisar_Branch, Howrah_Branch, Hubli_Branch, Hyderabad_Branch, Imphal_Branch, Indore_Branch, Itanagar_Branch, Jabalpur_Branch, Jagdalpur_Branch, Jaipur_Branch, Jalandhar_Branch, Jamshedpur_Branch, Jodhpur_Branch, Jorethang_Branch, Jorhat_Branch, Jowai_Branch, Kangpokpi_Branch, Kangra_Branch, Kanpur_Branch, Karaikal_Branch, Karimnagar_Branch, Kavaratti_Branch, Khammam_Branch, Kochi_Branch, Kohima_Branch, Kolasib_Branch, Kolkata_Branch, Korba_Branch, Kota_Branch, Kottayam_Branch, Kozhikode_Branch, Kullu_Branch, Lucknow_Branch, Ludhiana_Branch, Lunglei_Branch, Madurai_Branch, Mahe_Branch, Manali_Branch, Mangalore_Branch, Mangan_Branch, Mapusa_Branch, Margao_Branch, Meerut_Branch, Mokokchung_Branch, Mumbai_Branch, Munger_Branch, Muzaffarpur_Branch, Mysore_Branch, Nagaon_Branch, Nagpur_Branch, Naharlagun_Branch, Nainital_Branch, Namchi_Branch, Nashik_Branch, Nellore_Branch, New_Delhi_Branch, Nizamabad_Branch, Nongstoin_Branch, North_Delhi_Branch, Panaji_Branch, Patiala_Branch, Patna_Branch, Port_Blair_Branch, Puducherry_Branch, Pune_Branch, Raipur_Branch, Rajkot_Branch, Ranchi_Branch, Rishikesh_Branch, Rourkela_Branch, Salem_Branch, Sambalpur_Branch, Shillong_Branch, Shimla_Branch, Silchar_Branch, Siliguri_Branch, Silvassa_Branch, South_Delhi_Branch, Surat_Branch, Tawang_Branch, Thiruvananthapuram_Branch, Thoubal_Branch, Tirupati_Branch, Trichur_Branch, Trichy_Branch, Tura_Branch, Udaipur_Branch, Ujjain_Branch, Vadodara_Branch, Varanasi_Branch, Vasco_da_Gama_Branch, Vijayawada_Branch, Visakhapatnam_Branch, Warangal_Branch, West_Delhi_Branch, Wokha_Branch, Yanam_Branch, Ziro_Branch, ATM_Booth_Kiosk, Bank_Branch, Banking_Chatbot, Biometric_Scanner, Debit_Credit_Card, Desktop_Laptop, Mobile_Device, POS_Mobile_App, POS_Mobile_Device, POS_Terminal, Payment_Gateway_Device, QR_Code_Scanner, Self_service_Banking_Machine, Smart_Card, Tablet, Virtual_Card, Voice_Assistant, Wearable_Device, Web_Browser, Agra, Ahmedabad, Aizawl, Ajmer, Ambala, Ambassa, Amritsar, Asansol, Aurangabad, Bangalore, Belgaum, Berhampur, Bhagalpur, Bhavnagar, Bhopal, Bhubaneswar, Bilaspur, Bokaro, Car_Nicobar, Champhai, Chennai, Churachandpur, Coimbatore, Cuttack, Daman, Dehradun, Dhanbad, Dharmanagar, Dibrugarh, Diglipur, Dimapur, Diu, Durg, Durgapur, East_Delhi, Faridabad, Gangtok, Gaya, Guntur, Gurugram, Guwahati, Gwalior, Haldwani, Haridwar, Hazaribagh, Hisar, Howrah, Hubli, Hyderabad, Imphal, Indore, Itanagar, Jabalpur, Jagdalpur, Jaipur, Jalandhar, Jamshedpur, Jodhpur, Jorethang, Jorhat, Jowai, Kangpokpi, Kangra, Kanpur, Karaikal, Karimnagar, Kavaratti, Khammam, Kochi, Kohima, Kolasib, Kolkata, Korba, Kota, Kottayam, Kozhikode, Kullu, Lucknow, Ludhiana, Lunglei, Madurai, Mahe, Manali, Mangalore, Mangan, Mapusa, Margao, Meerut, Mokokchung, Mumbai, Munger, Muzaffarpur, Mysore, Nagaon, Nagpur, Naharlagun, Nainital, Namchi, Nashik, Nellore, New_Delhi, Nizamabad, Nongstoin, North_Delhi, Panaji, Patiala, Patna, Port_Blair, Pune, Raipur, Rajkot, Ranchi, Rishikesh, Rourkela, Salem, Sambalpur, Shillong, Shimla, Silchar, Siliguri, Silvassa, South_Delhi, Surat, Tawang, Thiruvananthapuram, Thoubal, Tirupati, Trichur, Trichy, Tura, Udaipur, Ujjain, Vadodara, Varanasi, Vasco_da_Gama, Vijayawada, Visakhapatnam, Warangal, West_Delhi, Wokha, Yanam, Ziro, Airline_ticket, Apparel_purchase, Bank_fee, Bank_transfer, Beauty_products, Bike_rental, Bill_payment, Birthday_present, Bitcoin_transaction, Bookstore_purchase, Bus_fare, Business_expense, Cafe_purchase, Camping_gear_purchase, Camping_trip, Car_rental, Car_repair_service, Car_service, Cash_deposit, Charity_contribution, Charity_donation, Childcare_expense, Childrens_clothing, Childrens_toys, Christmas_shopping, Clinic_payment, Clothing_purchase, Conference_fee, Consulting_fee, Contract_renewal, Corporate_event_ticket, Courier_charges, Credit_card_payment, Crowdfunding_contribution, Cryptocurrency_purchase, Customer_service_charge, Debt_repayment, Department_store_shopping, Digital_media_purchase, Dinner_payment, Doctor_consultation, Document_notarization, E_commerce_refund, Electronic_gadget_repair, Electronics_purchase, Electronics_rental, Event_ticket_purchase, Fine_payment, Fitness_membership, Flight_booking, Food_delivery, Food_subscription, Freelancer_payment, Freight_charges, Fuel_purchase, Fund_transfer, Furniture_purchase, Gift_card_purchase, Gift_for_colleague, Gift_for_friend, Gift_for_partner, Gifts_and_souvenirs, Gifts_for_family, Gifts_for_parents, Grocery_delivery, Grocery_shopping, Gym_membership, Health_insurance_payment, Healthcare_premium, Hiring_fee, Home_appliance_repair, Home_cleaning_services, Home_decor, Home_renovation, Home_repairs, Hospital_bill, Hotel_booking, Hotel_reservation, Import_duty_payment, Installment_payment, Insurance_claim, Insurance_premium, Investment_in_gold, Jewelry_purchase, Laundry_service, Legal_services_payment, Loan_payment, Loan_repayment, Long_distance_transport, Loyalty_points_redemption, Lunch_payment, Luxury_item_purchase, Meal_plan, Medical_treatment_payment, Membership_subscription, Mobile_phone_payment, Mobile_recharge, Monthly_installment, Movie_tickets, Moving_services_payment, Music_concert_tickets, Mutual_fund_investment, New_year_shopping, Online_book_purchase, Online_clothing_store, Online_course_payment, Online_education, Online_fitness_class, Online_gaming,blob1,blob2,blob3,blob4,blob5, Online_shopping, Online_software_purchase, Online_subscription, Online_workshop, POS_transaction, Parking_charges, Penalty_fee, Personal_finance_consulting, Personal_loan_repayment, Pet_care, Petroleum_purchase, Pharmacy_bill, Pharmacy_purchase, Phone_accessories, Political_donation, Property_tax_payment, Public_transport_pass, Real_estate_payment, Restaurant_dining, Ridesharing_service, School_fee_payment, Seminar_registration, Senior_citizen_care, Shopping_mall_purchase, Smart_home_device_purchase, Spa_treatment, Specialty_store_shopping, Sports_equipment, Sports_equipment_purchase, Sports_ticket, Stock_investment, Streaming_service, Streaming_service_subscription, Streaming_subscription, Student_loan_repayment, Subscription_box, Subscription_fee, Subscription_payment, Subscription_renewal, Subscription_service, Tax_payment, Taxi_booking, Taxi_fare, Team_lunch, Tech_gadgets_purchase, Ticket_booking, Tourist_attraction_payment, Training_course_fee, Transfer, Transportation_fare, Travel_agency_payment, Travel_expenses, Travel_insurance, Tuition_fee_payment, Utility_bill_payment, Utility_service, Vacation_payment, Vehicle_insurance, Wedding_anniversary_gift, Wedding_gift, Wedding_shopping, Withdrawal, Agra, Ahmedabad, Aizawl, Ajmer, Ambala, Ambassa, Amritsar, Asansol, Aurangabad, Bangalore, Belgaum, Berhampur, Bhagalpur, Bhavnagar, Bhopal, Bhubaneswar, Bilaspur, Bokaro, Car_Nicobar, Champhai, Chennai, Churachandpur, Coimbatore, Cuttack, Daman, Dehradun, Dhanbad, Dharmanagar, Dibrugarh, Diglipur, Dimapur, Diu, Durg, Durgapur, East_Delhi, Faridabad, Gangtok, Gaya, Guntur, Gurugram, Guwahati, Gwalior, Haldwani, Haridwar, Hazaribagh, Hisar, Howrah, Hubli, Hyderabad, Imphal, Indore, Itanagar, Jabalpur, Jagdalpur, Jaipur, Jalandhar, Jamshedpur, Jodhpur, Jorethang, Jorhat, Jowai, Kangpokpi, Kangra, Kanpur, Karaikal, Karimnagar, Kavaratti, Khammam, Kochi, Kohima, Kolasib, Kolkata, Korba, Kota, Kottayam, Kozhikode, Kullu, Lucknow, Ludhiana, Lunglei, Madurai, Mahe, Manali, Mangalore, Mangan, Mapusa, Margao, Meerut, Mokokchung, Mumbai, Munger, Muzaffarpur, Mysore, Nagaon, Nagpur, Naharlagun, Nainital, Namchi, Nashik, Nellore, New_Delhi, Nizamabad, Nongstoin, North_Delhi, Panaji, Patiala, Patna, Port_Blair, Pune, Raipur, Rajkot, Ranchi, Rishikesh, Rourkela, Salem, Sambalpur, Shillong, Shimla, Silchar, Siliguri, Silvassa, South_Delhi, Surat, Tawang, Thiruvananthapuram, Thoubal, Tirupati, Trichur, Trichy, Tura, Udaipur, Ujjain, Vadodara, Varanasi, Vasco_da_Gama, Vijayawada, Visakhapatnam, Warangal, West_Delhi, Wokha, Yanam, Ziro, gender_encoded, transaction_day, transaction_month, transaction_year, transaction_hour, transaction_minute, transaction_second]])




if st.button("Predict"):
    proba = model.predict_proba(input_data)
    label = (proba[:, 1] >= 0.45).astype(int)
    predicted_class = {0: "Not Fraud", 1: "Fraud"}[label[0]]

    st.write(f"Status of the transaction: **{predicted_class}**")