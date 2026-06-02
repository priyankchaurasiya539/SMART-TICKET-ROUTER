import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()
class TicketRequest(BaseModel):
    ticket_text:str

@app.post("/predict")
def predict_ticket(request : TicketRequest):
    raw_text = [request.ticket_text]
    predicted_dept = dept_model.predict(raw_text)[0]
    predicted_priority = priority_model.predict(raw_text)[0]
    conn = sqlite3.connect("ticket_system.db")
    cursor = conn.cursor() 
    cursor.execute("INSERT INTO resolved_tickets (ticket_text, department, priority) VALUES (?, ?, ?)", (request.ticket_text, predicted_dept, predicted_priority))
    conn.commit()
    conn.close()
    return{
        "department" : predicted_dept,
        "priority" : predicted_priority
    }



try : 
    dept_model = joblib.load("backend/app/artifacts/department_model.pkl")
    priority_model = joblib.load("backend/app/artifacts/priority_model.pkl")
    print("Model load Successfuly !!")
    conn = sqlite3.connect("ticket_system.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS resolved_tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    ticket_text TEXT, 
    department TEXT, 
    priority TEXT
)""")
    conn.commit()
    conn.close()


except Exception as e :
    print(f"Error loading model{e}")
