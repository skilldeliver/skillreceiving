using System;

namespace _07._Hideout
{
    class Program
    {
        static void Main(string[] args)
        {
            string map = Console.ReadLine();
            map += "ю";
                
            while (true)
            {
                string[] tokens = Console.ReadLine().Split();

                int count = 1;
                for (int i = 1; i < map.Length; i++)
                {
                    if (map[i] == map[i - 1] && map[i].ToString() == tokens[0])
                    {
                        count += 1;
                    }
                    else if (count != 1)
                    {
                        if (count >= int.Parse(tokens[1].ToString()))
                        {
                            Console.WriteLine($"Hideout found at index {i - count} and it is with size {count}!");
                            return;
                        }
                        count = 1;
                    }
                }
            }
        }
    }
}
