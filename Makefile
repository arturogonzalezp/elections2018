include .env
default:
	@make setup
	@make run
setup:
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
test:
	@echo "Tests"
.PHONY: default