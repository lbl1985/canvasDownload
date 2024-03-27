import sys, os, unittest
repo_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src')
sys.path.append(repo_root)
from get_video_download_link import get_video_download_link

class UtilTest(unittest.TestCase):
    def setUp(self):
        pass
            
    def tearDown(self):
        """tear down the test"""
        pass
    

    def test_get_video_download_link(self):
        """
        test for get_video_download_link
        """
        self.assertEqual('https://cdnapisec.kaltura.com/p/1329972/sp/132997200/playManifest/entryId/1_jokxyduz/format/download/protocol/https/flavorParamIds/0', 
                         get_video_download_link(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'Project-Management-Module7_files', 'saved_resource(1).html')
                            ) 
                         )