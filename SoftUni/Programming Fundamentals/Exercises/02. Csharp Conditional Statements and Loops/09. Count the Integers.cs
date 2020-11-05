using System;

namespace _09._Count_the_Integers
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 100; i++)
            {
                try
                {
                    int test = int.Parse(Console.ReadLine());
                }
                catch (Exception)
                {
                    Console.WriteLine(i - 1);
                    return;
                }

            }
        }
    }
}