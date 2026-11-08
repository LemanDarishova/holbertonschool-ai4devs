using System;
using System.Threading.Tasks;

public class NotificationService
{
    public async Task SendNotifications(string email, string transactionId)
    {
        await SendUserEmail(email);

        await SendMerchantWebhook(transactionId);

        await UpdateAnalytics(transactionId);

        Console.WriteLine("All notifications completed.");
    }

    private async Task SendUserEmail(string email)
    {
        await Task.Delay(5000);
        Console.WriteLine($"Email sent to {email}");
    }

    private async Task SendMerchantWebhook(string transactionId)
    {
        await Task.Delay(8000);
        Console.WriteLine($"Webhook sent: {transactionId}");
    }

    private async Task UpdateAnalytics(string transactionId)
    {
        await Task.Delay(2000);
        Console.WriteLine($"Analytics updated: {transactionId}");
    }
}
