from fabric.contrib.project import rsync_project
from fabric.api import run


def sync_files():
	rsync_project(remote_dir='/var/www/vhosts/ludumdare.pl/ldpoznan',
		local_dir='ldpoznan/',
		exclude=['local_settings.py', '*.pyc', '*.wsgi', '*/static/*'],
		delete=True,
		extra_opts='')

def reload_wsgi():
	run('touch /var/www/vhosts/ludumdare.pl/ldpoznan/ldpoznan.wsgi')

def deploy():
	sync_files()
	reload_wsgi()