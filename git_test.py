import unittest
from unittest import mock
from unittest.mock import Mock
from gitStuff import gitHubStuff

class s(object):
    def __init__(self, content):
        self.content = content

class test_git(unittest.TestCase):
        
    @mock.patch('requests.get')
    def testValidInput1(self, mockedReqs):
        mockedResponses = [0, 0, 0]
        mockedResponses[0] = s(b'[{"karsekh21" : "32808844", "SSW315" : "Java"}, {"karsekh21" : "32816276", "SSW555Agile" : "Java2"}]')
        mockedResponses[1] = s(b'[{"mark": "something"}, {"jeff": "something"}, {"kyle": "something"}]')
        mockedResponses[2] = s(b'[{"chris": "something"}, {"chris": "something"}]')
        
        
        mockedReqs.side_effect = mockedResponses
        self.assertEqual(getGitHubInfo("karsekh21"), [['Java', 3], ['Java2', 2]] )
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)