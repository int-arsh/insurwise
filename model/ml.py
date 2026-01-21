import pickle

import pandas as pd

# import the ml model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

# get class labels from model (fro matching probabilities to class name)
class_labels = model.classes_.tolist()
# print(class_labels)


def predict_category(data):
    input_df = pd.DataFrame(
        [
            {
                "bmi": data.bmi,
                "age_group": data.age_group,
                "lifestyle_risk": data.lifestyle_risk,
                "city_tier": data.city_tier,
                "income_lpa": data.income_lpa,
                "occupation": data.occupation,
            }
        ]
    )

    # Predict the class
    predicted_class = model.predict(input_df)[0]

    # get probabilities for all classes
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    # create mapping: {class_name : proobability}
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs,
    }
