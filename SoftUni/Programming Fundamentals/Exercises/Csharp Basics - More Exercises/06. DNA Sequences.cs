using System;

namespace _06._DNA_Sequences
{
    class Program
    {
        static void Main(string[] args)
        {
            int sum = int.Parse(Console.ReadLine());
            for (int i = 1; i <= 4; i++)
            {
                for (int j = 1; j <= 4; j++)
                {
                    for (int k = 1; k <= 4; k++)
                    {
                        if (i + j + k >= sum)
                        {
                            Console.Write("O" + convertStr(i) + convertStr(j) + convertStr(k) + "O ");
                        }
                        else
                        {
                            Console.Write("X" + convertStr(i) + convertStr(j) + convertStr(k) + "X ");
                        }
                    }
                    Console.WriteLine();
                }
            }
        }
        static string convertStr(int num)
        {
            if (num == 1)
            {
                return "A";
            }
            else if (num == 2)
            {
                return "C";
            }
            else if (num == 3)
            {
                return "G";
            }
            else if (num == 4)
            {
                return "T";
            }
            return "A";
        }
    }
}
