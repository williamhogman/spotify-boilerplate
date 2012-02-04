#!/usr/bin/env python
import util

import os
import sys


if __name__ == '__main__':
    manifest = util.load_yaml("manifest.yaml")
    
    name = manifest["AppName"]["en"]

    url = "spotify:app:{}".format(name)
    cf = "open {}" if sys.platform == "darwin" else "xdg-open {}"
    os.system(cf.format(url))
