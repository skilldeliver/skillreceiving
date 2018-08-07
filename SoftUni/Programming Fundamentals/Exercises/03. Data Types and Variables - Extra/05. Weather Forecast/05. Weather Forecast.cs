using System;

namespace _05._Weather_Forecast
{
    class Program
    {
        static void Main(string[] args)
        {
            string n = Console.ReadLine();

            for (int i = 0; i < n.Length; i++)
            {
                if (n[i] + "" == ".")
                {
                    Console.WriteLine("Rainy");
                    return;
                }
            }

            long num = long.Parse(n);

            if (num >= sbyte.MinValue && num <= sbyte.MaxValue)
            {
                Console.WriteLine("Sunny");
            }
            else if (num >= int.MinValue && num <= int.MaxValue)
            {
                Console.WriteLine("Cloudy");
            }
            else
            {
                Console.WriteLine("Windy");
            }
        }
    }
}
