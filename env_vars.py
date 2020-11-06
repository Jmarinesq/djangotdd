import os



def set_env_vars():
    chromedriver_path = os.environ['CHROMEDRIVER_PATH']
    if not chromedriver_path:
        chromedriver_path = "/Users/A187AG/Desktop/knwldg/Programming/djangoTDD/chromedriver"
        os.environ["PATH"] = os.environ["PATH"] + ":/Users/A187AG/Desktop/knwldg/Programming/djangoTDD"
    else:
        os.environ["PATH"] = os.environ["PATH"] + ":/usr/bin/"
    os.environ["DJANGO_SETTINGS_MODULE"] = "superlists.settings"
