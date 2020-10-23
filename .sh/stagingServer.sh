source /antenv/bin/activate
/antenv/bin/python /home/site/wwwroot/manage.py migrate --noinput
apt-get install git -y
git clone https://github.com/Jmarinesq/djangotdd.git .

export SITENAME=superlists.azurewebsites.net

ssh jmarin@157.245.68.84
jmarin - jmejme

mkdir -p ~/.ssh
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDkwYcyuikNoC3uU3cPCQk2/hpQmAtsgbGOyDMJ024tdbYDqsaqVFc94FsgqQRN8KWf3PnARPloWRPctn3ixz0YGAtUiNHR1ltx6Ipr8oXA5lK/+pawQerCiReZmgAe1lAdFXVd5xBR53qq0oDQAFdhZUeSreMxXUpcY1AMa4UCuseQBKtLS9btQAmMfWuEEX9DNEQ8Q6gFVC2PkZq2Po6qw2iBJr101fOeXDPlpc8GU1iNCRLSmk6bf++UnMTubvxAXpsUVnWtwUg2duFxBSMIBa1muE021myGs9KVq/9rxus4nAb6T02PKTzlv4m77MeH4D7f3bQiaZd8Zl0fedMGZjYP96e7Uz8TgPKURcNT+n41X+rQrQ1wEZPSt1s/2dmf/QLVR4Yw/8TQa+y8/yRvEvQiTIkeiA85oeS1wwCWeCN2m62FblK4yBUXEKN9J7L1CTe5GsfXwjnHopPI7vCbGRs3HK2eJo1RzX/qo46Fkql1xOHVsNmDiIc+hLG0iBE= A187AG@A187AGC02W109BHV2Q
' >> ~/.ssh/authorized_keys