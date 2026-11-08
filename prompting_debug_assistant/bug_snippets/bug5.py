import time

class PaymentGatewayService:
    def process_payment(self, amount):
        result = self.call_gateway(amount)

        if result["status"] == "SUCCESS":
            self.save_transaction(result["transaction_id"])
            return result["transaction_id"]

        raise Exception("Payment was rejected.")

    def call_gateway(self, amount):
        time.sleep(0.5)
        return None

    def save_transaction(self, transaction_id):
        print(f"Transaction saved: {transaction_id}")


service = PaymentGatewayService()
service.process_payment(100)
