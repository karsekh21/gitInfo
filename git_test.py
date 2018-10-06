import unittest
from unittest import mock
from unittest.mock import Mock
from gitStuff import gitHubStuff

class DummyObject(object):
    def __init__(self, content):
        self.content = content

class testGitAPI(unittest.TestCase):
        
    @mock.patch('requests.get')
    def testValidInput1(self, mockedReqs):
        mockedResponses = [0, 0, 0]
        mockedResponses[0] = DummyObject(b'[{"id" : "32808844", "name" : "test1"}, {"id" : "32816276", "name" : "test2"}]')
        mockedResponses[1] = DummyObject(b'[{"author": "jrr"}, {"author": "jrr"}, {"author": "jrr"}]')
        mockedResponses[2] = DummyObject(b'[{"author": "jrr"}, {"author": "jrr"}]')
        
        
        mockedReqs.side_effect = mockedResponses
        self.assertEqual(gitHubStuff("bsb226"), [['test1', 3], ['test2', 2]] )=

        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)
