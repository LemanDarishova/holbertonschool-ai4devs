
import unittest

from reference.flood_risk_analyzer import FloodRiskAnalyzer


class TestFloodRiskAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = FloodRiskAnalyzer()

    def test_low_risk(self):
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
        self.assertEqual(self.analyzer.analyze(data), expected)

    def test_medium_risk(self):
        data = {
            "location_id": "BAKU-002",
            "rainfall_mm": 20,
            "water_level_cm": 12,
            "drainage_status": "good"
        }
        expected = {
            "location_id": "BAKU-002",
            "risk_score": 35,
            "risk_level": "Medium"
        }
        self.assertEqual(self.analyzer.analyze(data), expected)

    def test_high_risk(self):
        data = {
            "location_id": "BAKU-003",
            "rainfall_mm": 35,
            "water_level_cm": 28,
            "drainage_status": "partial"
        }
        expected = {
            "location_id": "BAKU-003",
            "risk_score": 80,
            "risk_level": "High"
        }
        self.assertEqual(self.analyzer.analyze(data), expected)

    def test_score_cap(self):
        data = {
            "location_id": "BAKU-004",
            "rainfall_mm": 70,
            "water_level_cm": 80,
            "drainage_status": "blocked"
        }
        self.assertEqual(
            self.analyzer.analyze(data)["risk_score"], 100
        )

    def test_exact_rainfall_threshold(self):
        data = {
            "location_id": "BAKU-005",
            "rainfall_mm": 30,
            "water_level_cm": 0,
            "drainage_status": "good"
        }
        self.assertEqual(
            self.analyzer.analyze(data)["risk_score"], 30
        )

    def test_negative_value(self):
        data = {
            "location_id": "BAKU-006",
            "rainfall_mm": -1,
            "water_level_cm": 10,
            "drainage_status": "good"
        }
        self.assertEqual(
            self.analyzer.analyze(data),
            {"error": "Invalid input"}
        )

    def test_missing_field(self):
        data = {
            "location_id": "BAKU-007",
            "rainfall_mm": 10,
            "water_level_cm": 15
        }
        self.assertEqual(
            self.analyzer.analyze(data),
            {"error": "Invalid input"}
        )

    def test_numeric_string(self):
        data = {
            "location_id": "BAKU-008",
            "rainfall_mm": "40",
            "water_level_cm": 25,
            "drainage_status": "blocked"
        }
        self.assertEqual(
            self.analyzer.analyze(data),
            {"error": "Invalid input"}
        )

    def test_zero_values_with_blocked_drainage(self):
        data = {
            "location_id": "BAKU-009",
            "rainfall_mm": 0,
            "water_level_cm": 0,
            "drainage_status": "blocked"
        }
        expected = {
            "location_id": "BAKU-009",
            "risk_score": 25,
            "risk_level": "Low"
        }
        self.assertEqual(self.analyzer.analyze(data), expected)

    def test_boolean_as_number(self):
        data = {
            "location_id": "BAKU-010",
            "rainfall_mm": True,
            "water_level_cm": 10,
            "drainage_status": "good"
        }
        self.assertEqual(
            self.analyzer.analyze(data),
            {"error": "Invalid input"}
        )

    def test_invalid_drainage_status(self):
        data = {
            "location_id": "BAKU-011",
            "rainfall_mm": 20,
            "water_level_cm": 10,
            "drainage_status": "GOOD"
        }
        self.assertEqual(
            self.analyzer.analyze(data),
            {"error": "Invalid input"}
        )

    def test_whitespace_location_id(self):
        data = {
            "location_id": "   ",
            "rainfall_mm": 20,
            "water_level_cm": 10,
            "drainage_status": "good"
        }
        self.assertEqual(
            self.analyzer.analyze(data),
            {"error": "Invalid input"}
        )

    def test_decimal_values(self):
        data = {
            "location_id": "BAKU-012",
            "rainfall_mm": 15.5,
            "water_level_cm": 10.5,
            "drainage_status": "good"
        }
        expected = {
            "location_id": "BAKU-012",
            "risk_score": 35,
            "risk_level": "Medium"
        }
        self.assertEqual(self.analyzer.analyze(data), expected)

    def test_infinity_value(self):
        data = {
            "location_id": "BAKU-013",
            "rainfall_mm": float("inf"),
            "water_level_cm": 10,
            "drainage_status": "good"
        }
        self.assertEqual(
            self.analyzer.analyze(data),
            {"error": "Invalid input"}
        )

    def test_nan_value(self):
        data = {
            "location_id": "BAKU-014",
            "rainfall_mm": float("nan"),
            "water_level_cm": 10,
            "drainage_status": "good"
        }
        self.assertEqual(
            self.analyzer.analyze(data),
            {"error": "Invalid input"}
        )


if __name__ == "__main__":
    unittest.main()
