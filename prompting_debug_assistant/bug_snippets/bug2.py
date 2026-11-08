import time

class NotificationService:
    def send_email(self, email):
        time.sleep(5)
        print(f"Email sent to {email}")

    def send_webhook(self, transaction_id):
        time.sleep(8)
        print(f"Webhook sent: {transaction_id}")

    def update_analytics(self, transaction_id):
        time.sleep(2)
        print("Analytics updated")

    def send_notifications(self, email, transaction_id):
        self.send_email(email)
        self.send_webhook(transaction_id)
        self.update_analytics(transaction_id)

        print("All notifications completed.")
