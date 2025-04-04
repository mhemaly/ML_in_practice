import streamlit as st
from src.utils import predict_survival

def main():
    st.title("Titanic Survival Prediction App")
    st.write("Enter passenger details to predict survival:")

    pclass = st.selectbox("Passenger Class (1st, 2nd, 3rd):", [1, 2, 3])
    sex = st.radio("Sex:", ["Male", "Female"])
    age = st.slider("Age:", 0, 100, 28)
    sibsp = st.slider("Number of Siblings/Spouses Aboard:", 0, 8, 0)
    parch = st.slider("Number of Parents/Children Aboard:", 0, 6, 0)
    fare = st.number_input("Fare Paid:", 0.0, 512.0, 15.2458)
    alone = st.radio("Alone:", ["Yes", "No"])

    sex = 1 if sex == "Male" else 0
    alone = 1 if alone == "Yes" else 0

    input_data = {'pclass': pclass, 'sex': sex, 'age': age, 'sibsp': sibsp, 'parch': parch, 'fare': fare, 'alone': alone}

    if st.button("Predict Survival"):
        result = predict_survival(input_data)
        if result == "Survived":
            st.success(f"Prediction: {result}", icon="✅")
            st.markdown("<h2 style='color: green;'>Survived ✅</h2>", unsafe_allow_html=True)
        else:
            st.error(f"Prediction: {result}", icon="❌")
            st.markdown("<h2 style='color: red;'>Did Not Survive ❌</h2>", unsafe_allow_html=True)



if __name__ == '__main__':
    import subprocess
    from streamlit import runtime
    if runtime.exists():
        main()
    else:
        process = subprocess.Popen(["streamlit", "run", "./main.py"])