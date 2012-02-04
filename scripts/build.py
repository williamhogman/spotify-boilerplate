#!/usr/bin/env python
import util
import yaml
import shutil
import argparse
import os
import os.path as path
from functools import partial

def build_application(opt):
    """ Builds the application """
    basedir = util.smartpath(opt.appdir)
    projpath = partial(path.join,basedir)
    bld = projpath("build")
    buildpath = partial(path.join,bld)

    if path.exists(bld):
        print("removing build dir")
        shutil.rmtree(bld)
        os.mkdir(bld)
        
    if not path.isdir(basedir):
        raise BuildFailedError("Could not find the project dir") 

    manifest_file = projpath("manifest.yaml")

    if not path.isfile(manifest_file):
        raise BuildFailedError("Could not find manifest file") 

    manifest = util.load_manifest(manifest_file)
    
    tr = util.TemplateRenderer()
    tr.add(manifest)

    for filename in source_files(basedir):
        # WAT? - something.HtMl -> [something, .HtMl] -> "html"
        ext = path.splitext(filename)[1][1:].lower()
        
        with open(projpath(filename)) as f:
                data = f.read()
        if ext == "html":
            write_file(buildpath(filename),tr.render(data))
            print("[*] Rendered template {}".format(filename))
        else:
            write_file(buildpath(filename),data)            
            print("[*] Copied {}".format(filename))
        

def write_file(filename,data):
    try:
        os.makedirs(path.dirname(filename))
    except OSError:
        pass
    with open(filename,"w") as f:
        f.write(data)
        
def source_files(basedir):
    for root,dirs,files in os.walk(basedir,topdown=True):
        # scripts is where the build scripts are located
        def rem(col,i):
            if i in col: col.remove(i)
        remd,remf = partial(rem,dirs),partial(rem,files)
        map(remd,["scripts","build"])
        map(remf,["README.md","README","LICENCE"])
        if "manifest.yaml" in files:
            files.remove("manifest.yaml")
            
        # remove dotdirs and dirs
        def remove_dotf(col):
            [col.remove(i) for i in col if i[0] == "."]
        
        remove_dotf(dirs)
        remove_dotf(files)

        for f in files:
            yield path.relpath(path.join(root,f),start=basedir)
            
    
class BuildFailedError(RuntimeError):
    """ Raised if a critical failure occurs in the build process """

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build your app')
    
    parser.add_argument('appdir',nargs="?",default="./",
                        help="the directory from which to build the application")

    try:
        build_application(parser.parse_args())
    except BuildFailedError as e:
        print("Build failed: {}".format(e))
    else:
        print("Build complete")
