# install libraries cmd
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# install requirments.txt
freeze:
	pip freeze > requirements.txt

# run API server
server:
	uvicorn main:app --reload

# format code
format:
	black *.py
lint:
	pylint --disable=R,C file.py
test:
	#test
	python main.py
deploy:
	#deploy
all:
	install lint test deploy
