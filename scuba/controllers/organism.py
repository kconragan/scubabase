import logging

from pylons import request, response, session
from pylons.templating import render_mako as render
from pylons import tmpl_context as c
from pylons.controllers.util import abort, redirect_to

import sys
import scuba.lib.helpers as h
import scuba.lib.metaweb as m

from scuba.lib.base import BaseController, render

log = logging.getLogger(__name__)

class OrganismController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        c.name = request.params.get('name', 'Visitor')
        return render('/organism.html')
        
    def view(self, id):
        """
        The primary view page for an organism
        """
        organism_guid = id

        credentials = m.login("kconragan", "dulcev1da")
        
        query = {
          "*" : None,
          "guid" : '#' + id,
          "type" : "/user/kconragan/scuba_diving/marine_creature",
          "/common/topic/article" : [{}],
          "/common/topic/image" : [{}]
        }
        
        
        c.content = m.read(query, credentials)
        
        related_query = [{
            "higher_classification" : c.content['higher_classification'],
            "name" : [],
            "guid" : None,
            "type" : "/biology/organism_classification"
        }]
        
        c.related = m.read(related_query, credentials)
        return render('/derived/organism/view.html')
        
        
        
    def environ(self):
        response.content_type = 'text/plain'
        return h.format_environ(request.environ)
