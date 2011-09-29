# Fabric for deploying getteamtasks.com

from fabric.api import *

# SERVER
PRODUCTION = '46.51.184.117'


def production():
    """Production site"""
    env.alias = "production"
    env.hosts = [PRODUCTION]
    env.path = '/var/www/jqwiki.com'
    env.user = 'ubuntu'
    env.key_filename  = '/Users/phil.hawksworth/.ssh/philhawksworth-aws.pem'
    env.apache = 'jqwiki.com'
    env.release_path = "/var/releases/jqwiki.com"


def deploy():
    """Deployment actions"""
    export_release()
    
def initenv():
    '''Initialise the environment on the server'''
    make_release_location()
    create_web_root()    
    enable_site()


def make_release_location():
    '''Create the release code location on the server'''
    command = 'mkdir %(release_path)s'
    sudo(command % env)
    command = 'chown -R ubuntu:ubuntu %(release_path)s'
    sudo(command % env)
    
    
def create_web_root():
    '''Create the web root location'''
    command = 'mkdir %(path)s'
    sudo(command % env)
    command = 'chown -R ubuntu:ubuntu %(path)s'
    sudo(command % env)


def enable_site():
    '''Enable the new website'''
    command = 'a2ensite %(apache)s'
    sudo(command % env)    
    restart()
        

def export_release():
    """Exports a release with the current time and date"""
    run('cd %s && git pull origin master' % env.release_path)
    run('cp -R %(release_path)s/www/* %(path)s' % env)


def copy_apache():
    """Copies the apache file to the appropriate location."""
    command = 'cp %(release_path)s/etc/apache2/%(apache)s /etc/apache2/sites-available/'
    sudo(command % env)


def restart():
    """Restarts the apache server"""
    copy_apache()
    sudo('/etc/init.d/apache2 restart')
