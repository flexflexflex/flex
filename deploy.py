from fabric import Connection

HOST = '18.224.29.19'
KEY_PATH = '/Users/kensay/.ssh/flex.pem'

con = Connection(HOST, connect_kwargs={
    'key_filename': KEY_PATH,
}, user='ubuntu')

with con.cd('/var/www/flex/'):
    con.run('sudo docker-compose down')
    con.run('sudo git pull')
    con.run('sudo docker-compose up --build -d')

