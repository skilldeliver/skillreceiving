using System;
using System.Linq;
using System.Collections.Generic;

namespace _05._Array_Manipulator2
{
    class Program
    {
        static void Main(string[] args)
        {

            List<long> nums = Console.ReadLine().Split(' ').Select(long.Parse).ToList();
            string[] commmand = Console.ReadLine().Split(' ');

            while (commmand[0] != "print")
            {

                if (commmand[0] == "addMany")
                {       
                    int index = int.Parse(commmand[1]);

                    for (int i = 2; i < commmand.Length; i++)
                    {
                        nums.Insert(index, long.Parse(commmand[i]));
                        index += 1;
                    }
                }
                else if (commmand[0] == "add")
                {
                    nums.Insert(int.Parse(commmand[1]), long.Parse(commmand[2]));
                }
                else if (commmand[0] == "contains")
                {
                    Console.WriteLine(nums.IndexOf(long.Parse(commmand[1])));
                }
                else if (commmand[0] == "remove")
                {
                    nums.RemoveAt(int.Parse(commmand[1]));
                }
                else if (commmand[0] == "shift")
                {
                    for (int i = 0; i < int.Parse(commmand[1]); i++)
                    {
                        long first = nums[0];
                        for (int j = 1; j < nums.Count; j++)
                        {
                            nums[j - 1] = nums[j];
                        }

                        nums[nums.Count - 1] = first;
                    }
                }
                else if (commmand[0] == "sumPairs")
                {
                    List<long> pairs = new List<long>();

                    for (int i = 0; i < nums.Count; i += 2)
                    {
                        try
                        {
                            pairs.Add(nums[i] + nums[i + 1]);

                        }
                        catch (Exception)
                        {
                            pairs.Add(nums[i]);
                        }
                    }

                    nums = pairs;
                }

                commmand = Console.ReadLine().Split(' ').ToArray();
            }

            Console.WriteLine("[" + string.Join(", ", nums) + "]");

        }
    }
}
