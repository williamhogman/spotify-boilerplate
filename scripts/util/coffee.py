from subprocess import Popen,PIPE


def coffee(data):
    p =Popen("coffee -s -p",
                       stdout=PIPE,stdin=PIPE,stderr=PIPE,shell=True)

    output = p.communicate(data)
    if output[1] != "":
        print("Error from CoffeeScript")
        print(output[1])
        raise RuntimeError("could not build CoffeeScript")

    return output[0]
    
