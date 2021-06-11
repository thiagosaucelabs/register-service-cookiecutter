import os

REMOVE_PATHS = [
    '{% if cookiecutter.hasAPI != "YES" %} API.yaml {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    print(f'cwd: {os.getcwd()}; path: {path}; exists? {os.path.exists(path)}')
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
