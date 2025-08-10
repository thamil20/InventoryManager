from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import logging
import uvicorn
from backend.app import config
from backend.app.logging_config import setup_logging
from backend.app.routers import (current_inventory, sold_inventory, incomes, expenses)

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

setup_logging()
logger = logging.getLogger("backend_logger")

app = FastAPI()

app.mount("/images", StaticFiles(directory=config.IMAGE_UPLOAD_DIR), name="images")
app.include_router(current_inventory.router)
app.include_router(sold_inventory.router)
app.include_router(incomes.router)
app.include_router(expenses.router)

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"message": "Inventory backend is running!"}


if __name__ == "__main__":
    main()