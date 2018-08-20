using System;

namespace _09._Melrah_Shake
{
    class Program
    {
        static void Main(string[] args)
        {
            long first = 0;
            long last = 0;
            string line = Console.ReadLine();
            string search = Console.ReadLine();

            while (true)
            {
                first = line.IndexOf(search);
                last = line.LastIndexOf(search);

                if (first != -1 && last != -1 && search.Length > 0)
                {
                    line = line.Remove((int)last, search.Length);
                    line = line.Remove((int)first, search.Length);

                    Console.WriteLine("Shaked it.");

                    search = search.Remove(search.Length / 2, 1);
                }
                else
                {
                    Console.WriteLine("No shake.");
                    Console.WriteLine(line);
                    break;
                }
            }
        }
    }
}
