using System;

namespace _03._Karate_Strings
{
    class Program
    {
        static void Main(string[] args)
        {
            string line = Console.ReadLine();
            int remove = 0;

            for (int i = 0; i < line.Length; i++)
            {
                if (line[i] == '>')
                {
                    remove += int.Parse(line[i + 1].ToString());
                }
                else
                {
                    if (remove > 0)
                    {
                        line = line.Remove(i, 1);
                        remove--;
                        i--;
                    }
                }
            }
            Console.WriteLine(line);
        }
    }
}
