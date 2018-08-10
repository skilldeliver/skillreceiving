using System;
using System.Collections.Generic;
using System.Linq;


namespace _02._Change_List
{
    class Program
    {
        static void Main(string[] args)
        {
            List<long> nums = Console.ReadLine().Split(' ').Select(long.Parse).ToList();

            string command = "";

            while (!(command == "Odd" || command == "Even"))
            {
                if (command.StartsWith("Delete"))
                {
                    long num = long.Parse(command.Split(' ')[1]);

                    while (nums.Contains(num))
                    {
                        nums.Remove(num);
                    }
                }
                else if (command.StartsWith("Insert"))
                {
                    long item = long.Parse(command.Split(' ')[1]);
                    long index = long.Parse(command.Split(' ')[2]);

                    nums.Insert((int)index, item);
                }


                command = Console.ReadLine();
            }

            if (command == "Odd")
            {
                for(int i  = 0; i < nums.Count; i++)
                {
                    if (nums[i] % 2 != 0) Console.Write(nums[i] + " ");
                }
            }
            else
            {
                for (int i = 0; i < nums.Count; i++)
                {
                    if (nums[i] % 2 == 0) Console.Write(nums[i] + " ");
                }

            }
        }
    }
}
