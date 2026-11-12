import unittest
from reference.flood_risk_analyzer import FloodRiskAnalyzer

class TestEmptyLocation(unittest.TestCase):
    def test_empty_location_id(self):
        analyzer = FloodRiskAnalyzer()
        data = {
            "location_id": "",
            "rainfall_mm": 20,
            "water_level_cm": 10,
            "drainage_status": "good"
        }
        self.assertEqual(
            analyzer.analyze(data),
            {"error": "Invalid input"}
        )

if __name__ == "__main__":
    unittest.main()
