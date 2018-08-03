using System;

namespace _09._Refactor_Special_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            bool special = false;
            int sum = 0;

            for (int i = 1; i <= n; i++)
            {
                sum = 0;
                int curNum = i;
                while (curNum > 0)
                {
                    sum += curNum % 10;
                    curNum = curNum / 10;
                }
                special = (sum == 5) || (sum == 7) || (sum == 11);
                Console.WriteLine($"{i} -> {special}");
                
            }
        }
    }
}
