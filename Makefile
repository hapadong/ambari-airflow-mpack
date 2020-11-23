all: clean
	tar czvf airflow-service-mpack-$(shell git describe --tags).tar.gz airflow-service-mpack
clean:
	rm -f *.tar.gz
