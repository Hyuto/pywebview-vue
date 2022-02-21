import os
import sys
import webview
import getpass

DEBUG = True

# Template directory
if sys.flags.dev_mode:
    MAIN_DIR = os.path.join("..", "dist")  # development
else:
    MAIN_DIR = os.path.join(".", "dist")  # production


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
        import time

        def wait_template(template):
            while not os.path.exists(template):
                time.sleep(0.5)

        print("Waiting on template folder to be exist")
        wait_template(template=os.path.join(os.path.dirname(__file__), "..", "dist"))

    api = API()
    window = webview.create_window("pywebview-vue-app", template, js_api=api)
    webview.start(debug=DEBUG, http_server=True)


if __name__ == "__main__":
    WebViewApp()
