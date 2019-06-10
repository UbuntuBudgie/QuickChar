import os
from Xlib.display import Display
from Xlib import X
from Xlib.ext.xtest import fake_input
import Xlib.XK


def paste_char(*args, **kwargs):
    for c in args:
        fake_input(_display, X.KeyPress, _to_keysim(c))
        _display.sync()
    for c in reversed(args):
        fake_input(_display, X.KeyRelease, _to_keysim(c))
        _display.sync()


def _to_keysim(gotkey):
    return _display.keysym_to_keycode(Xlib.XK.string_to_keysym(gotkey))


_display = Display(os.environ['DISPLAY'])
