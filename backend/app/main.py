import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class TicketRequest(BaseModel):
    ticket_text:str

@app.post("/predict")
def predict_ticket(request : TicketRequest):
    raw_text = [request.ticket_text]
    predicted_dept = dept_model.predict(raw_text)[0]
    predicted_priority = priority_model.predict(raw_text)[0]
    return{
        "department" : predicted_dept,
        "priority" : predicted_priority
    }



try : 
    dept_model = joblib.load("backend/app/artifacts/department_model.pkl")
    priority_model = joblib.load("backend/app/artifacts/priority_model.pkl")
    print("Model load Successfuly !!")


except Exception as e :
    print(f"Error loading model{e}")
