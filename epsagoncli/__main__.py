#! /usr/bin/python3

from epsagoncli.consts import (
    VARS_COMMAND, VARS_SUBCOMMAND
)
from epsagoncli.utils import (
    _parse_args, _list_users, _list_groups, _invite_user
)


def run():
    cmd = _parse_args()
    res = {
        'iam': {
            'list-users': _list_users,
            'list-groups': _list_groups,
            'invite-user': _invite_user
        },
    }[cmd[VARS_COMMAND]][cmd[VARS_SUBCOMMAND]]()

    print(res.status_code, res.text)


if __name__ == '__main__':
    run()