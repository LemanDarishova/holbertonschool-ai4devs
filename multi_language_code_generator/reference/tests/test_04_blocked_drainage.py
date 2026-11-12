import unittest
from reference.flood_risk_analyzer import FloodRiskAnalyzer

class TestBlockedDrainage(unittest.TestCase):
    def test_blocked_drainage(self):
        analyzer = FloodRiskAnalyzer()
        data = {
            "location_id": "BAKU-104",
            "rainfall_mm": 0,
            "water_level_cm": 0,
            "drainage_status": "blocked"
        }
        self.assertEqual(analyzer.analyze(data)["risk_score"], 25)

if __name__ == "__main__":
    unittest.main()
