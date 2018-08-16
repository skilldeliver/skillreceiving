using System;
using System.Linq;
using System.Collections.Generic;

namespace _06._Rectangle_Position
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] points1 = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            int[] points2 = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

            Rectangle rect1 = new Rectangle(points1);
            Rectangle rect2 = new Rectangle(points2);

            if (rect1.IsInside(rect2)) Console.WriteLine("Inside");
            else Console.WriteLine("Not inside");
        }
    }

    class Rectangle
    {
        public int Left;
        public int Right;
        public int Top;
        public int Bottom;

        public Rectangle(int[] points)
        {
            int left = points[0];
            int top = points[1];
            int width = points[2];
            int height = points[3];

            Left = left;
            Right = left + width;
            Top = top;
            Bottom = top + height;
        }

        public bool IsInside(Rectangle r)
        {

            if (Left >= r.Left && Right <= r.Right && Top <= r.Top && Bottom <= r.Bottom)
            {
                return true;
            }
            return false;
        }
    }
}
