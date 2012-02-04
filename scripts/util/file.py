import yaml
import os
import os.path as path

def smartpath(p):
    return path.abspath(path.expanduser(p))

def load_manifest(p):
    if path.isdir(p):
        p = path.join(p,"manifest.yaml")
    return yaml.load(open(p))
        
def write_file(filename,data):
    try:
        os.makedirs(path.dirname(filename))
    except OSError:
        pass
    with open(filename,"w") as f:
        f.write(data)
