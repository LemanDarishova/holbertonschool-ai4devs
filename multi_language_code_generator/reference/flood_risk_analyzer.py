import math
class FloodRiskAnalyzer:

    DRAINAGE_POINTS = {
        "good": 0,
        "partial": 10,
        "blocked": 25
    }

    @staticmethod
    def calculate_rainfall_points(rainfall_mm):
        if rainfall_mm < 15:
            return 0
        elif rainfall_mm < 30:
            return 15
        elif rainfall_mm < 50:
            return 30
        return 45

    @staticmethod
    def calculate_water_points(water_level_cm):
        if water_level_cm < 10:
            return 0
        elif water_level_cm < 25:
            return 20
        elif water_level_cm < 50:
            return 40
        return 60

    @staticmethod
    def validate_input(data):
        if not isinstance(data, dict):
            return False

        required_fields = [
            "location_id",
            "rainfall_mm",
            "water_level_cm",
            "drainage_status"
        ]

        if not all(field in data for field in required_fields):
            return False

        location_id = data["location_id"]
        rainfall = data["rainfall_mm"]
        water_level = data["water_level_cm"]
        drainage = data["drainage_status"]

        if not isinstance(location_id, str) or not location_id.strip():
            return False

        for value in [rainfall, water_level]:
            if isinstance(value, bool):
                return False

            if not isinstance(value, (int, float)):
                return False

            if not math.isfinite(value) or value < 0:
                return False

        if drainage not in FloodRiskAnalyzer.DRAINAGE_POINTS:
            return False

        return True

    def analyze(self, data):
        if not self.validate_input(data):
            return {"error": "Invalid input"}

        rainfall_points = self.calculate_rainfall_points(
            data["rainfall_mm"]
        )

        water_points = self.calculate_water_points(
            data["water_level_cm"]
        )

        drainage_points = self.DRAINAGE_POINTS[
            data["drainage_status"]
        ]

        score = min(
            100,
            rainfall_points + water_points + drainage_points
        )

        if score <= 29:
            risk_level = "Low"
        elif score <= 59:
            risk_level = "Medium"
        else:
            risk_level = "High"

        return {
            "location_id": data["location_id"],
            "risk_score": score,
            "risk_level": risk_level
        }
