#! /usr/bin/python3

from epsagonctl.consts import (
    VARS_COMMAND, VARS_SUBCOMMAND, VARS_DEFAULT,
)
from epsagonctl.utils import (
    _parse_args, _list_users, _list_groups, _invite_user
)

options = {
    'iam': {
        'invite-user': _invite_user,
        'list-users': _list_users,
        'list-groups': _list_groups,
    },
    VARS_DEFAULT: {
        VARS_DEFAULT: lambda: None
    },
}


def run():
    args = _parse_args()
    res = options.get(
        args.get(VARS_COMMAND, options[VARS_DEFAULT])
    ).get(
        args.get(VARS_SUBCOMMAND, options[VARS_DEFAULT][VARS_DEFAULT])
    )()

    print(res.json())


if __name__ == '__main__':
    run()
