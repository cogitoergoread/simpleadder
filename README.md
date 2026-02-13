# Simple adder web service

# Objective

- OpenAPI 3.0 IF description for the service
- The service has one operation that returns the sum of two numbers
- The service is implemented in Python using Flask
- The service has a Swagger style UI for testing the operation

# OpenAPI 3.0 IF description

# OpenAPI 3.0

IF description in [adder.yaml](adder.yaml) file.

# Run
1. Install dependencies:
   - `pip install -e .`
2. Start the service:
   - `python -m simpleadder.main`
3. Open Swagger UI:
   - http://localhost:5000/docs
4. Test with curl:
   - `curl -s -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{"number1": 2, "number2": 2}'`


