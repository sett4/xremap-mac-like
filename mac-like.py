from xremap.dsl import *

define_keymap({}, {
    'ALT_R-b': 'left',
    'ALT_R-f': 'right',
    'ALT_R-p': 'up',
    'ALT_R-n': 'down',
    'ALT_R-a': 'home',
    'ALT_R-e': 'end',
    'ALT_R-c': 'C-c',
    'ALT_R-d': 'delete',
}, 'Emacs-like keys')


define_keymap({
    'only': ['Google-chrome','Code', 'gnome-terminal-server']
}, {
    'CTRL-SHIFT-RIGHTBRACE': 'LEFTCTRL-PAGEDOWN',
    'CTRL-SHIFT-LEFTBRACE': 'LEFTCTRL-PAGEUP',
    # 'C-tab': 'Alt-tab',
}, 'Mac-like keys')

define_keymap({
    'only': ['Code']
}, {
    'C-M-f': 'C-h',
}, 'Mac-like keys')

 

# define_keymap({}, {
#     'ALT-A': 'CTRL-a',
#     'Alt-c': 'CTRL-c',
#     'Alt-v': 'CTRL-v',
#     'Alt-t': 'CTRL-t',
#     'Alt-w': 'CTRL-w',
#     'Alt-f': 'CTRL-f',
#     'Alt-'
# }, 'Mac-like keys')


define_modmap({
    'Win_L': {
        'held': 'Alt_L',
        'alone': 'Win_L'
    },
    'CapsLock': 'Alt_R',
    'Alt_R': {
        'held': 'Control_R',
        'alone': 'Henkan',
        # 'alone_timeout_millis': 100
    },
    'Alt_L': {
        'held': 'Control_L',
        'alone': 'Muhenkan',
        # 'alone_timeout_millis': 100
    }
})
