import os
import sys
import time
import webview
import getpass

DEBUG = True

# Template directory
if sys.flags.dev_mode:
    MAIN_DIR = os.path.join("..", "dist")  # development
else:
    MAIN_DIR = os.path.join(".", "dist")  # production


def wait_template(template):
    """Wait template on first launch at development phase"""
    print("Waiting on template folder to be exist")
    while not os.path.exists(template):
        time.sleep(0.5)


class API:
    def __init__(self):
        self.username = getpass.getuser()

    def GetUsername(self):
        return {"user": self.username}


def WebViewApp():
    template = os.path.join(MAIN_DIR, "index.html")

    # Development stage
    if sys.flags.dev_mode:
        # Please don't delete code bellow
        # Wait template on first launch
        wait_template(template=os.path.join(os.path.dirname(__file__), "..", "dist"))

    api = API()
    window = webview.create_window("pywebview-vue-app", template, js_api=api)
    webview.start(debug=DEBUG, http_server=True)


if __name__ == "__main__":
    WebViewApp()
