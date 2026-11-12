import unittest
from reference.flood_risk_analyzer import FloodRiskAnalyzer

class TestWaterLevelBoundary(unittest.TestCase):
    def test_water_level_25(self):
        analyzer = FloodRiskAnalyzer()
        data = {
            "location_id": "BAKU-103",
            "rainfall_mm": 0,
            "water_level_cm": 25,
            "drainage_status": "good"
        }
        self.assertEqual(analyzer.analyze(data)["risk_score"], 40)

if __name__ == "__main__":
    unittest.main()
