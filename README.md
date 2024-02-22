<p align="center">
Jump to used before directory by part of the path in xonsh shell. <br>Lightweight zero-dependency implementation of <a href="https://github.com/wting/autojump">autojump</a> or <a href="https://github.com/ajeetdsouza/zoxide">zoxide</a> projects functionality. 
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/anki-code/xontrib-jump-to-dir" target="_blank">tweet</a>.
</p>

## Note

This xontrib is using [xonsh sqlite history backend](https://xon.sh/tutorial_hist.html#sqlite-history-backend) to get statistics by directories you're used to run commands.

## Installation

To install use pip:

```bash
xpip install xontrib-jump-to-dir
# OR: xpip install -U git+https://github.com/anki-code/xontrib-jump-to-dir
```

## Usage

Init:
```xsh
# Check that you're using sqlite history in ~/.xonshrc
$XONSH_HISTORY_BACKEND = 'sqlite'
xontrib load jump_to_dir
```
Jump to directory by path:
```xsh
mkdir -p /tmp/hello /tmp/world
cd /tmp/hello
echo 1
echo 2
echo 3
cd /tmp/world
echo 1
cd /

j           # Jump to most frequent directory i.e. `/tmp/hello/` because 3 `echo` commands were executed.
j wor       # Jump to directory with `*wor*` in path i.e. `/tmp/world/`.
j t he      # Jump to directory with `*t*he*` in path i.e. `/tmp/hello/`.
```
Jump to directory by command:
```xsh
cd /tmp
echo 112233
cd /
jc 22       # Jump to the directory where `*22*` command executed i.e. `/tmp`.
```

Custom shortcut:
```xsh
$XONTRIB_JUMP_TO_DIR_SHORTCUT = 'z'
xontrib load jump_to_dir
z tm            # Jump to previous directory with `*tm*` in path e.g. `/tmp/`
zc git commit   #Jump to previous directory where `*git*commit*` command executed e.g. `/git/`
```

## How it works

The history database has the commands you run and the directory where you was. The xontrib sorts the directories from history database by count of executed commands and filter them by mask e.g. the `j tm` command will find the directories by mask `*tm*`. Then you jump into the existing directory with the highest number of executed commands or if you already there to the previous directory by statistics. So if you have no commands that were executed in `/example` directory please avoid expectation that you can jump to it by running `j ex`.

If you want to add fallback functionality to jump to any directory by partial path in case of zero result in history database (e.g. `j o lo bi` will jump to `/opt/local/bin`) feel free to create PR.

## Environment variables

* `XONTRIB_JUMP_TO_DIR_SHORTCUT` - shortcut string. Default `j`.
* `XONTRIB_JUMP_TO_DIR_WARNING` - show warnings from xontrib. Default `True`.

## Credits

This package was created with [xontrib template](https://github.com/xonsh/xontrib-template).
