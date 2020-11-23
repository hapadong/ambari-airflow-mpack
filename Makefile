all: clean
	tar czvf airflow-service-mpack-1.10.0.tar.gz airflow-service-mpack
clean:
	rm -f *.tar.gz
