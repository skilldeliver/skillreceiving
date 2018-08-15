using System;
using System.Collections.Generic;
using System.Linq;

namespace Dictionaries_and_Lists___More_Exercises
{
    class Program
    {
        static void Main(string[] args)
        {
            SortedDictionary<long, string> hours = new SortedDictionary<long, string>();
            string[] line = Console.ReadLine().Split(' ');

            foreach (string hour in line)
            {
                long sum = 0;
                string[] hm = hour.Split(':');
                sum = (Parse(hm[0]) * 60) + Parse(hm[1]);
                hours[sum] = hour;
            }
            Console.WriteLine(string.Join(", ", hours.Values));
        }
        static long Parse(string min)
        {
            if (long.TryParse(min, out long n)) return long.Parse(min);
            return long.Parse(min[1] + "");
        }
    }
}
