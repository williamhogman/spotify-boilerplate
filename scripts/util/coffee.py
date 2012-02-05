from subprocess import Popen,PIPE
from util.exc import BuildFailedError


def coffee(data):
    
    p =Popen("coffee -s -p",stdout=PIPE,stdin=PIPE,
             stderr=PIPE,shell=True)

    output = p.communicate(data)
    if output[1] != "":
        raise BuildFailedError("CoffeeScript failed",output[1])

    return output[0]
    
