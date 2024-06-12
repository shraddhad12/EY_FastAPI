# Setup Virtual Environment
python -m venv env

# Activate env
source env/Scripts/activate

# use below command to run the packages
pip install -r requirements.txt

# Switch to the project directory 
cd /EY_FastAPI/FastAPI_project/

# To run the application run the below command
python -m app.app
OR
uvicorn app.app:app --reload
