from scuba.tests import *

class TestOrganismController(TestController):

    def test_index(self):
        response = self.app.get(url_for(controller='organism'))
        # Test response...
