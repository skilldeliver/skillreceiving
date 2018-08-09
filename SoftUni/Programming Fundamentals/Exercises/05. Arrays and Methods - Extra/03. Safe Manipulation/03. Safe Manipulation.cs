using System;
using System.Linq;

namespace _03._Safe_Manipulation
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] arr = Console.ReadLine().Split(' ');

            string command = "";
            while (command != "END")
            {

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
                    int n = int.Parse(parameters[1]);

                    if (n < 0 || n >= arr.Length)
                    {
                        Console.WriteLine("Invalid input!");
                    }
                    else
                    {
                        arr[n] = parameters[2];
                    }
                    
                }
                else if (command != "")
                {
                    Console.WriteLine("Invalid input!");
                }

                command = Console.ReadLine();
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
