# FastAPI Handling Errors

A Python project demonstrating how to handle errors and exceptions in **FastAPI** applications. This project showcases various methods for managing error responses, including custom error handling, global exception handling, and detailed error messages for better debugging and user feedback.

## Features

- **Global Exception Handling**: Catches all unhandled exceptions globally and provides custom error responses.
- **Custom Error Messages**: Allows you to create meaningful, user-friendly error messages for different exceptions.
- **Validation Errors**: Handles validation errors in the incoming request data.
- **Custom HTTPException Handling**: Demonstrates the use of custom HTTP exceptions to control specific error responses.
- **Logging Errors**: Logs error details for troubleshooting and auditing purposes.

## Requirements

- **Python 3.x**
- **FastAPI**
- **Uvicorn** (for running the FastAPI application)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/Fast_api_handeling_error.git
    cd Fast_api_handeling_error
    ```

2. **Install Dependencies:**

    If you're using `pip`, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:

    To run the FastAPI app:

    ```bash
    uvicorn main:app --reload
    ```

### How to Use

1. **Global Exception Handling**:
   - Any unhandled exceptions can be caught globally using FastAPI's exception handler.
   - You can customize the response for specific exceptions to provide clearer feedback to the client.

2. **Custom Error Responses**:
   - Create custom error classes using FastAPI's `HTTPException` for better control over error codes and messages.
   - Define specific error messages for different scenarios, like database failures or invalid inputs.

3. **Validation Errors**:
   - FastAPI automatically handles validation errors and returns a structured response with details about the validation failure.
   - You can customize how validation errors are presented to the user.

4. **Logging Errors**:
   - Use logging to record error details, which can be helpful for debugging and monitoring.

### Example Usage

1. **Custom Error Handling**:
   - When a request triggers an error (e.g., invalid input), the system catches it and returns a structured error message, including an error code and a description.

2. **Validation Errors**:
   - When invalid data is passed in a request (like missing required fields), FastAPI automatically responds with validation error details.

3. **Global Exception Handling**:
   - Unhandled exceptions will trigger a global error handler, ensuring the application always returns a predictable and controlled response.

### Project Structure

- `main.py`: Contains the FastAPI application, routes, and error-handling logic.
- `requirements.txt`: Lists necessary libraries like `FastAPI`, `Uvicorn`, etc.
- `error_handling.py`: Contains custom error handling logic and exception classes for the project.

## Contributing

Feel free to fork the project and submit pull requests for new features, improvements, or bug fixes.

## License

This project is open-source and available for educational purposes.
![Alt](https://repobeats.axiom.co/api/embed/eabe6508a91fa38b4ace0060919094363916f544.svg "Repobeats analytics image")
