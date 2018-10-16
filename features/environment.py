import os
from os.path import isfile, join, abspath, dirname, getmtime
from appium import webdriver


# Returns abs path relative to this file and not cwd
PATH = lambda p: abspath(
    join(dirname(__file__), p)
)


def get_recent_file(mypath):
    files_tuple = [(f, int(getmtime(join(mypath, f)))) for f in os.listdir(mypath) if isfile(join(mypath, f))]
    sort_by_update = sorted(files_tuple, key=lambda file: file[1])
    return sort_by_update[-1][0]


def get_bundle(filename):
    if 'dev' in filename:
        return 'com.appkode.utair.dev'
    elif 'alpha' in filename:
        return 'com.appkode.utair.alpha'
    else:
        return 'ru.utair.android'


def get_capabilities():
    recent_file = get_recent_file('/home/kode/android-ut-builds')
    full_path = '/home/kode/android-ut-builds/{}'.format(recent_file)
    desired_caps = {'platformName': 'Android', 'platformVersion': '7.0', 'app': PATH(full_path)}
    return desired_caps


def before_all(context):
    context.driver = webdriver.Remote('http://192.168.100.74:4723/wd/hub', get_capabilities())
    recent_file = get_recent_file('/home/kode/android-ut-builds')
    context.bundle = get_bundle(recent_file)


def after_all(context):
    context.driver.quit()
