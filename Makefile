include .env
default:
	@make clean
	@make setup
	@make tests
	@make run
setup:
	@make clean
	@sed 's/=s.*//' .env | while read x ; do eval $$x ; done
	@python setup.py
	@make clean
install:
	@sudo easy_install pip
	@sudo pip install --ignore-installed -r requirements.txt
	@touch playground.py
	@touch .env
	@touch elections/utils/users.txt
	@touch elections/utils/candidates.txt
	@touch elections/storage/local_storage.json
	@make setup
run:
	@make tests
	@python app.py ${candidate}
playground:
	@make tests
	@python playground.py
analyze:
	@make tests
	@python analyze.py
word-cloud:
	@make tests
	@python word_cloud.py
clean:
	@find . -name \*.pyc -delete
	@clear
tests:
	@python test/test_calc.py
	@echo '----------------------------------------------------------------------'
.PHONY: default