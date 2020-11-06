import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run, sudo
import paramiko as ssh
import os

ssh.util.log_to_file("paramiko.log", 10)
repo_url = 'https://github.com/Jmarinesq/djangotdd'


def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        print("_get_latest_source()")
        _get_latest_source()
        print("_update_virtual_env()")
        _update_virtual_env()
        print("_create_or_update_dotenv()")
        _create_or_update_dotenv()
        print("_update_static_files()")
        _update_static_files()
        print("_update_database()")
        _update_database()
        print("_restart_gunicorn()")
        _restart_gunicorn()


def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone{repo_url} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')


def _update_virtual_env():
    if not exists('virtualenv/bin/pip'):
        run(f'python3 -m venv virtualenv')
    run('./virtualenv/bin/pip install -r requirements.txt')


def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f'SITENAME={env.host}')
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789',
            k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')
    email_password = os.environ['EMAIL_PASSWORD']
    append('.env', f'EMAIL_PASSWORD={email_password}')


def _update_static_files():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'{site_folder}/virtualenv/bin/python3 {site_folder}/manage.py collectstatic --noinput')


def _update_database():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'{site_folder}/virtualenv/bin/python3 {site_folder}/manage.py migrate --noinput')


def _restart_gunicorn():
    sudo(f'sudo systemctl daemon-reload')
    sudo(f'sudo systemctl restart gunicorn')




