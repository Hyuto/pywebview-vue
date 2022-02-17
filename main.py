import os
import time
import webview
import getpass

DEBUG = True
MAIN_DIR = os.path.join(".", "dist")


class API:
    def __init__(self):
        self.username = getpass.getuser()

    def GetUsername(self):
        return {"user": self.username}


def WebViewApp():
    template = os.path.join(MAIN_DIR, "index.html")

    if not os.path.isfile(template) and DEBUG:
        time.sleep(2.5)

    api = API()
    window = webview.create_window("pywebview-vue-app", template, js_api=api)
    webview.start(debug=DEBUG, http_server=True)


if __name__ == "__main__":
    WebViewApp()
