using System;
using System.Globalization;

namespace _08._Objects_and_Classes___Lab
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(DateTime.ParseExact(Console.ReadLine(), "d-M-yyyy", CultureInfo.InvariantCulture).DayOfWeek); 

        }
    }
}
