using System;

namespace _12._Beer_Kegs
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            double max = double.MinValue;
            string result = "";

            for (int i = 0; i < n; i++)
            {
                string model = Console.ReadLine();
                double r = double.Parse(Console.ReadLine());
                int h = int.Parse(Console.ReadLine());

                double volume = Math.PI * r * r * h;
                //Console.WriteLine(volume);

                if (volume > max)
                {
                    max = volume;
                    result = model;
                }
            }

            Console.WriteLine(result);
        }
    }
}
