using System;

class Program
{
    static void PrintNumbers(int[] numbers)
    {
        for (int i = 0; i <= numbers.Length; i++)
        {
            Console.WriteLine(numbers[i]);
        }
    }

    static void Main()
    {
        int[] values = { 10, 20, 30, 40, 50 };

        PrintNumbers(values);
    }
}
