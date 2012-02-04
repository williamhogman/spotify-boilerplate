import yaml
import os.path as path

def smartpath(p):
    return path.abspath(path.expanduser(p))

def load_manifest(p):
    if path.isdir(p):
        p = path.join(p,"manifest.yaml")
    return yaml.load(open(p))
        
        
