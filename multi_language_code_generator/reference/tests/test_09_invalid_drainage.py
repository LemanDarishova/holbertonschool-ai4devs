import unittest
from reference.flood_risk_analyzer import FloodRiskAnalyzer

class TestInvalidDrainage(unittest.TestCase):
    def test_unknown_drainage(self):
        analyzer = FloodRiskAnalyzer()
        data = {
            "location_id": "BAKU-109",
            "rainfall_mm": 20,
            "water_level_cm": 10,
            "drainage_status": "unknown"
        }
        self.assertEqual(
            analyzer.analyze(data),
            {"error": "Invalid input"}
        )

if __name__ == "__main__":
    unittest.main()
