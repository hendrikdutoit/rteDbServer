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
        """Assert class __init__"""
        env_setup = env_setup_self_destruct
        t_rtedbserver = rtedbserver.RteDbServer(env_setup.dir)

        assert t_rtedbserver.success
        pass


del b_tls
