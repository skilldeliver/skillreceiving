using System;

namespace _02._Email_me
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] tokens = Console.ReadLine().Split('@');
            int sum1 = 0;
            int sum2 = 0;

            foreach (var item in tokens[0])
            {
                sum1 += item;
            }

            foreach (var item in tokens[1])
            {
                sum2 += item;
            }

            int result = sum1 - sum2;

            if (result >= 0)
            {
                Console.WriteLine("Call her!");
            }
            else
            {
                Console.WriteLine("She is not the one.");
            }
        }
    }
}
