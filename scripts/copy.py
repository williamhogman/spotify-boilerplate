#!/usr/bin/env python
import util

import shutil
import os

if __name__ == '__main__':
    manifest = util.load_manifest("manifest.yaml")
    path = os.path.expanduser("~/Spotify/{}/".format(manifest["AppName"]["en"].lower()))

    try:
        shutil.rmtree(path)
    except OSError:
        pass

    print("Copying {}".format(path))
    shutil.copytree("build",path)
    
    
