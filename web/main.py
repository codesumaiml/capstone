from pathlib import Path

import pandas as pd
import pickle
from fastapi import FastAPI
from pydantic import BaseModel


MODEL_PATH = Path(__file__).with_name("GradientBoosting_spf_20260325_064019UTC.pkl")

with MODEL_PATH.open("rb") as model_file:
    model = pickle.load(model_file)


class independentFeatures(BaseModel):
    age: int
    gender: str
    weight_kg: float
    height_m: float
    max_bpm: int
    avg_bpm: int
    resting_bpm: int
    session_duration_hours: float
    workout_type: str
    fat_percentage: float
    water_intake_liters: float
    workout_frequency_days_per_week: int
    experience_level: int
    bmi: float


app = FastAPI()


def build_feature_frame(features: independentFeatures) -> pd.DataFrame:
    age_group = pd.cut(
        pd.Series([features.age]),
        bins=[18, 25, 35, 45, 55, 65],
        labels=["18-25", "26-35", "36-45", "46-55", "56-65"],
        include_lowest=True,
    ).iloc[0]

    bpm_duration_index = features.avg_bpm * features.session_duration_hours
    intensity = features.avg_bpm / features.session_duration_hours

    return pd.DataFrame(
        [
            {
                "Age": features.age,
                "Gender": features.gender,
                "Weight (kg)": features.weight_kg,
                "Height (m)": features.height_m,
                "Max_BPM": features.max_bpm,
                "Avg_BPM": features.avg_bpm,
                "Resting_BPM": features.resting_bpm,
                "Session_Duration (hours)": features.session_duration_hours,
                "Workout_Type": features.workout_type,
                "Fat_Percentage": features.fat_percentage,
                "Water_Intake (liters)": features.water_intake_liters,
                "Workout_Frequency (days/week)": features.workout_frequency_days_per_week,
                "Experience_Level": features.experience_level,
                "BMI": features.bmi,
                "Age_Group": age_group,
                "BPM_Duration_Index": bpm_duration_index,
                "Intensity": intensity,
            }
        ]
    )


@app.get("/")
def hello() -> str:
    return "Hello from Gym Exercise Prediction Portal"


@app.post("/predict")
def predict_calories_burned(variables: independentFeatures) -> dict[str, float]:
    data = build_feature_frame(variables)
    prediction = model.predict(data)
    return {"prediction": float(prediction.item())}
