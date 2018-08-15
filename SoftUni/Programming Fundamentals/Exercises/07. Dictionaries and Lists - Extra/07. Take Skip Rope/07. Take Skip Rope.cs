using System;
using System.Linq;
using System.Collections.Generic;

namespace _07._Take_Skip_Rope
{
    class Program
    {
        static void Main(string[] args)
        {
            string message = Console.ReadLine();
            List<int> numbers = new List<int>();
            List<char> nonNumbers = new List<char>();

            foreach (char chr in message)
            {
                if (int.TryParse(chr + "", out int n))
                {
                    numbers.Add(int.Parse(chr + ""));
                }
                else
                {
                    nonNumbers.Add(chr);
                }
            }

            List<int> takeList = new List<int>();
            List<int> skipList = new List<int>();

            for (int i = 0; i < numbers.Count; i++)
            {
                if (i % 2 == 0) takeList.Add(numbers[i]);
                else skipList.Add(numbers[i]);
            }

            string result = "";
            int total = 0;

            for (int i = 0; i < takeList.Count; i++)
            {

                int to = total + takeList[i];
                if (to > nonNumbers.Count) to = nonNumbers.Count;

                for (int j = total; j < to; j++)
                {
                    result += nonNumbers[j];
                }
                total += takeList[i] + skipList[i];
            }

            Console.WriteLine(result);
        }
    }
}
