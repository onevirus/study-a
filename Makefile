all:
	pipenv install
	pipenv run jupyter-book build contents/
	pipenv run ghp-import -n -p -f contents/_build/html
