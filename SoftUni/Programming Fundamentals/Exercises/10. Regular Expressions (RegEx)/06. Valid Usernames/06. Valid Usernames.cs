using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace _06._Valid_Usernames
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] usernames = Console.ReadLine().Split(" /\\()".ToCharArray(), StringSplitOptions.RemoveEmptyEntries);
            string regex = @"^[a-zA-Z][a-zA-Z0-9_]{2,24}$";
            List<string> validUsers = new List<string>();

            foreach (string user in usernames)
            {
                if (Regex.IsMatch(user, regex)) validUsers.Add(user);
            }

            long sum = 0;
            string first = "";
            string second = "";

            for (int i = 1; i < validUsers.Count; i++)
            {
                long currSum = validUsers[i - 1].Length + validUsers[i].Length;
                if (currSum > sum)
                {
                    sum = currSum;
                    first = validUsers[i - 1];
                    second = validUsers[i];
                }
            }
            Console.WriteLine(first);
            Console.WriteLine(second);
        }
    }
}
