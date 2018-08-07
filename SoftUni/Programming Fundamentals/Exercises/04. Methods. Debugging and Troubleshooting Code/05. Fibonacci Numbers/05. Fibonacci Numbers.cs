using System;

namespace _05._Fibonacci_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int num = int.Parse(Console.ReadLine());
            Console.WriteLine(NthFibonacciNum(num));
        }

        static int NthFibonacciNum(int n)
        {
            int previousNumber = 1;
            int currentNumber = 1;

            for (int i = 2; i <= n; i++)
            {
                currentNumber = currentNumber + previousNumber;
                previousNumber = currentNumber - previousNumber;
            }
            return currentNumber;
        }
    }
}
