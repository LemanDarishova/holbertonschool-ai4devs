using System;
using System.Threading.Tasks;

public class PaymentRetryService
{
    private const int RetryLimit = 3;

    public async Task<string> ProcessPayment(decimal amount)
    {
        for (int attempt = 1; attempt <= RetryLimit; attempt++)
        {
            try
            {
                return await CallPaymentGateway(amount);
            }
            catch (TimeoutException)
            {
                Console.WriteLine($"Retry attempt: {attempt}");
            }
        }

        throw new Exception("Payment failed after retries.");
    }

    private async Task<string> CallPaymentGateway(decimal amount)
    {
        await Task.Delay(1000);

        // Payment may succeed even if the client times out.
        throw new TimeoutException("Gateway response timeout");
    }
}
