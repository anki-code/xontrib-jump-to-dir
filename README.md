<p align="center">
Jump to directory by name. <br>Lightweight zero-dependency implementation of <a href="https://github.com/wting/autojump">autojump</a> or <a href="https://github.com/ajeetdsouza/zoxide">zoxide</a> projects functionality. 
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

j  # Jump to most frequent directory
j Doc  # Jump to directory with "Doc" in path
```

## Credits

This package was created with [xontrib template](https://github.com/xonsh/xontrib-template).
