setting = {
    'filepath': __file__,
    'use_db': True,
    'use_default_setting': True,
    'home_module': None,
    'menu': {
        'uri': __package__,
        'name': 'Info 동기화',
        'list': [
            {'uri': 'basic/setting', 'name': '설정'},
            {'uri': 'basic/main',    'name': 'Info 관리'},
            {'uri': 'basic/manual',  'name': '매뉴얼'},
            {'uri': 'log',           'name': '로그'},
        ],
    },
    'setting_menu': None,
    'default_route': 'normal',
}

from plugin import *

P = create_plugin_instance(setting)

import os as _os
import sys as _sys
import traceback as _tb
try:
    from support import SupportSC
    _here = _os.path.dirname(_os.path.abspath(__file__))
    for _name in ('worker', 'providers', 'client_kakaopage',
                  'client_kakao', 'client_naver', 'client_series',
                  'client_novelpia', 'client_lezhin', 'client_munpia',
                  'client_joara', 'client_toomics', 'client_ridi'):
        if (not _os.path.exists(_os.path.join(_here, _name + '.py'))) \
                and _os.path.exists(_os.path.join(_here, _name + '.pyf')):
            _mod = SupportSC.load_module_f(__file__, _name)
            if _mod is not None:
                _sys.modules[f'{__package__}.{_name}'] = _mod
except Exception:
    P.logger.error(_tb.format_exc())

try:
    from .mod_basic import ModuleBasic
except Exception:
    from support import SupportSC
    _mb = SupportSC.load_module_P(P, 'mod_basic')
    _sys.modules[f'{__package__}.mod_basic'] = _mb
    ModuleBasic = _mb.ModuleBasic
P.set_module_list([ModuleBasic])
