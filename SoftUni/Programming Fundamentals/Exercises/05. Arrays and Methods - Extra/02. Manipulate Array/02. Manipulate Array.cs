using System;
using System.Linq;

namespace _02._Manipulate_Array
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] arr = Console.ReadLine().Split(' ');
            int n = int.Parse(Console.ReadLine());

            for (int i = 0; i < n; i++)
            {
                string command = Console.ReadLine();

                if (command == "Distinct")
                {
                    arr = arr.Distinct().ToArray();
                }
                else if (command == "Reverse")
                {
                    arr = arr.Reverse().ToArray();
                }
                else if (command.StartsWith("Replace"))
                {
                    string[] parameters = command.Split(' ');
                    arr[int.Parse(parameters[1])] = parameters[2];
                }
            }

            PrintArr(arr);

        }
        static void PrintArr(string[] arr)
        {
            foreach (var item in arr)
            {
                Console.Write(item);
                if (!item.Equals(arr[arr.Length - 1]))
                {
                    Console.Write(", ");
                }
                
            }
        }
    }
}
