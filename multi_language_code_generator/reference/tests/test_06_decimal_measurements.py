import unittest
from reference.flood_risk_analyzer import FloodRiskAnalyzer

class TestDecimalMeasurements(unittest.TestCase):
    def test_decimal_values(self):
        analyzer = FloodRiskAnalyzer()
        data = {
            "location_id": "BAKU-106",
            "rainfall_mm": 29.9,
            "water_level_cm": 24.9,
            "drainage_status": "good"
        }
        self.assertEqual(analyzer.analyze(data)["risk_score"], 35)

if __name__ == "__main__":
    unittest.main()
