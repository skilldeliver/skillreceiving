using System;

namespace _10._Cube_Properties
{
    class Program
    {
        static void Main(string[] args)
        {
            double side = double.Parse(Console.ReadLine());
            string property = Console.ReadLine();

            Console.WriteLine("{0:F2}", CubeProperties(side, property));
            
        }

        static double CubeProperties(double side, string property)
        {
            double result = 0.0;

            if (property == "face")
            {
                result = Math.Sqrt(2 * (side * side));    
            }
            else if (property == "space")
            {
                result = Math.Sqrt(3 * (side * side));
            }
            else if (property == "volume")
            {
                result = side * side * side;
            }
            else if (property == "area")
            {
                result = 6 * (side * side);
            }

            return result;
        }
    }
}
