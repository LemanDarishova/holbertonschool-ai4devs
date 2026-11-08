using System;
using System.Diagnostics;
using System.Threading.Tasks;

public class PaymentProcessor
{
    private const int Timeout = 30000;

    public async Task<string> ProcessPayment(decimal amount)
    {
        var stopwatch = Stopwatch.StartNew();

        await ValidatePayment(amount);
        await CheckFraudRules(amount);
        var result = await CallPaymentGateway(amount);
        await UpdateTransaction(result);
        await SendNotifications(result);

        stopwatch.Stop();

        if (stopwatch.ElapsedMilliseconds > Timeout)
        {
            throw new TimeoutException("transaction_timeout");
        }

        return result;
    }

    private async Task ValidatePayment(decimal amount) =>
        await Task.Delay(200);

    private async Task CheckFraudRules(decimal amount) =>
        await Task.Delay(5000);

    private async Task<string> CallPaymentGateway(decimal amount)
    {
        await Task.Delay(10000);
        return "SUCCESS";
    }

    private async Task UpdateTransaction(string result) =>
        await Task.Delay(500);

    private async Task SendNotifications(string result) =>
        await Task.Delay(15000);
}
