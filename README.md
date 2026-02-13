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
5. Enable debug request body logging:
   - `SIMPLEADDER_DEBUG_BODY=1 python -m simpleadder.main`

# Makefile targets
- `make all` runs `build`, `install`, then `run`
- `make build` builds the package with `uv build`
- `make install` installs the package in editable mode
- `make run` starts the service via the `simpleadder` script
- `make curltest` sends a test request to `/add`
- `make browserdocs` opens the Swagger UI in a browser


