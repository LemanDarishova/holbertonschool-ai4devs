import unittest
from reference.flood_risk_analyzer import FloodRiskAnalyzer

class TestBooleanMeasurement(unittest.TestCase):
    def test_boolean_water_level(self):
        analyzer = FloodRiskAnalyzer()
        data = {
            "location_id": "BAKU-108",
            "rainfall_mm": 20,
            "water_level_cm": True,
            "drainage_status": "good"
        }
        self.assertEqual(
            analyzer.analyze(data),
            {"error": "Invalid input"}
        )

if __name__ == "__main__":
    unittest.main()
