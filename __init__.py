import os

try:
    import requests  # noqa
except Exception:
    os.system("pip install requests")

try:
    from curl_cffi import requests as _cffi  # noqa
except Exception:
    os.system("pip install curl_cffi")
