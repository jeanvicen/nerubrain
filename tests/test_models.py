import unittest
from nerubrain.networks.model import Population, Projection, validate_projection
from nerubrain.simulation.base import RunConfig
from nerubrain.io.provenance import sha256_file
from nerubrain.neurons.validation import validate_morphology
from nerubrain.swc import parse_swc
class ModelTests(unittest.TestCase):
    def test_population_projection_and_endpoints(self):
        cells={"a":Population("a",2,"pyramidal"),"b":Population("b",1,"interneuron")}
        validate_projection(Projection("p","a","b"),cells)
        with self.assertRaisesRegex(ValueError,"unknown"): validate_projection(Projection("p","a","x"),cells)
    def test_run_config_requires_positive_steps(self):
        with self.assertRaises(ValueError): RunConfig(0,0.1)
    def test_structural_report_and_hash(self):
        m=parse_swc(["1 1 0 0 0 1 -1\n"])
        self.assertTrue(validate_morphology(m).valid)
        self.assertEqual(len(sha256_file("data/raw/02a_pyramidal2aFI.CNG.swc")),64)
