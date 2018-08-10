using System;
using System.Collections.Generic;
using System.Linq;

namespace _03._Search_for_a_Number
{
    class Program
    {
        static void Main(string[] args)
        {
            List<long> nums = Console.ReadLine().Split(' ').Select(long.Parse).ToList();
            List<long> temp = Console.ReadLine().Split(' ').Select(long.Parse).ToList();

            long take = temp[0];
            long del = temp[1];
            long search = temp[2];

            for (long i = del; i < take; i++)
            {
                if (nums[(int)i] == search)
                {
                    Console.WriteLine("YES!");
                    return;
                }
            }

            Console.WriteLine("NO!");

        }
    }
}
