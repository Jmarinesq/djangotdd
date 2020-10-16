import os


chromedriver_path = "/Users/A187AG/Desktop/knwldg/Programming/djangoTDD/chromedriver"

def set_env_vars():
    os.environ["PATH"] = os.environ["PATH"] + ":/Users/A187AG/Desktop/knwldg/Programming/djangoTDD"
    os.environ["DJANGO_SETTINGS_MODULE"] = "superlists.settings"
