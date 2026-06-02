import mysql.connector
import pandas as pd
import joblib
import os
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

load_dotenv()

# 1. Connect to the MySQL Server 
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password= os.getenv("DB_PASSWORD"), # <--- Type your unlocked password here
    database='ticket_system'
)

print("Successfully connected to MySQL database!")

# 2. Test reading the table with Pandas
try:
    df = pd.read_sql_query("SELECT * FROM customer_tickets", conn)
    print("\n--- Current Data inside MySQL ---")
    print(df["department"].value_counts())
    print(df["priority"].value_counts())

    X = df["ticket_text"]
    y_dept = df["department"]
    y_priority = df["priority"]

    dept_pipeline = Pipeline([("Vectorizer" , TfidfVectorizer(ngram_range=(1 , 3) , stop_words="english")) , ("Classifier" , LogisticRegression(class_weight="balanced"))])
    dept_pipeline.fit(X , y_dept)

    priority_pipeline = Pipeline([("Vectorizer" , TfidfVectorizer(ngram_range=(1 , 3) , stop_words="english")) , ("Classifier" , LogisticRegression(class_weight="balanced"))])
    priority_pipeline.fit(X , y_priority)


    joblib.dump(dept_pipeline, "backend/app/artifacts/department_model.pkl")
    joblib.dump(priority_pipeline , "backend/app/artifacts/priority_model.pkl")
    print(df)
except Exception as e:
    print(f"\nConnection worked, but couldn't read table: {e}")
