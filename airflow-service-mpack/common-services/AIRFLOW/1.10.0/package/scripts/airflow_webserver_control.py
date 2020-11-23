import sys, os, pwd, grp, signal, time
from resource_management import *
from subprocess import call
from airflow_setup import *

class AirflowWebserver(Script):
	"""
	Contains the interface definitions for methods like install, 
	start, stop, status, etc. for the Airflow Server
	"""
	def install(self, env):
		import params
		env.set_params(params)
		self.install_packages(env)
		Logger.info(format("Installing Airflow Service"))
		Execute(format("{conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} pip"))
		Execute(format("{conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} setuptools"))
		Execute(format("{conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} docutils pytest-runner Cython==0.28"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[all_dbs]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[async]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[celery]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[cloudant]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[crypto]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[devel]==1.10.0"))
		#Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[devel_hadoop]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[druid]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[hashicorp]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[hdfs]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[jdbc]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[hive]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[kubernetes]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[ldap]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[oracle]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[mysql]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[mssql]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[postgres]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[password]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[presto]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[qds]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[rabbitmq]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[redis]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[samba]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[slack]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[ssh]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed apache-airflow[vertica]==1.10.0"))
		Execute(format("export SLUGIFY_USES_TEXT_UNIDECODE=yes && {conda_root}/envs/{conda_airflow_virtualenv}/bin/pip install --upgrade {airflow_pip_params} --ignore-installed marshmallow-sqlalchemy==0.18.0"))
		Execute(format("chmod 755 /bin/airflow /usr/bin/airflow"))
		Execute(format("useradd {airflow_user}"), ignore_failures=True)
		Execute(format("mkdir -p {airflow_home}"))
		airflow_make_startup_script(env)
		Execute(format("chown -R {airflow_user}:{airflow_group} {airflow_home}"))
		Execute(format("export AIRFLOW_HOME={airflow_home} && {conda_root}/envs/airflow/bin/airflow initdb"),
			user=params.airflow_user
		)

	def configure(self, env):
		import params
		env.set_params(params)
		airflow_configure(env)
		airflow_make_systemd_scripts_webserver(env)
		
	def start(self, env):
		import params
		self.configure(env)
		Execute("service airflow-webserver start")
		Execute('ps -ef | grep "airflow webserver" | grep -v grep | awk \'{print $2}\' | tail -n 1 > ' + params.airflow_webserver_pid_file,
			user=params.airflow_user
		)

	def stop(self, env):
		import params
		env.set_params(params)
		# Kill the process of Airflow
		Execute("service airflow-webserver stop")
		File(params.airflow_webserver_pid_file,
			action = "delete",
			owner = params.airflow_user
		)

	def status(self, env):
		import status_params
		env.set_params(status_params)
		#use built-in method to check status using pidfile
		check_process_status(status_params.airflow_webserver_pid_file)

	def initdb(self, env):
		import params
		env.set_params(params)
		self.configure(env)
		Execute(format("export AIRFLOW_HOME={airflow_home} && airflow initdb"),
			user=params.airflow_user
		)

if __name__ == "__main__":
	AirflowWebserver().execute()
