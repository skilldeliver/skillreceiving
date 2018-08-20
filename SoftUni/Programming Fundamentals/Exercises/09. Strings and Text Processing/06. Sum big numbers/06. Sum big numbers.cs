using System;

namespace _06._Sum_big_numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            string num1 = Console.ReadLine().TrimStart('0');
            string num2 = Console.ReadLine().TrimStart('0');

            int max = Math.Max(num1.Length, num2.Length);
            num1 = new string('0', max - num1.Length) + num1;
            num2 = new string('0', max - num2.Length) + num2;

            string result = "";
            int onMind = 0;

            for (int i = max - 1; i >= 0; i--)
            {
                int n = int.Parse(num1[i] + "") + int.Parse(num2[i] + "") + onMind;

                if (n < 10)
                {
                    onMind = 0;
                    result = n + result;
                }
                else
                {
                    onMind = 1;
                    n -= 10;
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