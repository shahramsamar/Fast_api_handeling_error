# setup fastapi 
pip install "fastapi[standard]"

# how to run multi choose
1:
 uvicorn main:app --reload
2:
fastapi dev main.py


3:
import uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", port =8000, log_level="info")
    
    