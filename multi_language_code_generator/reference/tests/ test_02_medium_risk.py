import unittest
from reference.flood_risk_analyzer import FloodRiskAnalyzer


class TestLowRisk(unittest.TestCase):

    def test_low_risk(self):
        analyzer = FloodRiskAnalyzer()

        data = {
            "location_id": "BAKU-001",
            "rainfall_mm": 5,
            "water_level_cm": 2,
            "drainage_status": "good"
        }

        expected = {
            "location_id": "BAKU-001",
            "risk_score": 0,
            "risk_level": "Low"
        }

        self.assertEqual(analyzer.analyze(data), expected)
