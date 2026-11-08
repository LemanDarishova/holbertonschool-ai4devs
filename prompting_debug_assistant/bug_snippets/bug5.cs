using System;
using System.Threading.Tasks;

public class PaymentResult
{
    public string TransactionId { get; set; }
    public string Status { get; set; }
}

public class PaymentGatewayService
{
    public async Task<string> ProcessPayment(decimal amount)
    {
        PaymentResult result = await CallGateway(amount);

        if (result.Status == "SUCCESS")
        {
            await SaveTransaction(result.TransactionId);
            return result.TransactionId;
        }

        throw new Exception("Payment was rejected.");
    }

    private async Task<PaymentResult> CallGateway(decimal amount)
    {
        await Task.Delay(500);
        return null;
    }

    private async Task SaveTransaction(string transactionId)
    {
        await Task.Delay(200);
    }
}
