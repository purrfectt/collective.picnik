import unittest2 as unittest
from zope import interface
from plone.app import testing
from collective.picnik.tests import layer
from collective.picnik.tests import utils

class UnitTestCase(unittest.TestCase):
    
    def setUp(self):
        from ZPublisher.tests.testPublish import Request
        from zope.annotation.interfaces import IAttributeAnnotatable
        self.context = utils.FakeContext()
        self.request = utils.FakeRequest()
        super(UnitTestCase, self).setUp()

class IntegrationTestCase(unittest.TestCase):

    layer = layer.INTEGRATION

    def setUp(self):
        from zope.annotation.interfaces import IAttributeAnnotatable
        from collective.picnik.interfaces import IPicnikLayer
        interface.alsoProvides(self.layer['request'],
                               (IAttributeAnnotatable,IPicnikLayer))
        super(IntegrationTestCase, self).setUp()
        self.portal = self.layer['portal']
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

class FunctionalTestCase(unittest.TestCase):

    layer = layer.FUNCTIONAL

    def setUp(self):
        from zope.annotation.interfaces import IAttributeAnnotatable
        from collective.gallery.interfaces import IPicnikLayer
        interface.alsoProvides(self.layer['request'],
                               (IAttributeAnnotatable,IPicnikLayer))
        self.portal = self.layer['portal']
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        testing.setRoles(self.portal, testing.TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']

def build_test_suite(test_classes):
    suite = unittest.TestSuite()
    for klass in test_classes:
        suite.addTest(unittest.makeSuite(klass))
    return suite
