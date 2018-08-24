using System;
using System.Linq;
using System.IO;

namespace _05._Folder_Size
{
    class Program
    {
        static void Main(string[] args)
        {
            double length = Directory.GetFiles(@"TestFolder", "*", SearchOption.AllDirectories).Sum(t => (new FileInfo(t).Length));

            File.WriteAllText(@"output.txt", (length / 1000000).ToString());
            Console.WriteLine("Done!");
        }
    }
}
