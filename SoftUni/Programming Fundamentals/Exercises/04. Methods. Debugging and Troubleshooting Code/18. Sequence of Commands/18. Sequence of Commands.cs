using System;
using System.Linq;

namespace _18._Sequence_of_Commands
{
    class Program
    {
        static void Main(string[] args)
        {
            int sizeOfArray = int.Parse(Console.ReadLine());

            long[] array = Console.ReadLine().Split(' ').Select(long.Parse).ToArray();

            string command = Console.ReadLine();

            while (!command.Equals("stop"))
            {
                string[] line = command.Trim().Split(' ');
                int[] parameters = new int[2];

                if (line[0].Equals("add") ||
                    line[0].Equals("subtract") ||
                    line[0].Equals("multiply"))
                {

                    parameters[0] = int.Parse(line[1]);
                    parameters[1] = int.Parse(line[2]);

                    array = PerformAction(array, line[0], parameters);
                }
                else
                {
                    parameters[0] = 1;
                    parameters[1] = 1;
                    array = PerformAction(array, line[0], parameters);
                }


                //PrintArray(array);
                Console.WriteLine();

                command = Console.ReadLine();
            }
        }

        static long[] PerformAction(long[] arr, string action, int[] args)
        {
            long[] array = arr.Clone() as long[];
            int pos = args[0] - 1;
            int value = args[1];

            switch (action)
            {
                case "multiply":
                    array[pos] *= value;
                    break;
                case "add":
                    array[pos] += value;
                    break;
                case "subtract":
                    array[pos] -= value;
                    break;
                case "lshift":
                    array = ArrayShiftLeft(array);
                    break;
                case "rshift":
                    array = ArrayShiftRight(array);
                    break;
            }
            PrintArray(array);

            return array;
        }

        static long[] ArrayShiftRight(long[] array)
        {
            long lastElement = array[array.Length - 1];

            for (int i = array.Length - 1; i >= 1; i--)
            {
                array[i] = array[i - 1];
            }

            array[0] = lastElement;

            return array;
        }

        static long[] ArrayShiftLeft(long[] array)
        {
            long firstElement = array[0];

            for (int i = 0; i < array.Length - 1; i++)
            {
                array[i] = array[i + 1];
            }

            array[array.Length - 1] = firstElement;

            return array;
        }

        private static void PrintArray(long[] array)
        {
            for (int i = 0; i < array.Length; i++)
            {
                Console.Write(array[i] + " ");
            }
        }
    }
}
