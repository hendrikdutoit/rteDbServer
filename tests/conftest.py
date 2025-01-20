'''Create a conftest.py

Define the fixture functions in this file to make them accessible across multiple test files.
'''

from pathlib import Path
import pytest

from tempfile import mkdtemp
from beetools import rm_tree

_DESC = __doc__.split('\n')[0]
_PATH = Path(__file__)

_INI = '''
[Batch01]
Cmd1010 = sudo;apt-get;-y;install;mysql-server

[Batch02]
Cmd2110 = sudo;apt-get;-y;install;mysql-client

[Batch03]

[DEFAULT]
InstallUserId           = installuser
InstallUserPassword     = installpassword

[General]
BatchNamePrefix   = Batch
CommandNamePrefix = Cmd
PackagePrefix     = App
MySQLRightsPrefix = Rights
TargetOS          = linux
UserPrefix        = User
# VenvSuffix      = _env

[LinuxUsers]
User1 = testuser;testpassword;sudo

[MySQLUsers]
Admin = root;root
User1 = %(InstallUserId)s;%(InstallUserPassword)s;localhost
User2 = remoteuser;remotepassword;%%
Rights1 = root;localhost;*;*;Y;ALL
Rights2 = %(InstallUserId)s;localhost;*;*;Y;ALL
Rights3 = remoteuser;%%;*;*;N;ALL

[SystemPreReqPackages]
App100 = mysql-connector-python

[Test]
TestMode     = Yes
'''

_PROJECT_NAME = "rtedbserver"


class WorkingDir:
    def __init__(self):
        self.dir = Path(mkdtemp(prefix='packageit_'))


class EnvSetUp:
    def __init__(self, p_make_project_ini=False):
        self.dir = WorkingDir().dir
        self.ini_pth = self.dir / 'rtdbserver.ini'
        self.ini_pth.write_text(_INI)
        pass

    # def make_project_name(self):
    #     return '{}_{}'.format(
    #         _PROJECT_NAME, datetime.datetime.now().strftime('%y%m%d%H%M%S%f')
    #     )


@pytest.fixture
def env_setup_self_destruct():
    '''Set up the environment base structure'''
    setup_env = EnvSetUp()
    yield setup_env
    rm_tree(setup_env.dir, p_crash=False)
