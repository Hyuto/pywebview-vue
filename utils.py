import os
import sys
import argparse
from pathlib import Path


def no_cache():
    """Set no caching in Webview"""
    wsgi = Path(os.path.join(".", "webview-env", "Lib", "site-packages", "webview", "wsgi.py"))
    wsgi.write_text(wsgi.read_text().replace(r"'max-age={}'.format(self.max_age)", "'no-store'"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Utils script")
    parser.add_argument("-nc", "--no-cache", help="Set no caching in Webview", action="store_true")

    args = parser.parse_args()

    if args.no_cache:
        no_cache()
