import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

repo_url = 'https://github.com/Jmarinesq/djangotdd'

#env.use_ssh_config = True

env.password = 'AAAAB3NzaC1yc2EAAAADAQABAAABgQDkwYcyuikNoC3uU3cPCQk2/hpQmAtsgbGOyDMJ024tdbYDqsaqVFc94FsgqQRN8KWf3PnARPloWRPctn3ixz0YGAtUiNHR1ltx6Ipr8oXA5lK/+pawQerCiReZmgAe1lAdFXVd5xBR53qq0oDQAFdhZUeSreMxXUpcY1AMa4UCuseQBKtLS9btQAmMfWuEEX9DNEQ8Q6gFVC2PkZq2Po6qw2iBJr101fOeXDPlpc8GU1iNCRLSmk6bf++UnMTubvxAXpsUVnWtwUg2duFxBSMIBa1muE021myGs9KVq/9rxus4nAb6T02PKTzlv4m77MeH4D7f3bQiaZd8Zl0fedMGZjYP96e7Uz8TgPKURcNT+n41X+rQrQ1wEZPSt1s/2dmf/QLVR4Yw/8TQa+y8/yRvEvQiTIkeiA85oeS1wwCWeCN2m62FblK4yBUXEKN9J7L1CTe5GsfXwjnHopPI7vCbGRs3HK2eJo1RzX/qo46Fkql1xOHVsNmDiIc+hLG0iBE=A187AG@A187AGC02W109BHV2Q'


def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):

        _get_latest_source()
        print("_get_latest_source()")
        _update_virtual_env()
        print("_update_virtual_env()")
        _create_or_update_dotenv()
        print("_create_or_update_dotenv()")
        _update_static_files()
        print("_update_static_files()")
        _update_database()


def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone{repo_url} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')


def _update_virtual_env():
    if not  exists('virtualenv/bin/pip'):
        run(f'python3 -m venv virtualenv')
    run('./virtualenv/bin/pip install -r requirements.txt')


def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f'SITENAME={env.host.split(_)[0]}')
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789',
            k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')


def _update_static_files():
    run('./virtualenv/bin/python manage.py collectstatic --noinput')


def _update_database():
    run('.virtualenv/bin/python manage.py migrate --noinput')




