using System;
using System.Linq;
using System.Collections.Generic;

namespace _07._Play_Catch
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> nums = Console.ReadLine().Split().Select(int.Parse).ToList();
            int count = 0;

            while (count < 3)
            {
                string[] tokens = Console.ReadLine().Split();
                string command = tokens[0];

                try
                {
                    if (command == "Replace")
                    {
                        int index = int.Parse(tokens[1]);
                        nums[index] = int.Parse(tokens[2]);
                    }
                    else if (command == "Print")
                    {
                        int start = int.Parse(tokens[1]);
                        int end = int.Parse(tokens[2]);

                        Console.WriteLine(string.Join(", ", nums.GetRange(start, end - start + 1)));
                    }
                    else if (command == "Show")
                    {
                        int index = int.Parse(tokens[1]);
                        Console.WriteLine(nums[index]);
                    }
                }
                catch
                {
                    int check = 0;

                    if (tokens.Length > 2)
                    {

                        if (int.TryParse(tokens[1], out check) && int.TryParse(tokens[2], out check))
                        {
                            Console.WriteLine("The index does not exist!");
                        }
                        else
                        {
                            Console.WriteLine("The variable is not in the correct format!");
                        }
                    }
                    else if (int.TryParse(tokens[1], out check))
                    {                    
                            Console.WriteLine("The index does not exist!");
                    }
                    else
                    {
                        Console.WriteLine("The variable is not in the correct format!");
                    }
                    count++;
                }
            }
            Console.WriteLine(string.Join(", ", nums));
        }
    }
}
