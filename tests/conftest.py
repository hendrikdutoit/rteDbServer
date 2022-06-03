'''Create a conftest.py

Define the fixture functions in this file to make them accessible across multiple test files.
'''
import datetime
from pathlib import Path
import pytest

# import sys
from tempfile import mkdtemp
from beetools import rm_tree

# import configparserext
# from github import Github, GithubException as gh_exc

_DESC = __doc__.split('\n')[0]
_PATH = Path(__file__)

_INI = '''
[Batch01]
# Cmd1050 = sudo;apt-get;-y;install;nginx
Cmd1060 = sudo;apt-get;-y;install;mysql-server

[Batch02]
# Cmd2010 = sudo;apt-get;-y;install;php-fpm
# Cmd2020 = sudo;apt-get;-y;install;php-mysql
# Cmd2030 = sudo;apt-get;-y;install;gcc
# Cmd2040 = sudo;apt-get;-y;install;cython3
# Cmd2050 = sudo;apt-get;-y;install;libxml2-dev
# Cmd2060 = sudo;apt-get;-y;install;libxslt-dev
# Cmd2070 = sudo;apt-get;-y;install;zlib1g-dev
# Cmd2080 = sudo;apt-get;-y;install;python3-dev
# #Cmd2080 = sudo;apt-get;-y;rteinstallserver;python3-pip
# Cmd2090 = sudo;apt-get;-y;install;libsqlite3-0
# Cmd2100 = sudo;apt-get;-y;install;libmysqlclient-dev
Cmd2110 = sudo;apt-get;-y;install;mysql-client
# Cmd2120 = sudo;apt-get;-y;install;uwsgi
# Cmd2130 = sudo;apt-get;-y;install;uwsgi-plugin-python3
# Cmd2140 = sudo;apt-get;-y;install;python3-venv
# Cmd2150 = sudo;mkdir;-p;%(ReahlFolder)s
# Cmd2160 = sudo;chmod;777;%(ReahlFolder)s
# Cmd2170 = sudo;mkdir;-p;%(ReahlDbFolder)s
# Cmd2180 = sudo;chmod;777;%(ReahlDbFolder)s
# Cmd2190 = sudo;chown;www-data.www-data;%(ReahlDbFolder)s
# Cmd2200 = sudo;mkdir;-p;%(ReahlDistributionFolder)s
# Cmd2210 = sudo;chmod;777;%(ReahlDistributionFolder)s
# Cmd2220 = sudo;mkdir;-p;%(ReahlConfigFolder)s
# Cmd2230 = sudo;chmod;777;%(ReahlConfigFolder)s
# Cmd2240 = sudo;chmod;777;%(wwwFolder)s
# Cmd2260 = sudo;chmod;-R;u+wr,g+wr,o+wr;%(NginXRootFolder)s/sites-available
# Cmd2270 = sudo;chmod;-R;u+wr,g+wr,o+wr;%(NginXRootFolder)s/sites-enabled
# Cmd2280 = sudo;chmod;-R;u+wr,g+wr,o+wr;%(UwsgiRootFolder)s/apps-available
# Cmd2290 = sudo;chmod;-R;u+wr,g+wr,o+wr;%(UwsgiRootFolder)s/apps-enabled
# Cmd2300 = sudo;rm;-f;%(NginXRootFolder)s/sites-enabled/default
#
[Batch03]
# Cmd3010 = sudo;nginx;-t
# Cmd3020 = sudo;systemctl;stop;nginx
# Cmd3030 = sudo;systemctl;start;nginx
# Cmd3040 = sudo;systemctl;is-enabled;nginx
# Cmd3060 = sudo;systemctl;stop;uwsgi
# Cmd3070 = sudo;systemctl;start;uwsgi
# Cmd3080 = sudo;systemctl;is-enabled;uwsgi
#
[DEFAULT]
# etcFolder               = /etc
InstallUserId           = rtinstall
# InstallUserPassword     = Rt1inst@ll
# NginXRootFolder         = %(etcFolder)s/nginx
# ProjectsFolder          = /nfs/projects
# VenvBaseFolder          = %(UsrLocalFolder)s
# ReahlFolder             = %(UsrLocalFolder)s/reahl
# ReahlDistributionFolder = /nfs/Lib/Wheels
# ReahlDbFolder           = %(ReahlFolder)s/db
# ReahlConfigFolder       = %(etcFolder)s/reahl.d
# DataFolder              = %(usrLocalFolder)s/realtime
# UsrLocalFolder          = /usr/local
# UwsgiRootFolder         = %(etcFolder)s/uwsgi
# wwwFolder               = /var/www
#
# [Domains]
# Url01 = rthome.co.za
# Url02 = rtclub.co.za
# Url03 = rtregion.co.za
# Url04 = rtprovince.co.za
# Url05 = rtferderation.co.za
# # Url06 = rtschool.co.za  # src-dev01
#
# [Folders]
# CodeSubFolder  = Code
# DataSubFolder  = Data
#
[General]
BatchNamePrefix   = Batch
CommandNamePrefix = Cmd
# DefAdminEmail     = admin  # Omit the domain
# DomainNamePrefix  = Url
PackagePrefix     = App
MySQLRightsPrefix = Rights
TargetOS          = linux
UserPrefix        = User
# VenvSuffix        = _env

[LinuxUsers]
User1 = hendrik;S@ret6810;sudo
#
# [LogLevels]
# #CRITICAL = 50, ERROR = 40, WARNING = 30, INFO = 20, DEBUG = 10, NOTSET = 0
# Default = 0
# Console = 0
# File    = 0

[MySQLUsers]
Admin = root;En0l@Gay
# User1 = %(InstallUserId)s;%(InstallUserPassword)s;localhost
# Rights1 = root;localhost;*;*;Y;ALL
# Rights2 = %(InstallUserId)s;localhost;*;*;Y;ALL
#
# [ReahlPreReqPackages]
# App01 = wheel
#
# [ReahlWheels]
# #App01 = RealTimeEventsWS-0.0-py2.py3-none-any.whl
#
# [RealTimeEventsWS]
# AppActive       = Yes
# CreateDb        = Yes
# CreateDbTables  = Yes
# CreateDbUser    = Yes
# DataBase        = mysql
# eMail           = no-reply@realtimeevents.co
# RemoteDbAccess  = Yes
# SMTP            = mail.smtp_port=25
# uwsgiProcesses  = 2
# uwsgiThreats    = 2
# WebSiteRoot     = HomePageUI
#
# [rthome.co.za]
# SiteActive  = Yes
# ReahlApp    = RealTimeEventsWS
#
# [rtclub.co.za]
# SiteActive  = Yes
# ReahlApp    = RealTimeEventsWS
#
# [rtregion.co.za]
# SiteActive  = Yes
# ReahlApp    = RealTimeEventsWS
#
# [rtprovince.co.za]
# SiteActive  = Yes
# ReahlApp    = RealTimeEventsWS
#
# [rtferderation.co.za]
# SiteActive  = Yes
# ReahlApp    = RealTimeEventsWS
#
# [prodigyhelmsman.co.za]
# SiteActive  = Yes
# ReahlApp    = prodigyhelmsman
#
[SystemPreReqPackages]
App100 = mysql-connector-python

# [SystemPreReqWheels]
#
# [Test]
# TestMode     = Yes
'''

_PROJECT_NAME = "rtedbserver"


class WorkingDir:
    def __init__(self):
        self.dir = Path(mkdtemp(prefix='packageit_'))


class EnvSetUp:
    def __init__(self, p_make_project_ini=False):
        # self.project_name = self.make_project_name()
        self.dir = WorkingDir().dir
        self.ini_pth = self.dir / 'rtdbserver.ini'
        self.ini_pth.write_text(_INI)
        # self.external_arc_dir = self.dir / 'external_archive'
        # self.external_arc_dir.mkdir(parents=True)
        # self.packageit_ini_pth = self.make_packageit_ini()
        # self.project_ini_pth = None
        # self.token_dir = Path('d:\\', 'dropbox', 'lib', 'SSHKeys')
        # self.token_gh_pth = self.token_dir / 'github_token.txt'
        # self.token_pypi_pth = self.token_dir / 'PYPI_API_TOKEN.txt'
        # self.token_testpypi_pth = self.token_dir / 'TEST_PYPI_API_TOKEN.txt'
        # self.token_rtd_pth = self.token_dir / 'readthedocs_token.txt'
        #
        # if p_make_project_ini:
        #     self.project_ini_pth = self.make_project_ini()
        pass

    def create_mock_files(self):
        # project_root_dir = self.dir / self.project_name
        # src_dir = project_root_dir / 'src' / self.project_name.lower()
        # (src_dir / '{}.py'.format(self.project_name.lower())).write_text(
        #     'Test file\nThis file is included'
        # )
        # (src_dir / '{}.pyc'.format(self.project_name.lower())).write_text(
        #     'Test file\nThis file is excluded'
        # )
        # (src_dir / '{}.ini'.format(self.project_name.lower())).write_text('[Folders]\n')
        pass

    def make_packageit_ini(self):
        # '''Make INI file for testing'''
        # packageit_ini_pth = self.dir / 'pimt.ini'
        # ini = configparserext.ConfigParserExt(inline_comment_prefixes="#")
        # ini['Classifiers'] = {
        #     'DevStatus': 'Development Status :: 1 - Planning',
        #     'IntendedAudience002': 'Intended Audience :: Developers',
        #     'IntendedAudience013': 'Intended Audience :: System Administrators',
        #     'Topic013': 'Topic :: Software Development',
        #     'Topic027': 'Topic :: System :: Systems Administration',
        #     'License': 'License :: OSI Approved :: MIT License',
        #     'ProgrammingLanguage001': 'Programming Language :: Python :: 3.0',
        #     'ProgrammingLanguage010': 'Programming Language :: Python :: 3.9',
        #     'ProgrammingLanguage011': 'Programming Language :: Python :: 3.10',
        # }
        # ini['Coverage'] = {'Omit010': 'setup.py'}
        # ini['Detail'] = {
        #     'Author': 'Ann Other',
        #     'AuthorEmail': 'ann.other@testmodule.com',
        #     'HeaderDescription': 'Project Header Description (default ini)',
        #     'LongDescription': 'Project long description goes in here (default ini)',
        #     '{}ProjectAnchorDir'.format(get_os()): self.dir,
        #     '{}ProjectIniDir'.format(get_os()): Path(self.dir, 'ini'),
        #     'PythonRequires': '>=3.6',
        #     'Url': 'www.{}.com'.format(self.project_name.lower()),
        #     'Type': 'Module',
        # }
        #
        # ini['flake8'] = {
        #     'exclude': '__init__.py, VersionArchive /, Archive /',
        #     'max-line-length': '120',
        # }
        # ini['General'] = {'Verbose': 'Yes'}
        # ini['Git'] = {
        #     'Enable': 'Yes',
        #     #     'Include' : '*.py;*.ini;*.bat;*.sh',
        #     #     'Ignore'  : '/VersionArchive;.workspace/;__pycache__/;*.komodoproject;*.log'
        # }
        # ini['GitHub'] = {
        #     'BugTemplate': 'templ_github_bug.md',
        #     'ConfigTemplate': 'templ_github_config.yaml',
        #     'Enable': 'Yes',
        #     'FeatureTemplate': 'templ_github_feature.md',
        #     'TokenFileName': 'github_token.txt',
        #     'UserName': 'hendrikdutoit',
        #     'Url': 'https: // github.com',
        # }
        # ini['Import'] = {
        #     'ReWrite': 'Yes',
        #     'Prod01': 'pypi;termcolor',
        #     'Test01': 'pypi;pip',
        #     'Test02': 'pypi;wheel',
        #     'Test03': 'pypi;pre-commit',
        #     'Test04': 'pypi;pytest',
        #     'Test05': 'pypi;beetools',
        #     'Test06': 'pypi;pytest-cov',
        #     'Test07': 'pypi;sphinx',
        #     'Test08': 'pypi;sphinx-autobuild',
        #     'Test09': 'pypi;black',
        #     'Test10': 'pypi;build',
        #     'Test11': 'pypi;configparserext',
        #     'Test12': 'pypi;pygithub',
        # }
        # ini['Install Apps'] = {'App01': 'pre-commit install'}
        # ini['LogLevels'] = {'Default': 0, 'Console': 0, 'File': 0}
        # ini['PyPi'] = {
        #     'Publishing': 'GitHub',  # No | GitHub| Twine
        #     'Repository': 'testpypi',
        #     'TokenFileNamePyPi': 'PYPI_API_TOKEN.txt',
        #     'TokenFileNameTestPyPi': 'TEST_PYPI_API_TOKEN.txt',
        # }
        # ini['ReadTheDocs'] = {
        #     'Enable': 'Yes',
        #     'ConfigTemplate': 'readthedocs_def_.readthedocs_template.yaml',
        #     'NewProjectTemplate': 'readthedocs_def_newproject_template.json',
        #     'TokenFileName': 'readthedocs_token.txt',
        # }
        # ini['Sphinx'] = {
        #     'Enable': "Yes",
        #     'ConfPyInstr001': "extensions = ['sphinx.ext.autodoc']",
        #     'ConfPyInstr010': "templates_path = ['_templates']",
        #     'ConfPyInstr020': "language = 'en'",
        #     'ConfPyInstr030': "exclude_patterns = []",
        #     'ConfPyInstr040': "html_theme = 'agogo'",
        #     'ConfPyInstr050': "html_static_path = ['_static']",
        #     'AddSection001': "Installation",
        #     'AddSection010': "Usage",
        #     'AddSection020': "Support",
        #     'AddContent001': "conventions",
        #     'AddContent010': "api",
        #     'AddContent020': "donotexist",
        # }
        # ini['tool:pytest'] = {
        #     'addopts_cmd': '--doctest-modules '
        #     '--cov=tests --cov=packageit '
        #     '--ignore-glob=*/VersionArchive '
        #     '--ignore-glob=*/Archive '
        #     '--ignore-glob=*/Templates '
        #     '--cov-report=html',
        #     'addopts_ide': '--ignore-glob=*/VersionArchive '
        #     '--ignore-glob=*/Archive '
        #     '--cov-report=html',
        # }
        # ini['VEnv'] = {
        #     'Enable': 'Yes',
        #     'Upgrade': 'Yes',
        #     'ReinstallVEnv': 'No',
        #     '{}VEnvBaseFolder'.format(get_os()): self.dir,
        #     '{}VEnvAnchorDir'.format(get_os()): self.dir / 'venv',
        # }
        # with open(packageit_ini_pth, 'w') as ini_file:
        #     ini.write(ini_file)
        # return packageit_ini_pth
        pass

    def make_project_ini(self):
        # '''Make a project specific ini file'''
        # project_ini_pth = Path(
        #     self.packageit_ini_pth.parents[0],
        #     self.project_name,
        #     '.packageit',
        #     'packageit.ini',
        # )
        # if not project_ini_pth.parents[0].exists():
        #     project_ini_pth.parents[0].mkdir(parents=True)
        # ini = configparserext.ConfigParserExt(inline_comment_prefixes="#")
        # ini['Classifiers'] = {
        #     'DevStatus': 'Development Status :: 1 - Planning',
        #     'IntendedAudience002': 'Intended Audience :: Developers',
        #     'IntendedAudience003': 'Intended Audience :: System Administrators',
        #     'Topic013': 'Topic :: Software Development',
        #     'License': 'License :: OSI Approved :: MIT License',
        #     'ProgrammingLanguage001': 'Programming Language :: Python :: 3.0',
        #     'ProgrammingLanguage011': 'Programming Language :: Python :: 3.10',
        # }
        # ini['Coverage'] = {}
        # ini['Detail'] = {
        #     'Author': 'Hendrik du Toit',
        #     'AuthorEmail': 'hendrik@brightedge.co.za',
        #     'HeaderDescription': 'Project Header Description (project ini)',
        #     'Import01': 'import sys',
        #     'LongDescription': 'Project long description goes in here (project ini)',
        #     'Url': 'www.brightedge.co.za',
        # }
        # ini['flake8'] = {
        #     'exclude': '__init__.py, VersionArchive /, Archive /',
        #     'max-line-length': '120',
        # }
        # ini['General'] = {'Verbose': 'Yes'}
        # ini['Git'] = {}
        # ini['GitHub'] = {'UserName': 'hendrikdutoit', 'Url': 'https: // github.com'}
        # ini['Import'] = {}
        # ini['Install Apps'] = {}
        # ini['LogLevels'] = {}
        # ini['PyPi'] = {}
        # ini['Sphinx'] = {}
        # ini['tool:pytest'] = {
        #     'addopts_cmd': '--doctest-modules '
        #     '--cov = tests '
        #     '--cov=packageit '
        #     '--ignore-glob=*/VersionArchive '
        #     '--ignore-glob=*/Archive '
        #     '--ignore-glob=*/Templates '
        #     '--cov-report=html',
        #     'addopts_ide': '--ignore-glob=*/VersionArchive '
        #     '--ignore-glob=*/Archive '
        #     '--cov-report=html',
        # }
        # ini['VEnv'] = {}
        # with open(project_ini_pth, 'w') as project_ini_file:
        #     ini.write(project_ini_file)
        # return project_ini_pth
        pass

    def make_project_name(self):
        return '{}_{}'.format(
            _PROJECT_NAME, datetime.datetime.now().strftime('%y%m%d%H%M%S%f')
        )


@pytest.fixture
def env_setup_self_destruct():
    '''Set up the environment base structure'''
    setup_env = EnvSetUp()
    yield setup_env
    rm_tree(setup_env.dir, p_crash=False)


@pytest.fixture
def env_setup_with_project_ini_self_destruct():
    '''Set up the environment base structure'''
    setup_env = EnvSetUp(p_make_project_ini=True)
    yield setup_env
    rm_tree(setup_env.dir, p_crash=False)


@pytest.fixture
def working_dir_self_destruct():
    '''Set up the environment base structure'''
    working_dir = WorkingDir()
    yield working_dir
    rm_tree(working_dir.dir, p_crash=False)
