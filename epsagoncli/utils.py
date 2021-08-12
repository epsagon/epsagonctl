
from epsagoncli.consts import (
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
    print(method, f'{API_BASE_URL}/{path}')
    return {
        'get': lambda _url, _headers=None: requests.get(_url, headers=_headers or {}),
        'post': lambda _url, _headers=None: requests.post(_url, headers=_headers or {}),
    }.get(method)(f'{API_BASE_URL}/{path}', {'Authorization': 'Bearer 87a6f6b4-b796-455d-9d5e-bba5119c7d87'})

def _invite_user():
    pass

def _list_users():
    return _req('auth/users_in_account', 'post')

def _list_groups():
    return _req('groups', 'get')

def _invite_user():
    return _req('auth/invite_user', 'post')
