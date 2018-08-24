using System;
using System.Collections.Generic;
using System.IO;

namespace _11._Files__Directories_and_Exceptions___Exercises
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines(@"text.txt");
            List<string> oddLines = new List<string>();

            for (int i = 0; i < lines.Length; i++)
            {
                if (i % 2 != 0)
                {
                    oddLines.Add(lines[i]);
                }
            }

            File.WriteAllLines(@"output.txt", oddLines);
            Console.WriteLine("Done!");
        }
    }
}
