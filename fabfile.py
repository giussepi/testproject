""" fabric's file """

from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['giuseppi@198.101.153.252']

def test():
    local("./manage.py test baseapp")

def push():
    local("git push")

def prepare_deploy():
    test()
    push()

def deploy():
    test()
    code_dir = '~giuseppi/testproject'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone git@github.com:giussepi/testproject.git {}".format(
                code_dir))
            run("virtualenv --distribute ../env")

    with cd(code_dir):
        run("git pull")        
        commands_tuple = (
            'source ../env/bin/activate',
            'pip install -r requirements.txt',
            './manage.py collectstatic --noinput',
        )
        run(" && ".join(commands_tuple))

        # the following line is not working :(
        # run("source ../env/bin/activate && pip install -r requirements.txt && ./manage.py collectstatic --noinput && nohup ./manage.py runserver 0.0.0.0:8000 >& /dev/null < /dev/null &")
