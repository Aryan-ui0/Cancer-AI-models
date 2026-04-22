import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

def train_model(csv_file, model_name):
    print(f"\nTraining {model_name}...")

    # Load dataset
    data = pd.read_csv(csv_file)

    # Split features and target
    X = data.drop("target", axis=1)
    y = data["target"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create model
    model = LogisticRegression(max_iter=1000)

    # Train model
    model.fit(X_train, y_train)

    # Evaluate
    accuracy = model.score(X_test, y_test)
    print(f"{model_name} Accuracy: {round(accuracy * 100, 2)}%")

    # Save model
    joblib.dump(model, model_name)
    print(f"{model_name} saved!")

# Train all datasets
#train_model("lung.csv", "lung_model.pkl")
#train_model("liver.csv", "liver_model.pkl")
train_model("kidney.csv", "kidney_model.pkl")
#train_model("skin.csv", "skin_model.pkl")

print("\n✅ All models trained successfully!")