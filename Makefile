.PHONY : build tests generate analyze

generate : build
	docker run --rm --name xml_zipper -v ${PWD}/data:/data -u $$(id -u) xml_zipper generate

analyze : build
	docker run --rm --name xml_zipper -v ${PWD}/data:/data -u $$(id -u) xml_zipper analyze

tests : build
	docker run --rm --name xml_zipper xml_zipper tests

build :
	docker build . -t xml_zipper
