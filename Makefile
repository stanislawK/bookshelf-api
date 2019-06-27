tests:	## Start tests with pytest and flake8
				docker-compose run --rm api sh -c "pytest && flake8"
