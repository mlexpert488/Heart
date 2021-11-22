import numpy as np
import joblib
import pickle


def load_pkl(fname):
    with open(fname, "rb") as f:
        obj = pickle.load(f)
    return obj


def preprocessdata(
    age,
    anaemia,
    creatinine_phosphokinase,
    diabetes,
    ejection_fraction,
    high_blood_pressure,
    platelets,
    serum_creatinine,
    serum_sodium,
    sex,
    smoking,
    time,
):
    test_data = [
        [
            age,
            anaemia,
            creatinine_phosphokinase,
            diabetes,
            ejection_fraction,
            high_blood_pressure,
            platelets,
            serum_creatinine,
            serum_sodium,
            sex,
            smoking,
            time,
        ]
    ]

    trained_model = joblib.load(r"modelrandomforest.pkl")
    print(test_data)
    prediction = trained_model.predict(test_data)

    return prediction


# prediction = preprocessdata(40.000, 1, 101, 0, 40, 0, 226000.0, 0.8, 141, 0, 0, 187)
# print(prediction)

