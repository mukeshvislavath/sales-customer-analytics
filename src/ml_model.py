import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,confusion_matrix
)

# --------------------------------
# 1. Load dataset
# --------------------------------

df = pd.read_csv("data/sales_data.csv")

print("Dataset loaded successfully.")
print("Dataset shape:", df.shape)


# --------------------------------
# 2. Create target variable
# --------------------------------

df["Profitable"] = (df["Profit"] > 0).astype(int)

print("\nTarget distribution:")
print(df["Profitable"].value_counts())


# --------------------------------
# 3. Select features
# --------------------------------

features = [
    "Sales",
    "Quantity",
    "Discount",
    "Category",
    "Segment",
    "Region",
    "Ship Mode"
]

X = df[features]
y = df["Profitable"]


# --------------------------------
# 4. Identify feature types
# --------------------------------

numeric_features = [
    "Sales",
    "Quantity",
    "Discount"
]

categorical_features = [
    "Category",
    "Segment",
    "Region",
    "Ship Mode"
]


# --------------------------------
# 5. Train/Test Split
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# --------------------------------
# 6. Preprocessing
# --------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# --------------------------------
# 7. Create ML Pipeline
# --------------------------------

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000))
    ]
)


# --------------------------------
# 8. Train the model
# --------------------------------

model.fit(X_train, y_train)

print("\nModel trained successfully.")

# --------------------------------
# 9. Make predictions
# --------------------------------

y_pred = model.predict(X_test)

print("\nPredictions generated successfully.")

# --------------------------------
# 10. Evaluate the model
# --------------------------------

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\nModel Performance:")
print("Accuracy :", round(accuracy, 4))
print("Precision:", round(precision, 4))
print("Recall   :", round(recall, 4))
print("F1 Score :", round(f1, 4))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# --------------------------------
# 11. Confusion Matrix
# --------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# --------------------------------
# 12. Random Forest Model
# --------------------------------

rf_model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(
            n_estimators=200,
            random_state=42,
            class_weight="balanced"
        ))
    ]
)

# Train Random Forest
rf_model.fit(X_train, y_train)

print("\nRandom Forest model trained successfully.")


# --------------------------------
# 13. Random Forest Predictions
# --------------------------------

rf_pred = rf_model.predict(X_test)


# --------------------------------
# 14. Random Forest Evaluation
# --------------------------------

rf_accuracy = accuracy_score(y_test, rf_pred)
rf_precision = precision_score(y_test, rf_pred)
rf_recall = recall_score(y_test, rf_pred)
rf_f1 = f1_score(y_test, rf_pred)

print("\nRandom Forest Performance:")
print("Accuracy :", round(rf_accuracy, 4))
print("Precision:", round(rf_precision, 4))
print("Recall   :", round(rf_recall, 4))
print("F1 Score :", round(rf_f1, 4))
# --------------------------------
# 15. Save Final Model
# --------------------------------

joblib.dump(model, "data/profitability_model.pkl")

print("\nFinal model saved successfully.")