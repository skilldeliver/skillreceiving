using System;

namespace _06._Catch_the_Thief
{
    class Program
    {
        static void Main(string[] args)
        {
            string type = Console.ReadLine();
            int n = int.Parse(Console.ReadLine());

            long max = long.MinValue;
            long num = 0;

            if (type == "sbyte") num = sbyte.MaxValue;
            else if (type == "int") num = int.MaxValue;
            else if (type == "long") num = long.MaxValue;

            for (int i = 0; i < n; i++)
            {
                long number = long.Parse(Console.ReadLine());
                
                if (number > max && number <= num)
                {
                    max = number;
                }
            }

            Console.WriteLine(max);
        }
    }
}
//switch (type)
//{
//    case "sbyte":
//        num = sbyte.MaxValue;
//        break;
//    case "int":
//        num = int.MaxValue;
//        break;
//    case "long":
//        num = long.MaxValue;
//        break;
//}
