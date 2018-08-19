using System;
using System.Linq;

namespace _03._Circles_Intersection
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] c1 = Console.ReadLine().Split().Select(long.Parse).ToArray();
            long[] c2 = Console.ReadLine().Split().Select(long.Parse).ToArray();

            Circle cirlce1 = new Circle(new long[] { c1[0], c1[1] }, c1[2]);
            Circle cirlce2 = new Circle(new long[] { c2[0], c2[1] }, c2[2]);

            if (Intersect(cirlce1, cirlce2))
            {
                Console.WriteLine("Yes");
            }
            else
            {
                Console.WriteLine("No");
            }

        }
        static bool Intersect(Circle c1, Circle c2)
        {
            Point p = new Point();
            if (c1.Radius + c2.Radius >= p.CalcDistance(c1.Center, c2.Center)) return true;
            return false;

        }

        class Circle
        {
            public long[] Center;
            public long Radius;

            public Circle(long[] points, long r)
            {
                Center = points;
                Radius = r;
            }
        }

        class Point
        {

            public double CalcDistance(long[] point1, long[] point2)
            {
                long a = Math.Abs(point1[0] - point2[0]);
                long b = Math.Abs(point1[1] - point2[1]);

                return Math.Sqrt(a * a + b * b);
            }
        }
    }
}
