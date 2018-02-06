include .env
default:
	@make clean
	@make setup
	@make run
setup:
	@make clean
	@sed 's/=s.*//' .env | while read x ; do eval $$x ; done
install:
	@sudo easy_install pip
	@sudo pip install --ignore-installed -r requirements.txt
	@touch playground.py
	@touch .env
	@make setup
run:
	@python app.py
playground:
	@python playground.py
clean:
	@find . -name \*.pyc -delete
	@clear
test:
	@echo "Tests"
.PHONY: default