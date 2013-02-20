import unittest

from django.core.urlresolvers import reverse
from django_selenium.livetestcases import SeleniumLiveTestCase
from django_selenium.testcases import SeleniumElement


class SimpleUnitTests(unittest.TestCase):

    def test_multiple_elements(self):
        test_list = ['one string', 'another string']
        se = SeleniumElement(test_list)
        self.assertEquals(se.replace('one', 'two'), 'two string')
        for i, elem in enumerate(se):
            self.assertEquals(elem, test_list[i])


class MyTestCase(SeleniumLiveTestCase):

    def test_home(self):
        self.driver.open_url(reverse('main'))
        self.assertEquals(self.driver.get_title(), 'Sample Test Page')
        self.driver.type_in('input#id_query', 'search something')
        self.driver.click('.form-search button[type="submit"]')

        self.assertEquals(self.driver.get_text('#success'), 'SUCCESS')
