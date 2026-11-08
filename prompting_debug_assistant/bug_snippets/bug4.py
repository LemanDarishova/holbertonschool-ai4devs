import time

class PaymentRetryService:
    RETRY_LIMIT = 3

    def process_payment(self, amount):
        for attempt in range(self.RETRY_LIMIT):
            try:
                return self.call_payment_gateway(amount)
            except TimeoutError:
                print(f"Retry attempt: {attempt + 1}")

        raise Exception("Payment failed after retries.")

    def call_payment_gateway(self, amount):
        time.sleep(1)

        # Payment succeeds, but response times out.
        print(f"Payment of {amount} processed successfully.")
        raise TimeoutError("Gateway response timeout")


service = PaymentRetryService()
service.process_payment(100)
