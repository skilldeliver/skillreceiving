using System;

namespace _06._Theatre_Promotion
{
    class Program
    {
        static void Main(string[] args)
        {
            string typeday = Console.ReadLine();
            int age = int.Parse(Console.ReadLine());

            int price = 0;
            bool notElse = true;

            if (age >= 0 && age <= 18)
            {
                if (typeday == "Weekday") price = 12;
                else if (typeday == "Weekend") price = 15;
                else if (typeday == "Holiday") price = 5;

            }
            else if (age >= 19 && age <= 64)
            {
                if (typeday == "Weekday") price = 18;
                else if (typeday == "Weekend") price = 20;
                else if (typeday == "Holiday") price = 12;

            }
            else if (age >= 65 && age <= 122)
            {
                if (typeday == "Weekday") price = 12;
                else if (typeday == "Weekend") price = 15;
                else if (typeday == "Holiday") price = 10;
            }
            else
            {
                Console.WriteLine("Error!");
                notElse = false;
            }
            if (notElse) Console.WriteLine(price + "$");
        }
    }
}
