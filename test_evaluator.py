import unittest
from src.claim_verifiability.evaluator import evaluate_checks, MEP_ITEMS

class EvaluatorTests(unittest.TestCase):
    def test_complete_score(self):
        result = evaluate_checks([True] * len(MEP_ITEMS))
        self.assertEqual(result["score"], 100)
        self.assertEqual(result["missing"], [])

    def test_missing_items(self):
        checks = [True] * len(MEP_ITEMS)
        checks[0] = False
        result = evaluate_checks(checks)
        self.assertLess(result["score"], 100)
        self.assertEqual(len(result["missing"]), 1)

if __name__ == "__main__":
    unittest.main()
