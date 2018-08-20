using System;

namespace _07._Multiply_big_number
{
    class Program
    {
        static void Main(string[] args)
        {
            string num1 = Console.ReadLine().TrimStart('0');
            int mult = int.Parse(Console.ReadLine());

            string result = "";
            int onMind = 0;

            for (int i = num1.Length - 1; i >= 0; i--)
            {
                int n = int.Parse(num1[i] + "") * mult + onMind;

                if (n < 10)
                {
                    onMind = 0;
                    result = n + result;
                }
                else
                {
                    onMind = n / 10;
                    n = n % 10;
                    result = n + result;
                }
            }
            if (onMind != 0)
            {
                result = onMind + result;
            }
            Console.WriteLine(result);
        }
    }
}
