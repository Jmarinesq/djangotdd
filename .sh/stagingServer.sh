source /antenv/bin/activate
/antenv/bin/python /home/site/wwwroot/manage.py migrate --noinput
apt-get install git -y
git clone https://github.com/Jmarinesq/djangotdd.git .

export SITENAME=superlists.azurewebsites.net