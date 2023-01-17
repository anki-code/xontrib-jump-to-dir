from xonsh.built_ins import XSH

_hist_backend = XSH.env.get('XONSH_HISTORY_BACKEND')

if _hist_backend == 'sqlite':
    def _jump_to_dir(args):
        import sqlite3 as _sqlite3
        from pathlib import Path as _Path
        con = _sqlite3.connect(XSH.env.get('XONSH_HISTORY_FILE'))
        success = False
        try:
            cur = con.cursor()
            sql = f"""
                SELECT cwd FROM xonsh_history 
                WHERE cwd LIKE ? and cwd != ?
                GROUP BY cwd ORDER BY count(*) DESC
                LIMIT 10"""
            for row in cur.execute(sql, (f"%{'%'.join(args) if args else ''}%", XSH.env.get('PWD'))):
                if _Path(row[0]).exists():
                    __xonsh__.subproc_captured_stdout(['cd', row[0]])
                    success = True
                    break
        finally:
            con.close()

        return 0 if success else 1

    aliases['j'] = _jump_to_dir
    del _jump_to_dir
else:
    print(f"xontrib-jump-to-dir: You're using {_hist_backend} for history backend. It's not supported for jump.")
    print("xontrib-jump-to-dir: Feel free to contribute: https://github.com/anki-code/xontrib-jump-to-dir")
