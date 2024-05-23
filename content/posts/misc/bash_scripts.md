---
date: 2023-11-17
title: "Notes on Bash scripting"
---

### Common shell commands
- `whoami` - username
- `id` - user id
- `date`
- `man` - manual
- `find` for searching files

## shell scripting

### shebang
- `#!<interpreter_path> [optional_args]`: e.g. `#!/bin/bash -x` `#!/usr/bin/env python3`

### `${}` vs `$()`
- `${}` - variable substitution, e.g. `${var}` or `${var:-default}` or `${var:=default}`
- `$()` - command substitution, e.g. `$(command)`

### Pipes and filters
- `|` - pipe, used to chain filter commands
- filter commands: `wc, cat, more, head, sort, grep, etc`

### Meta-characters
- `#` comment, `;` command separator, `&` run command in background
- `\` escape char, `""` literal with evaluation meta-characters, `''` just literal no eval
- `>` redirect output to file, `>>` append output to file, `2>, 2>>` rediect / append stderr to file
- `<` file content to std input , `<<` here document, 

### Cron Job Scheduling
- `crontab -e` open editor
- `m h dom mon dow command` - minute, hour, day of month, month, day of week, command
  - example `0 0 * * * /path/to/script.sh` - run script at midnight every day
- 

###  Linux user and group management system
#### common groups
- `adm` (admin), `dialout` (port access), `cdrom, audio, video, etc` (hardware access), `sudo`, `plugdev, netdev, bluetooth, etc` (device access)
- `/etc/passwd` - user info, mapping of username, user_id, GID(primary group id), user_info, home_dir, login_shell_path
  - example `shane:x:1000:1000:,,,:/home/shane:/bin/bash`
- `/etc/group`: group info, mapping of groupname, group_id, group_members
  - example `adm:x:4:syslog,shane`
- `/etc/shadow`: encrypted password info and expiration info
  - example `shane:$y$j9T$.....:19756:0:99999:7:::`
- `etc/gshadow`: group password info

#### permission Lookup process
0. critical info like permissions are cached in RAM (if using `nscd` or `sssd`, otherwise, relies on kernel caching)
1. when run a command, the system first check who can execute the command / file.
2. then it checks current user's UID and GID to see if you can execute it.
