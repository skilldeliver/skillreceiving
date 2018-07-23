using System;

namespace _08._Calories_Counter
{
    class Program
    {
        static void Main(string[] args)
        {

            int n = int.Parse(Console.ReadLine());
            int total = 0;

            for (int i = 1; i <= n; i++)
            {
                string ingredient = Console.ReadLine().ToLower();

                if (ingredient == "cheese")
                {
                    total += 500;
                }
                else if (ingredient == "tomato sauce")
                {
                    total += 150;
                }
                else if (ingredient == "salami")
                {
                    total += 600;
                }
                else if (ingredient == "pepper")
                {
                    total += 50;
                }

            }
            Console.WriteLine("Total calories: " + total);
        }
    }
}
