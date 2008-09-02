"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to both as 'h'.
"""
# Import helpers as desired, or define your own, ie:
# from webhelpers.html.tags import checkbox, password

from routes import url_for
import string

def format_environ(environ):
    results = []
    keys = environ.keys()
    keys.sort()
    for key in keys:
        results.append("%s: %r"%(key, environ[key]))
    return '\n'.join(results)
    
def format_guid(guid):
    """
    A helper function for creating view urls
    """
    # Strip hash from guid for url parsing
    guid = guid.strip('#')
    
    #Construct url
    view_url = '/organism/view/' +  guid  
    return view_url