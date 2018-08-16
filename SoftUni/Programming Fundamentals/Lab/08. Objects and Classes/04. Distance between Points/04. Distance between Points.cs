using System;
using System.Linq;

namespace _04._Distance_between_Points
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] point1 = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            int[] point2 = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

            Point c = new Point();
            Console.WriteLine($"{c.CalcDistance(point1, point2):F3}");
        }
    }

    class Point
    {

        public double CalcDistance(int[] point1, int[] point2)
        {
            int a = Math.Abs(point1[0] - point2[0]);
            int b = Math.Abs(point1[1] - point2[1]);

            return Math.Sqrt(a * a + b * b);
        }
    }
}
