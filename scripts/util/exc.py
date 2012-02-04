
class BuildFailedError(RuntimeError):
    """ Raised if a critical failure occurs in the build process """
    def __init__(self,message="",longmsg=""):
        self.longmsg = longmsg
        super(RuntimeError).__init__(message)
