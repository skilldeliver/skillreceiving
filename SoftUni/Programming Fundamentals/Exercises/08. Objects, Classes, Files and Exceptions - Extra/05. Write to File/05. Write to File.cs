using System;
using System.Collections.Generic;
using System.IO;

namespace _05._Write_to_File
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines(@"sample.txt");
            string chars = ".,!?:";
            List<string> newLines = new List<string>();

            foreach (string line in lines)
            {
                string nline = "";
                foreach (char chr in line)
                {
                    if (chars.IndexOf(chr) == -1)
                    {
                        nline += chr;
                    }
                }
                newLines.Add(nline);
            }

            File.WriteAllLines(@"C:\ABC\Programminng\C#\08. Objects, Classes, Files and Exceptions - More\04. Punctuation Finder\sample.txt", newLines);

            string[] nlines = File.ReadAllLines(@"C:\ABC\Programminng\C#\08. Objects, Classes, Files and Exceptions - More\04. Punctuation Finder\sample.txt");

            Console.WriteLine(string.Join("\n", nlines));

        }
    }
}
