using System;

public class Bug4Fixed
{
    // Return true when the password has at least 8 characters
    // and contains at least one digit.
    public static bool IsValidPassword(string password)
    {
        if (password == null)
            return false;

        bool hasDigit = false;

        foreach (char character in password)
        {
            if (char.IsDigit(character))
                hasDigit = true;
        }

        return password.Length >= 8 && hasDigit;
    }

    public static void Main()
    {
        Console.WriteLine(IsValidPassword("hello123")); // Expected: True
    }
}
