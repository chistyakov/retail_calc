.PHONY : calc tests format static_check build_prod build_dev

calc : build_prod
	docker run --rm --name retail_calc_calc retail_calc_prod calc

tests : build_dev
	docker run --rm --name retail_calc_test retail_calc_dev tests

format : build_dev
	docker run --rm --name retail_calc_format -v ${PWD}:/app -u $$(id -u) retail_calc_dev format

static_check : build_dev
	docker run --rm --name retail_calc_format retail_calc_dev static_check

build_prod:
	docker build  --target prod --tag retail_calc_prod .

build_dev:
	docker build  --target dev --tag retail_calc_dev .
