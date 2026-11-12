import unittest
from reference.flood_risk_analyzer import FloodRiskAnalyzer

class TestPartialDrainage(unittest.TestCase):
    def test_partial_drainage(self):
        analyzer = FloodRiskAnalyzer()
        data = {
            "location_id": "BAKU-105",
            "rainfall_mm": 0,
            "water_level_cm": 0,
            "drainage_status": "partial"
        }
        self.assertEqual(analyzer.analyze(data)["risk_score"], 10)

if __name__ == "__main__":
    unittest.main()
