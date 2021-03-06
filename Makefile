clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build


format:
	black -l 88 **/*.py

install:
	pip3 install git+https://github.com/WesleySteve/bancoslib.git && \
	pip3 install -r requirements.txt


up:
	docker-compose up -d

down:
	docker-compose stop
	
	
