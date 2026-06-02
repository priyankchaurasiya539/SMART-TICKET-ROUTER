Smart Ticket Router System
About the Project : My project Smart Ticket Router System is useful for production line system . It does classify the problems of user what they are in facing . My model recevies the user problem and then it specifies its department ( may be it from technical ,billing , accounting , refund , web team , delivery etc ) and its priority ( may be low , medium , high and urgent.)

##Tech Stack

Machine Learning : Scikit-Learn(Logistic Regression , TF-IDF Vectorizer with n_grams and balanced class weight)
Backend : FastAPI , Uvicorn , Pydantic , Joblib
Frontend : Streamlit , Requests
Database : MySQL
Project Structure
smart-ticket-router/ ├── ML_pipeline/ # Model training scripts & data telemetry ├── backend/ # FastAPI engine & production artifacts (.pkl) ├── frontend/ # Streamlit web interface portal └── ticket_system.db # Storage ledger

How to run :
Backend Command Block : 'uvicorn backend.app.main:app --reload'
Frontend Command Block : 'streamlit run frontend/app.py'
