'''Testing rtedbserver__init__()'''

from pathlib import Path
from beetools.beearchiver import Archiver
import installit
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
        assert t_rtedbserver.ini_path == env_setup.ini_pth
        assert t_rtedbserver.batch_name_prefix == 'Batch'
        assert t_rtedbserver.command_name_prefix == 'Cmd'
        assert t_rtedbserver.install_userid == 'rtinstall'
        assert t_rtedbserver.mysql_rights_prefix == 'Rights'
        assert t_rtedbserver.package_prefix == 'App'
        assert t_rtedbserver.target_os == 'linux'
        assert t_rtedbserver.user_prefix == 'User'
        assert isinstance(t_rtedbserver.inst_tls, installit.InstallIt)
        assert t_rtedbserver.success
        pass

    def test_configure_mysql_remote_access(self, env_setup_self_destruct):
        env_setup = env_setup_self_destruct
        t_rtedbserver = rtedbserver.RteDbServer(env_setup.ini_pth)
        t_rtedbserver.configure_mysql_remote_access()
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

    def test_install_system_prereq_packages(self, env_setup_self_destruct):
        env_setup = env_setup_self_destruct
        t_rtedbserver = rtedbserver.RteDbServer(env_setup.ini_pth)
        t_rtedbserver.install_system_prereq_packages()
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
