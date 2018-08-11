using System;
using System.Linq;

namespace _05._Short_Words_Sorted
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] words = Console.ReadLine().ToLower().Split(new char[] { '.', ',', ':', ';', '(', ')', '[', ']', '"', '\'', '\\', '/', '!', '?', ' ' }, StringSplitOptions.RemoveEmptyEntries);

            words = words.Where(w => w.Length < 5).OrderBy(w => w).Distinct().ToArray();
            Console.WriteLine(string.Join(", ", words));
        }
    }
}
