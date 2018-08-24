using System;
using System.Linq;
using System.Collections.Generic;

namespace _02._Vehicle_Catalogue
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Vehicle> vehicles = new List<Vehicle>();
            //distinct list or last element 33
            //car formating

            while (true)
            {
                string[] tokens = Console.ReadLine().Split();
                if (tokens[0] == "End") break;

                Vehicle vehicle = new Vehicle();
                vehicle.Type = tokens[0];
                vehicle.Model = tokens[1];
                vehicle.Color = tokens[2];
                vehicle.HP = int.Parse(tokens[3]);

                vehicles.Add(vehicle);
            }

            while (true)
            {
                string model = Console.ReadLine();
                if (model == "Close the Catalogue") break;

                List<Vehicle> vehicleL = vehicles.Where(x => x.Model == model).ToList();
                Vehicle vehicle = vehicleL[vehicleL.Count - 1];

                Console.Write("Type: ");
                for (int i = 0; i < vehicle.Type.Length; i++)
                {
                    if (i == 0)
                    {
                        Console.Write((vehicle.Type[i] + "").ToUpper());
                    }
                    else
                    {
                        Console.Write((vehicle.Type[i] + "").ToLower());
                    }
                }
                Console.WriteLine();
                Console.WriteLine("Model: " + vehicle.Model);
                Console.WriteLine("Color: " + vehicle.Color);
                Console.WriteLine("Horsepower: " + vehicle.HP);
            }

            double avgC = 0;
            double avgT = 0;
            try
            {
                avgC = vehicles.Where(x => x.Type.ToLower() == "car").Select(x => x.HP).Average();

            }
            catch (InvalidOperationException) { }

            try
            {
                avgT = vehicles.Where(x => x.Type.ToLower() == "truck").Select(x => x.HP).Average();

            }
            catch (InvalidOperationException) { }

            Console.WriteLine($"Cars have average horsepower of: {avgC:F2}.");
            Console.WriteLine($"Trucks have average horsepower of: {avgT:F2}.");

        }
    }

    class Vehicle
    {
        public string Type { get; set; }
        public string Model { get; set; }
        public string Color { get; set; }
        public int HP { get; set; }
    }
}
