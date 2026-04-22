import csv
import random

def generate_row():
    age = random.randint(20, 80)
    bp = random.randint(90, 180)
    albumin = random.randint(0, 5)
    sugar = random.randint(70, 200)
    creatinine = round(random.uniform(0.5, 10.0), 2)
    fatigue = random.randint(0, 1)
    swelling = random.randint(0, 1)

    # 💡 Smart target logic (NOT random)
    risk_score = 0

    if creatinine > 1.5:
        risk_score += 2
    if albumin >= 2:
        risk_score += 2
    if bp > 140:
        risk_score += 1
    if sugar > 140:
        risk_score += 1
    if fatigue == 1:
        risk_score += 1
    if swelling == 1:
        risk_score += 1

    target = 1 if risk_score >= 4 else 0

    return [age, bp, albumin, sugar, creatinine, fatigue, swelling, target]


def generate_dataset(filename="kidney_dataset.csv", rows=200):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Header
        writer.writerow([
            "age", "blood_pressure", "albumin",
            "blood_sugar", "creatinine",
            "fatigue", "swelling", "target"
        ])
        
        for _ in range(rows):
            writer.writerow(generate_row())

    print(f"Dataset with {rows} rows saved as {filename}")


# Run this
generate_dataset(rows=400)