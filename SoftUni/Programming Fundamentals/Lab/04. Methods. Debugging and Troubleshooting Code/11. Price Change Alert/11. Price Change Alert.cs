using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        double threshold = double.Parse(Console.ReadLine());
        double previousPrice = double.Parse(Console.ReadLine());

        for (int i = 0; i < n - 1; i++)
        {
            double price = double.Parse(Console.ReadLine());
            double difference = Difference(previousPrice, price); bool isSignificantDifference = IsThereDiff(difference, threshold);
            string message = GetChangeMessage(price, previousPrice, difference, isSignificantDifference);
            Console.WriteLine(message);
            previousPrice = price;
        }
    }

    private static string GetChangeMessage(double price, double previousPrice, double difference, bool isSignificantDifference)
    {
        string result = "";
        if (difference == 0)
        {
            result = string.Format("NO CHANGE: {0}", price);
        }
        else if (!isSignificantDifference)
        {
            result = string.Format("MINOR CHANGE: {0} to {1} ({2:F2}%)", previousPrice, price, difference * 100);
        }
        else if (isSignificantDifference && (difference > 0))
        {
            result = string.Format("PRICE UP: {0} to {1} ({2:F2}%)", previousPrice, price, difference * 100);
        }
        else if (isSignificantDifference && (difference < 0))
            result = string.Format("PRICE DOWN: {0} to {1} ({2:F2}%)", previousPrice, price, difference * 100);
        return result;
    }

    private static bool IsThereDiff(double difference, double isDiff)
    {
        if (Math.Abs(difference) >= isDiff)
        {
            return true;
        }
        return false;
    }

    private static double Difference(double previousPrice, double price)
    {
        return (price - previousPrice) / previousPrice;
    }
}
