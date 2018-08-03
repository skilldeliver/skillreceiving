using System;

namespace _05._Special_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
    
            for (int i = 1; i <= n; i++)
            {
                int sum = 0;
                string istring = i.ToString();

                for (int j = 0; j < istring.Length; j++)
                {
                    sum += int.Parse(istring[j] + "");
                }

                if (sum == 5 || sum == 7 || sum == 11)
                {
                    Console.WriteLine(i + " -> True");
                }
                else
                {
                    Console.WriteLine(i + " -> False");
                }
               
            }
        }
    }
}
