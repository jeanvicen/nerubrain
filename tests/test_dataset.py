import unittest
from nerubrain.dataset import standardized_url
class DatasetTests(unittest.TestCase):
    def test_standardized_url_uses_normalized_archive_and_escaped_name(self):
        self.assertEqual(standardized_url({"archive":"Allman Lab","neuron_name":"cell_a-1","species":"human"}), "https://neuromorpho.org/dableFiles/allman%20lab/CNG%20version/cell_a-1.CNG.swc")
    def test_reject_path_injection(self):
        with self.assertRaises(ValueError): standardized_url({"archive":"../bad","neuron_name":"neuron"})
