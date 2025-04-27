from typing import Union  # Import for type annotations.

from fastapi import FastAPI  # Import FastAPI framework.

from api.user.router import router as UserRoutes  # Import user-related routes.

# Initialize the FastAPI application.
app = FastAPI()

# Define the root endpoint.
@app.get("/")
def read_root():
    """
    Root endpoint of the application.
    Returns:
        dict: A simple JSON response with a greeting message.
    """
    return {"Hello": "World"}

# Include user-related routes under the "/guardian" prefix.
app.include_router(UserRoutes, prefix="/guardian")


