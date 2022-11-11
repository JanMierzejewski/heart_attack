# źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic)

import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model1.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

sex_d = {0:"famale", 1:"male"}
ChestPainType_d = {0:"ASY",1:"ATA", 2:"NAP", 3:"TA"}
RestingECG_d = {0:"LVH", 1:"Normal", 2:"ST"}
ExerciseAngina_d = {0:"N", 1:"Y"}
ST_Slope_d = {0: "Down", 1:"Flat", 2:"Up"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem

def main():

	st.set_page_config(page_title="czy dostaniesz zawału serca")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://wybieram-zdrowie.com/wp-content/uploads/2017/04/004C5550-3C4B-470B-9FDC-226597237DDB.jpeg")

	with overview:
		st.title("czy dostaniesz zawału serca")
		st.subheader("Żyj zdrowo ;)")

	with left:
		sex_radio = st.radio( "Płeć", list(sex_d.keys()), format_func=lambda x : sex_d[x] )
		ChestPainType_radio = st.radio( "Ból w klatce", list(ChestPainType_d.keys()), index=2, format_func= lambda x: ChestPainType_d[x] )
		RestingECG_radio = st.radio("Resting ECG", list(RestingECG_d.keys()), format_func=lambda x : RestingECG_d[x] )
		ST_Slope_radio = st.radio("ST Slope", list(ST_Slope_d.keys()), format_func=lambda x : ST_Slope_d[x] )

	with right:
		age_slider = st.slider("Wiek", value=1, min_value=28, max_value=77)
		RestingBP_slider = st.slider("Ciśnienie spoczykowe", min_value=0, max_value=200, step=1) 
		#tu chyba jest coś nie tak z danymi gdyż jest jedna osoba, która ma RestingBP '0' a następne min value to już '80' - startuje od '0' ale potem nie ma przeskoku do '80' więc coś jest nie tak :(
		Cholesterol_slider = st.slider("Cholesterol", min_value=0, max_value=603) 
		#podobna sytuacja jak wyżej
		FastingBS_slider = st.slider("FastingBS", min_value=0, max_value=1, step=1)
		MaxHR_slider = st.slider("MaxHR", min_value=60, max_value=202, step=1)
		Oldpeak_slider = st.slider("Oldpeak", min_value=-2.0, max_value=6.2, step=0.1) 
		HeartDisease_slider = st.slider("HeartDisease", min_value=0, max_value=1, step=1)


	data = [[age_slider, RestingBP_slider, Cholesterol_slider, FastingBS_slider, MaxHR_slider, Oldpeak_slider, HeartDisease_slider]] 
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.subheader("Czy taka osoba dostanie zawału serca?")
		st.subheader(("Tak" if survival[0] == 1 else "Nie"))
		st.write("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()
