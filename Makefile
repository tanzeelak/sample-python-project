install:
	pip3 install -r requirements.txt

run:
	python3 -m src.baddie

test:
	pytest && rm -rf .pytest_cache