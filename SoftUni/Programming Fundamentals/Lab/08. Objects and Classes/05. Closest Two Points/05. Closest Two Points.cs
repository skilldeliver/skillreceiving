using System;
using System.Collections.Generic;
using System.Linq;

namespace _05._Closest_Two_Points
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            List<int[]> points = new List<int[]>();

            for (int i = 0; i < n; i++)
            {
                points.Add(Console.ReadLine().Split(' ').Select(int.Parse).ToArray());
            }

            Point point = new Point();
            Console.WriteLine(point.ClosestPoint(points));
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

        public string ClosestPoint(List<int[]> points)
        {
            double minDist = double.MaxValue;
            string twoPoints = "";

            for (int i = 0; i < points.Count; i++)
            {
                for (int j = 0; j < points.Count; j++)
                {
                    if (j != i)
                    {
                        double dist = CalcDistance(points[i], points[j]);
                        if (dist < minDist)
                        {
                            minDist = dist;
                            twoPoints = $"({points[i][0]}, {points[i][1]})\n({points[j][0]}, {points[j][1]})";
                        }
                    }
                }
            }
            return $"{minDist:F3}\n{twoPoints}";
        }
    }
}
