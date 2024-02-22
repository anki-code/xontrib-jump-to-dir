"""Jump to used before directory by part of the path. Lightweight zero-dependency implementation of autojump or zoxide projects functionality. """

from xonsh.built_ins import XSH
import functools

_hist_backend = XSH.env.get('XONSH_HISTORY_BACKEND')

if _hist_backend == 'sqlite':
    def _jump_to_dir(args, search_column='cwd'):
        import sqlite3 as _sqlite3
        from pathlib import Path as _Path
        con = _sqlite3.connect(XSH.env.get('XONSH_HISTORY_FILE'))
        success = False
        try:
            cur = con.cursor()
            sql = f"""
                SELECT cwd FROM xonsh_history 
                WHERE 
                  {search_column} LIKE ? 
                  AND cwd != ?
                  AND inp NOT LIKE 'j %'
                  AND inp NOT LIKE 'jc %'
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

    c = __xonsh__.env.get('XONTRIB_JUMP_TO_DIR_SHORTCUT', 'j')
    aliases[c] = functools.partial(_jump_to_dir, search_column='cwd')
    aliases[c+'c'] = functools.partial(_jump_to_dir, search_column='inp')

elif __xonsh__.env.get('XONTRIB_JUMP_TO_DIR_WARNING', True):
    print(f"xontrib-jump-to-dir: You're using {_hist_backend} for history backend. It's not supported for jump.")
    print("xontrib-jump-to-dir: Feel free to contribute: https://github.com/anki-code/xontrib-jump-to-dir")
