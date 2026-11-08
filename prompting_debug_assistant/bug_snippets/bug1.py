import time

class PaymentProcessor:
    TIMEOUT = 30

    def process_payment(self, amount):
        start_time = time.time()

        self.validate_payment(amount)
        self.check_fraud_rules(amount)
        result = self.call_payment_gateway(amount)
        self.update_transaction(result)
        self.send_notifications(result)

        elapsed = time.time() - start_time

        if elapsed > self.TIMEOUT:
            raise TimeoutError("transaction_timeout")

        return result

    def validate_payment(self, amount):
        time.sleep(0.2)

    def check_fraud_rules(self, amount):
        time.sleep(5)

    def call_payment_gateway(self, amount):
        time.sleep(10)
        return "SUCCESS"

    def update_transaction(self, result):
        time.sleep(0.5)

    def send_notifications(self, result):
        time.sleep(15)
