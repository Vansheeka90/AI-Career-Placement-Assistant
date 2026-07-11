import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv("dataset/student_placement_synthetic.csv")

print("First 5 Rows:")
print(df.head())

# ==========================
# Encode Categorical Column
# ==========================
le = LabelEncoder()
df["branch"] = le.fit_transform(df["branch"])
tier_encoder = LabelEncoder()
df["college_tier"] = tier_encoder.fit_transform(df["college_tier"])

# ==========================
# Features and Target
# ==========================
X = df.drop(["placement_status", "salary_package_lpa"], axis=1)
y = df["placement_status"]

# ==========================
# Train Test Split
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# Train Model
# ==========================
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================
# Prediction
# ==========================
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy : {accuracy*100:.2f}%")

# ==========================
# Save Model
# ==========================
joblib.dump(model, "model/placement_model.pkl")
joblib.dump(le, "model/label_encoder.pkl")
joblib.dump(tier_encoder, "model/tier_encoder.pkl")

print("Model Saved Successfully!")