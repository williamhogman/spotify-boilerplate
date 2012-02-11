from mako.template import Template

class TemplateRenderer(object):
    """ Class for interfacing with templates """
    def __init__(self):
        self.context = {}
        self._add_fn(self.local_file)
        self._add_fn(self.app_url)
            
    def _add_fn(self,fn):
        self.context[fn.__name__] = fn
        
    def add(self,obj):
        """ adds a dict to the context"""
        self.context.update(obj)

    def render(self,template):
        """ Renders the template using the current context"""
        return Template(template).render(**self.context)
    
    @property
    def app_id(self):
        return self.context["AppName"]["en"].lower()

    def app_url(self,link=None):
        if link is None:
            return "sp:{}".format(self.app_id)
        else: 
            return "sp:{}:{}".format(self.app_id,link)
            
    def local_file(self,name):
        return "sp://{}/{}".format(self.app_id,name)
        

