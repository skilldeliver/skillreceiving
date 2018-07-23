using System;

namespace _06._Interval_of_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int n1 = int.Parse(Console.ReadLine());
            int n2 = int.Parse(Console.ReadLine());

            int num1 = 0;
            int num2 = 0;

            if (n1 > n2)
            {
                num1 = n2;
                num2 = n1;
            }
            else
            {
                num1 = n1;
                num2 = n2;
            }

            for (int i = num1; i <= num2; i++)
            {
                Console.WriteLine(i);
            }
        }
    }
}
