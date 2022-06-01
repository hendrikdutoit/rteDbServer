'''Testing rtedbserver__init__()'''

from pathlib import Path
from beetools.beearchiver import Archiver
import rtedbserver

_PROJ_DESC = __doc__.split('\n')[0]
_PROJ_PATH = Path(__file__)


def project_desc():
    return _PROJ_DESC


b_tls = Archiver(_PROJ_DESC, _PROJ_PATH)


class TestrteDbServer:
    def test__init__(self, env_setup_self_destruct):
        env_setup = env_setup_self_destruct
        t_rtedbserver = rtedbserver.RteDbServer(env_setup.ini_pth)

        assert t_rtedbserver.success
        pass

    def test_create_linux_users(self, env_setup_self_destruct):
        env_setup = env_setup_self_destruct
        t_rtedbserver = rtedbserver.RteDbServer(env_setup.ini_pth)
        t_rtedbserver.create_linux_users()
        pass

    def test_create_mysql_users(self, env_setup_self_destruct):
        env_setup = env_setup_self_destruct
        t_rtedbserver = rtedbserver.RteDbServer(env_setup.ini_pth)
        t_rtedbserver.create_mysql_users()
        pass

    def test_install(self, env_setup_self_destruct):
        env_setup = env_setup_self_destruct
        t_rtedbserver = rtedbserver.RteDbServer(env_setup.ini_pth)
        t_rtedbserver.install()
        pass

    def test_secure_mysql(self, env_setup_self_destruct):
        env_setup = env_setup_self_destruct
        t_rtedbserver = rtedbserver.RteDbServer(env_setup.ini_pth)
        t_rtedbserver.secure_mysql()
        pass

    def test_start_firewall(self, env_setup_self_destruct):
        env_setup = env_setup_self_destruct
        t_rtedbserver = rtedbserver.RteDbServer(env_setup.ini_pth)
        t_rtedbserver.start_firewall()
        pass


del b_tls
