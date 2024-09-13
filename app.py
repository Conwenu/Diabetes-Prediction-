import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle as pk

model = pk.load(open("DiabetesPreictionModel.pkl", "rb"))

data = pd.read_csv("new_data.csv")

data_no_target = data.drop(columns='Target', axis=1)
X = data_no_target
y = data["Target"]
X_train, X_test, y_train , y_test = train_test_split(X,y, test_size=0.2, random_state=0)
scaler = StandardScaler()
scaler.fit(X_train)

age_category_mapping = {
    '18-24': 1,
    '25-29': 2,
    '30-34': 3,
    '35-39': 4,
    '40-44': 5,
    '45-49': 6,
    '50-54': 7,
    '55-59': 8,
    '60-64': 9,
    '65-69': 10,
    '70-74': 11,
    '75-79': 12,
    '80 or older': 13
}

education_level_mapping = {
    "Never attended school or only kindergarten": 1,
    "Grades 1 - 8 (Elementary)": 2,
    "Grades 9 - 11 (Some high school)": 3,
    "Grade 12 or GED (High school graduate)": 4,
    "College 1 year to 3 years (Some college or technical school)": 5,
    "College 4 years or more (College graduate)": 6
}

income_range_mapping = {
    "Less than $10K": 1,
    "$10K - $15K": 2,
    "$15K - $20K": 3,
    "$20K - $25K": 4,
    "$25K - $35K": 5,
    "$35K - $50K": 6,
    "$50K - $75K": 7,
    "$75K or more": 8
}

yes_no_mapping = {
    "Yes" : 1,
    "No" : 0
}

gender_mapper = {
    "Female" : 0,
    "Male" : 1
}

diabetes_res_mapper = {
    0 : "No Diabetes",
    1 : "Diabetes"
}

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://64.media.tumblr.com/b8fc09902ac19cea2062ba446312d0c2/dd86d122c788d105-e9/s500x750/88971e6194b3b5c769c0d95d866bf1a82d7eb1be.gif")
    }
   .sidebar .sidebar-content {
        background: url("url_goes_here")
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Diabetes Prediction Application")

st.header("Questions", divider="gray")

st.subheader("What is your name?")
name = st.text_input(" ", label_visibility="collapsed")
if name:
    st.markdown(f"Hello **{name}**!")


st.subheader("What is your gender?")
Gender = st.selectbox(
    " ",
    options=["Female", "Male"],
    label_visibility="collapsed",
    key="Gender"
)

st.subheader("What is your age group?")
Age = st.selectbox(
    " ",
    options=[
        "18-24",
        "25-29",
        "30-34",
        "35-39",
        "40-44",
        "45-49",
        "50-54",
        "55-59",
        "60-64",
        "65-69",
        "70-74",
        "75-79",
        "80 or older"
    ],
    label_visibility="collapsed",
    key="Age"
)

st.subheader("What is your highest level of education?")
Education = st.selectbox(
    " ",
    options=[
        "Never attended school or only kindergarten",
        "Grades 1 - 8 (Elementary)",
        "Grades 9 - 11 (Some high school)",
        "Grade 12 or GED (High school graduate)",
        "College 1 year to 3 years (Some college or technical school)",
        "College 4 years or more (College graduate)"
    ],
    label_visibility="collapsed",
    key="Education"
)

st.subheader("What income range do you fall in?")
Income = st.selectbox(
    " ",
    options=[
        "Less than $10K",
        "$10K - $15K",
        "$15K - $20K",
        "$20K - $25K",
        "$25K - $35K",
        "$35K - $50K",
        "$50K - $75K",
        "$75K or more"
    ],
    label_visibility="collapsed",
    key="Income"
)

st.subheader("What is your BMI?")
BMI = st.number_input(" ", value = 30.0, label_visibility="collapsed", key = "BMI" )

st.subheader("Do you have high blood pressure?")
HighBP = st.radio(" ", ('Yes', 'No'), label_visibility="collapsed", key = "HighBP")

st.subheader("Do you have high cholesterol?")
HighChol = st.radio(" ", ('Yes', 'No'), label_visibility="collapsed", key = "HighChol")

st.subheader("Have you had your cholesterol checked in the last 5 years?")
CholCheckLast5Years = st.radio(" ", ('Yes', 'No'), label_visibility="collapsed", key = "CholCheckLast5Years")

st.subheader("Have you smoked at least 100 cigarettes in your entire life?")
Smoker = st.radio(" ", ('Yes', 'No'), label_visibility="collapsed", key = "Smoker")

st.subheader("Have you ever had a stroke?")
Stroke = st.radio(" ", ('Yes', 'No'), label_visibility="collapsed", key = "Stroke")

st.subheader("Have you ever had coronary heart disease (CHD) or myocardial infarction (MI)?")
HeartDiseaseOrAttack = st.radio(" ", ('Yes', 'No'), label_visibility="collapsed", key = "HeartDiseaseOrAttack")

st.subheader("Have you engaged in any physical activity in past 30 days - not including job?")
PhysActivity = st.radio(" ", ('Yes', 'No'), label_visibility="collapsed", key = "PhysActivity")

st.subheader("Do you consume fruit 1 or more times per day?")
Fruits = st.radio(" ", ('Yes', 'No'), label_visibility="collapsed", key = "Fruits")

st.subheader("Do you consume vegetables 1 or more times per day?")
Veggies = st.radio(" ", ('Yes', 'No'), label_visibility="collapsed", key = "Veggies")

st.subheader("Are you a heavy drinker? (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)")
HvyAlcoholConsump = st.radio(" ", ('Yes', 'No'), label_visibility="collapsed", key = "HvyAlcoholConsump")

st.subheader("Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc?")
AnyHealthcare = st.radio(" ", ('Yes', 'No'), label_visibility="collapsed", key = "AnyHealthcare")

st.subheader("Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?")
NoDocBcCost = st.radio(" ", ('Yes', 'No'), label_visibility="collapsed", key = "NoDocBcCost")

st.subheader("How would you rate your overall health on a scale of 1 to 5, where 1 is excellent, 2 is very good, 3 is good, 4 is fair, and 5 is poor?")
GeneralHealth = st.slider(" ", min_value = 1, max_value = 5, label_visibility="collapsed", key = "GeneralHealth")

st.subheader("In regard to your mental health how many days out of the past 30 did you deal with things such as stress, depression, and problems with emotions, etc?")
MentalHealth = st.slider(" ", min_value = 1, max_value = 30, label_visibility="collapsed", key = "MentalHealth")

st.subheader("How many days out of the past 30 did you deal with with physical illness and  injury?")
PhysicalHealth = st.slider(" ", min_value = 1, max_value = 30, label_visibility="collapsed", key = "PhysicalHealth")

st.subheader("Do you have serious difficulty walking or climbing stairs?")
Difficulty_Walking = st.radio(" ", ('Yes', 'No'), label_visibility="collapsed", key = "Difficulty_Walking")



def predict():
    _BMI = BMI
    _HighBP = yes_no_mapping.get(HighBP)
    _HighChol = yes_no_mapping.get(HighChol)
    _Stroke = yes_no_mapping.get(Stroke)
    _HeartDiseaseOrAttack = yes_no_mapping.get(HeartDiseaseOrAttack)
    _Education = education_level_mapping.get(Education)
    _Income = income_range_mapping.get(Income)
    _AnyHealthcare = yes_no_mapping.get(AnyHealthcare)
    
    HighBP_And_HighChol = _HighBP * _HighChol
    ChronicConditions = _HighBP + _HighChol + _Stroke + _HeartDiseaseOrAttack
    Education_Income = _Education * _Income
    Income_HealthcareAccess = _Income * _AnyHealthcare
    
    DiabetesRiskScore = _HighBP + _HighChol + int(_BMI >= 30)
    
    BMI_Squared = _BMI ** 2
    BMI_Cubed = _BMI ** 3
    
    features = [
        _HighBP,
        _HighChol,
        yes_no_mapping.get(CholCheckLast5Years),
        BMI,
        yes_no_mapping.get(Smoker),
        _Stroke,
        _HeartDiseaseOrAttack,
        yes_no_mapping.get(PhysActivity),
        yes_no_mapping.get(Fruits),
        yes_no_mapping.get(Veggies),
        yes_no_mapping.get(HvyAlcoholConsump),
        _AnyHealthcare,
        yes_no_mapping.get(NoDocBcCost),
        GeneralHealth,
        MentalHealth,
        PhysicalHealth,
        yes_no_mapping.get(Difficulty_Walking),
        gender_mapper.get(Gender),
        age_category_mapping.get(Age),
        _Education,
        _Income,
        HighBP_And_HighChol,
        ChronicConditions,
        BMI_Squared,
        BMI_Cubed,
        DiabetesRiskScore,  
        Education_Income, 
        Income_HealthcareAccess  
    ]
    
    features_2d = np.array(features).reshape(1, -1)
    
    features_scaled = scaler.transform(features_2d)
    
    y_pred = model.predict(features_scaled)
    y_prob = model.predict_proba(features_scaled)
    
    return y_pred[0], y_prob[0]

st.divider()

st.header("Results", divider="gray")

if st.button("Predict", use_container_width = True):
    if not name:
        name = "User"
    res = predict()
    print(res)
    res_diagnosis = diabetes_res_mapper[res[0]]
    res_diagnosis_pct = round(res[1][res[0]], 4) * 100
    res_string = ""
    if res_diagnosis == "Diabetes": 
        res_d = ":red[ may have Diabetes.] 😢"
    else:
        res_d = ":green[ do not have diabetes.] 😀"
    store = f"Ok :blue[{name}], based on our model there is a :orange[{res_diagnosis_pct}%] chance you {res_d}"
    st.markdown(store)


st.divider()

