import requests
import streamlit as st


def pretty(label: str) -> str:
    return label.replace("_", " ").title()


def number_input_hidden(label, **kwargs):
    st.caption(pretty(label))
    return st.number_input(label, label_visibility="collapsed", **kwargs)


def selectbox_hidden(label, options, index=0):
    st.caption(pretty(label))
    return st.selectbox(label, options, index=index, label_visibility="collapsed")


st.title("Gym Exercise Calories Burned Prediction App")

with st.form("prediction_form"):
    age = number_input_hidden("age", min_value=18, max_value=65, value=30, step=1)
    gender = selectbox_hidden("gender", ["Male", "Female"], index=0)
    weight_kg = number_input_hidden("weight_kg", min_value=30.0, value=70.0, step=0.1)
    height_m = number_input_hidden("height_m", min_value=1.2, value=1.70, step=0.01)
    max_bpm = number_input_hidden("max_bpm", min_value=60, value=190, step=1)
    avg_bpm = number_input_hidden("avg_bpm", min_value=40, value=140, step=1)
    resting_bpm = number_input_hidden("resting_bpm", min_value=30, value=60, step=1)
    session_duration_hours = number_input_hidden(
        "session_duration_hours", min_value=0.1, value=1.0, step=0.1
    )
    workout_type = selectbox_hidden(
        "workout_type", ["Cardio", "Strength", "HIIT", "Yoga"], index=0
    )
    fat_percentage = number_input_hidden(
        "fat_percentage", min_value=1.0, value=20.0, step=0.1
    )
    water_intake_liters = number_input_hidden(
        "water_intake_liters", min_value=0.1, value=2.5, step=0.1
    )
    workout_frequency_days_per_week = number_input_hidden(
        "workout_frequency_days_per_week", min_value=0, max_value=7, value=4, step=1
    )
    experience_level = number_input_hidden(
        "experience_level", min_value=1, max_value=5, value=3, step=1
    )
    bmi = number_input_hidden("bmi", min_value=10.0, value=24.0, step=0.1)
    submitted = st.form_submit_button("Submit")

if submitted:
    try:
        feature_dict = {
            "age": age,
            "gender": gender,
            "weight_kg": weight_kg,
            "height_m": height_m,
            "max_bpm": max_bpm,
            "avg_bpm": avg_bpm,
            "resting_bpm": resting_bpm,
            "session_duration_hours": session_duration_hours,
            "workout_type": workout_type,
            "fat_percentage": fat_percentage,
            "water_intake_liters": water_intake_liters,
            "workout_frequency_days_per_week": workout_frequency_days_per_week,
            "experience_level": experience_level,
            "bmi": bmi,
        }

        url = "http://127.0.0.1:8000/predict"
        response = requests.post(url=url, json=feature_dict, timeout=30)

        if response.status_code != 200:
            st.error(f"API Error: {response.status_code} - {response.text}")
        else:
            output_dict = response.json()
            predicted_calories = output_dict.get("prediction")
            message = (
                f"Based on the information provided, the predicted calories burned "
                f"for this session is {predicted_calories:.2f}."
            )

            if predicted_calories < 300:
                st.info(f"{message} This looks like a light workout session.")
            elif predicted_calories < 600:
                st.success(f"{message} This looks like a moderate workout session.")
            elif predicted_calories < 900:
                st.success(f"{message} This looks like a high-effort workout session.")
            else:
                st.success(f"{message} This looks like a very intense workout session.")

    except Exception as e:
        st.error(f"Request failed: {e}")
