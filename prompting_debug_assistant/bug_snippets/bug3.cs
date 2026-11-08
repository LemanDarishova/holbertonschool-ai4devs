using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public class FraudRule
{
    public string Name { get; set; }
    public bool IsBlocked { get; set; }
}

public class FraudDetectionService
{
    public async Task<bool> IsFraudDetected(
        List<FraudRule> rules)
    {
        foreach (var rule in rules)
        {
            await Task.Delay(100);

            if (rule.IsBlocked)
            {
                Console.WriteLine($"Fraud detected: {rule.Name}");
                return true;
            }

            return false;
        }

        return false;
    }
}
