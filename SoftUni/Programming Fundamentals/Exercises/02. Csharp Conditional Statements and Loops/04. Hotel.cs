using System;

namespace _04._Hotel
{
    class Program
    {
        static void Main(string[] args)
        {
            string month = Console.ReadLine();
            int nights = int.Parse(Console.ReadLine());
            double studio = 0;
            double doubleV = 0;
            double suite = 0;

            if (month == "May" || month == "October")
            {
                studio = 50;
                doubleV = 65;
                suite = 75;

                if (nights > 7) studio *= 0.95;
            }
            else if (month == "June" || month == "September")
            {
                studio = 60;
                doubleV = 72;
                suite = 82;

                if (nights > 14) doubleV *= 0.9;
            }
            else if (month == "July" || month == "August" || month == "December")
            {
                studio = 68;
                doubleV = 77;
                suite = 89;

                if (nights > 14) suite *= 0.85;
            }

            double priceStudio = nights * studio;
            double priceDouble = nights * doubleV;
            double priceSuite = nights * suite;

            if ((month == "September" || month == "October") && nights > 7) priceStudio -= studio;

            Console.WriteLine($"Studio: {priceStudio:f2} lv.");
            Console.WriteLine($"Double: {priceDouble:f2} lv.");
            Console.WriteLine($"Suite: {priceSuite:f2} lv.");

        }
    }
}
