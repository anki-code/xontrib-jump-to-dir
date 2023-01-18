<p align="center">
Jump to used before directory by part of the path. <br>Lightweight zero-dependency implementation of <a href="https://github.com/wting/autojump">autojump</a> or <a href="https://github.com/ajeetdsouza/zoxide">zoxide</a> projects functionality. 
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/anki-code/xontrib-jump-to-dir" target="_blank">tweet</a>.
</p>

## Note

This xontrib is using [xonsh sqlite history backend](https://xon.sh/tutorial_hist.html#sqlite-history-backend) to get statistics by directories you're used to run commands.

## Installation

To install use pip:

```bash
xpip install -U git+https://github.com/anki-code/xontrib-jump-to-dir
```

## Usage

```xsh
# Check that you're using sqlite history in ~/.xonshrc
$XONSH_HISTORY_BACKEND = 'sqlite'

xontrib load jump_to_dir

mkdir -p /tmp/hello /tmp/world
cd /tmp/hello
echo 1
cd /tmp/world
echo 1
cd /

j           # Jump to most frequent directory
j wor       # Jump to directory with `*wor*` in path i.e. `/tmp/world`
j t he      # Jump to directory with `*t*he*` in path i.e. `/tmp/hello`
```

## Credits

This package was created with [xontrib template](https://github.com/xonsh/xontrib-template).
