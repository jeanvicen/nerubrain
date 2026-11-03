import io, math, unittest
from nerubrain.swc import parse_swc, summarize
VALID="# simple fixture\n1 1 0 0 0 1 -1\n2 3 3 0 0 0.5 1\n3 3 3 4 0 0.5 2\n4 3 3 0 12 0.5 2\n"
class SWCTests(unittest.TestCase):
    def test_parse_and_summary(self):
        m=parse_swc(io.StringIO(VALID)); s=summarize(m)
        self.assertEqual(len(m.nodes),4); self.assertEqual(m.comments,("simple fixture",))
        self.assertEqual(s["root_count"],1); self.assertEqual(s["branch_point_count"],1); self.assertEqual(s["terminal_count"],2)
        self.assertTrue(math.isclose(s["total_path_length"],19.0)); self.assertEqual(s["bounding_box"]["z"],[0.0,12.0])
    def test_reject_bad_columns(self):
        with self.assertRaisesRegex(ValueError,"7 SWC columns"): parse_swc(["1 1 0 0 0 -1\n"])
    def test_reject_missing_parent(self):
        with self.assertRaisesRegex(ValueError,"missing parent"): parse_swc(["1 1 0 0 0 1 -1\n", "2 3 0 0 0 1 8\n"])
    def test_reject_duplicate_and_invalid_radius(self):
        with self.assertRaisesRegex(ValueError,"unique"): parse_swc(["1 1 0 0 0 1 -1\n","1 2 0 0 0 1 1\n"])
        with self.assertRaisesRegex(ValueError,"radius"): parse_swc(["1 1 0 0 0 -1 -1\n"])
    def test_reject_empty(self):
        with self.assertRaisesRegex(ValueError,"no nodes"): parse_swc([])
