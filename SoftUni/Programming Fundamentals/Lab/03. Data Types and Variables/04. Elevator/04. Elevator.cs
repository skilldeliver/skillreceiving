using System;

namespace _04._Elevator
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int c = int.Parse(Console.ReadLine());

            int courses = 0;

            if (n <= c)
            {
                courses = 1;
            }
            else if (c % n != 0)
            {
                courses = (int)Math.Ceiling((double)n / c);
            }
            else
            {
                courses = n / c;
            }

            Console.WriteLine(courses);
        }
    }
}
