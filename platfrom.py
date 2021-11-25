import platform


if platform.system() != 'Linux':
    print('bad')
else:
    print('good')