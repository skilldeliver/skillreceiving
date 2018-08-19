using System;
using System.Globalization;
using System.Linq;
using System.Collections.Generic;

namespace _07._Andrey_and_Billiard
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            Dictionary<string, decimal> entities = new Dictionary<string, decimal>();

            for (int i = 0; i < n; i++)
            {
                string[] tokens = Console.ReadLine().Split('-');
                entities[tokens[0]] = decimal.Parse(tokens[1]);
            }

            List<Customer> customers = new List<Customer>();

            while (true)
            {
                string line = Console.ReadLine();
                if (line == "end of clients") break;

                string[] tokens = line.Split('-');
                string name = tokens[0];
                string[] productQuan = tokens[1].Split(',');
                string product = productQuan[0];
                int quanity = int.Parse(productQuan[1]);

                if (!entities.Keys.Contains(product)) continue;
                
                if (customers.Select(c => c.Name).Contains(name))
                {
                    var curCust = customers[customers.FindIndex(x => x.Name == name)];
                    if (curCust.ShopList.Keys.Contains(product))
                    {
                        curCust.ShopList[product] += quanity;
                    }
                    else
                    {
                        curCust.ShopList[product] = quanity;
                    }

                    customers[customers.FindIndex(x => x.Name == name)] = curCust;
                }
                else
                {
                    Customer customer = new Customer();
                    customer.Name = name;
                    customer.ShopList = new Dictionary<string, int>();
                    customer.ShopList[product] = quanity;
                    customers.Add(customer);
                }
            }

            decimal totalBill = 0;
            foreach (Customer cust in customers.OrderBy(c => c.Name))
            {
                Console.WriteLine(cust.Name);
                decimal bill = 0;
                foreach (var entry in cust.ShopList)
                {
                    Console.WriteLine($"-- {entry.Key} - {entry.Value}");
                    bill += entities[entry.Key] * entry.Value;
                }
                Console.WriteLine($"Bill: {bill:F2}");
                totalBill += bill;
            }
            Console.WriteLine($"Total bill: {totalBill:F2}");
        }
    }

    class Customer
    {
        public string Name { get; set; }
        public Dictionary<string, int> ShopList { get; set; }
        public decimal Bill { get; set; }
    }
}
