using System;
using System.Linq;

namespace _06._Heists
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] jewelsAndGold = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();

            string line = "";
            long totalEarnings = 0;
            long totalExpense = 0;

            while (line != "Jail Time")
            {
                if (line.Length > 1)
                {
                    string[] heist = line.Split(' ');
                    
                    for (int i = 0; i < heist[0].Length; i++)
                    {
                        if (heist[0][i] == '%')
                        {
                            totalEarnings += jewelsAndGold[0];
                        }
                        if (heist[0][i] == '$')
                        {
                            totalEarnings += jewelsAndGold[1];
                        }
                    }

                    totalExpense += long.Parse(heist[1]);
                }
                line = Console.ReadLine();
            }

            if (totalEarnings >= totalExpense)
            {
                Console.WriteLine($"Heists will continue. Total earnings: {totalEarnings - totalExpense}.");
            }
            else
            {
                Console.WriteLine($"Have to find another job. Lost: {totalExpense - totalEarnings}.");
            }
        }
    }
}
