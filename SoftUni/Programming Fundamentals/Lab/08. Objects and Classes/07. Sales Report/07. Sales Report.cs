using System;
using System.Linq;
using System.Collections.Generic;

namespace _07._Sales_Report
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            SortedDictionary<string, double> data = new SortedDictionary<string, double>();

            for (int i = 0; i < n; i++)
            {
                Sale sale = new Sale(Console.ReadLine().Split(' '));
                data[sale.Town] = sale.Price * sale.Quantity;
            }

            foreach (var entry in data)
            {
                Console.WriteLine($"{entry.Key} -> {entry.Value:F2}");
            }
        }
    }

    class Sale
    {
        public string Town;
        public string Product;
        public double Price;
        public double Quantity;

        public Sale(string[] arr)
        {
            Town = arr[0];
            Product = arr[1];
            Price = double.Parse(arr[2]);
            Quantity = double.Parse(arr[3]);
        }
    }
}
