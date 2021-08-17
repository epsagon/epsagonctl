
from epsagonctl.consts import (
    VARS_COMMAND, VARS_SUBCOMMAND, API_BASE_URL
)

import argparse
import requests


def _parse_args():
    parser = argparse.ArgumentParser(
        description='Epsagon CLI Parser'
    )
    commands = parser.add_subparsers(title='Epsagon Command', dest=VARS_COMMAND)

    users_parser = commands.add_parser('iam', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    users_parser.add_argument(VARS_SUBCOMMAND, help='IAM Operation to Perform', type=str)

    return vars(parser.parse_args())


def _req(path, method, headers=None, body=None):
    return {
        'get': lambda _url, _headers=None: requests.get(_url, headers=_headers or {}),
        'post': lambda _url, _headers=None: requests.post(_url, headers=_headers or {}),
    }.get(method)(f'{API_BASE_URL}/{path}', {'Authorization': 'Bearer 2db3136a-bcc2-458c-b717-a1f78cd74942'})

def _invite_user():
    pass

def _list_users():
    return _req('auth/users_in_account', 'post')

def _list_groups():
    return _req('groups', 'get')

def _invite_user():
    return _req('auth/invite_user', 'post')





def init_cli():
    epsagon_path = os.path.expanduser('~/.epsagon')
    if not os.path.exists(epsagon_path):
        with open(epsagon_path, 'w+') as epsagon_file:
            epsagon_file.write()
        # cmd('mkdir', PIPS_PATH)
    # if not os.path.exists(CREDENTIALS_PATH):
        name = input('Org Name: ')
        pips_id = input('PIPS id: ')
        with open(CREDENTIALS_PATH, 'w+') as creds_f:
            toml.dump({'credentials': {'name': name, 'pips_id': pips_id}}, creds_f)
        # cmd('echo', f'"{creds_toml}"', '>', CREDENTIALS_PATH, log=True)


def verify_action():
    res = input('Continue? [y/N]\n -> ')
    if 'y' in res:
        return True
    print('Bye.')
    return False