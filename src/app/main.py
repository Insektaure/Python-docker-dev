from src.config.settings import APP_NAME
from src.app.api import app

def main():
    import uvicorn
    print(f"Welcome to {APP_NAME}")
    uvicorn.run(app, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()