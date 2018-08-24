using System;
using System.Collections.Generic;
using System.IO;


namespace _02._Line_Numbers
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines(@"text.txt");
            List<string> numberedLines = new List<string>();

            for (int i = 0; i < lines.Length; i++)
            {
                numberedLines.Add((i + 1) + ". " + lines[i]);
            }
            File.WriteAllLines(@"output.txt", numberedLines);
            Console.WriteLine("Done!");
        }
    }
}
