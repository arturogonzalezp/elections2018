include .env
default:
	@make clean
	@make setup
	@make tests
	@make run
setup:
	@make clean
	@sed 's/=s.*//' .env | while read x ; do eval $$x ; done
install:
	@sudo easy_install pip
	@sudo pip install --ignore-installed -r requirements.txt
	@touch playground.py
	@touch .env
	@touch elections/utils/users.txt
	@touch elections/storage/local_storage.json
	@make setup
run:
	@make tests
	@python app.py
playground:
	@make tests
	@python playground.py
analyze:
	@make tests
	@python analyze.py
clean:
	@find . -name \*.pyc -delete
	@clear
tests:
	@python test/test_calc.py
.PHONY: default