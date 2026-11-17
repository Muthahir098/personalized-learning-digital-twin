import pandas as pd
import numpy as np


np.random.seed(42)

students = 200

data = {
    "student_id": [f"S{i:03d}" for i in range(1, students + 1)],

    "attendance": np.random.randint(50, 100, students),

    "math_score": np.random.randint(30, 100, students),

    "python_score": np.random.randint(30, 100, students),

    "english_score": np.random.randint(30, 100, students),

    "study_hours": np.round(
        np.random.uniform(0.5, 5.0, students), 1
    ),

    "quiz_score": np.random.randint(30, 100, students),

    "assignments_completed": np.random.randint(2, 11, students)
}


df = pd.DataFrame(data)

df.to_csv("data/student_data.csv", index=False)

print("Student dataset created successfully!")
print(df.head())