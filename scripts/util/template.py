from mako.template import Template

class TemplateRenderer(object):
    """ Class for interfacing with templates """
    def __init__(self):
        self.context = {}
        self._add_fn(self.local_file)
            
    def _add_fn(self,fn):
        self.context[fn.__name__] = fn
        
    def add(self,obj):
        """ adds a dict to the context"""
        self.context.update(obj)

    def render(self,template):
        """ Renders the template using the current context"""
        return Template(template).render(**self.context)
        
    def local_file(self,name):
        return "sp://{}/{}".format(self.context["AppName"]["en"].lower(),name)
        

