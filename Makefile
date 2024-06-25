install:
	pip3 install -r requirements.txt

run-baddie:
	python3 -m src.baddie

run-life:
	python3 -m src.life

test:
	pytest && rm -rf .pytest_cache