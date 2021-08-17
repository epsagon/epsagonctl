
 <p align="center">
   <a href="https://epsagon.com" target="_blank" align="center">
     <img src="https://cdn2.hubspot.net/hubfs/4636301/Positive%20RGB_Logo%20Horizontal%20-01.svg" width="300">
   </a>
   <br />
 </p>

# epsagonctl

Epsagon's Command Line Interface.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)


## Installation

Install the CLI with 

    $ pip install epsagonctl

And the package will be added to your PATH under `epsagon`.

## Usage

The CLI expects a `command` and `subcommand` for every usage.

Commands and their corresponding SubCommands include:

### IAM


IAM is Epsagon's central location for all things account-related.


<b> invite-user </b>

Invite a user to an account.

    $ epsagon iam invite-user <EMAIL-ADDR>

<b> list-users </b>

List all users in an account.

    $ epsagon iam list-users

<b> list-groups </b>
 
List all groups in an account,

    $ epsagon iam list-groups
