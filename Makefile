all: build install run

build: src/simpleadder/main.py
	uv build

install:
	uv pip  install -e .

run:
	simpleadder simpleadder.main:app --host 0.0.0.0 --port 5000

curltest:
	curl -s -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{"number1": 2, "number2": 2}'

browserdocs:
	open http://localhost:5000/docs