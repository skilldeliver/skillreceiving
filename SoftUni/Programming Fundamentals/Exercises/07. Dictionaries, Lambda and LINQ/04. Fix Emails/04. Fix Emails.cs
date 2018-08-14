using System;
using System.Collections.Generic;

namespace _04._Fix_Emails
{
    class Program
    {
        static void Main(string[] args)
        {
            string name = "";
            string email = "";

            Dictionary<string, string> dict = new Dictionary<string, string>();

            while (true)
            {
                name = Console.ReadLine();
                if (name == "stop") break;
                email = Console.ReadLine();

                if (!(email.EndsWith("us") || email.EndsWith("uk")))
                {
                    dict[name] = email;
                }

            }

            foreach (var entry in dict)
            {
                Console.WriteLine(entry.Key + " -> " + entry.Value);
            }
        }
    }
}
