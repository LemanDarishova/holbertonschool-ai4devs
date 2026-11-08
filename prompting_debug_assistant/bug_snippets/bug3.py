import time

class FraudDetectionService:
    def is_fraud_detected(self, rules):
        for rule in rules:
            time.sleep(0.1)

            if rule["is_blocked"]:
                print(f"Fraud detected: {rule['name']}")
                return True

            return False

        return False


rules = [
    {"name": "Low Risk", "is_blocked": False},
    {"name": "Suspicious Activity", "is_blocked": True}
]

service = FraudDetectionService()
print(service.is_fraud_detected(rules))
