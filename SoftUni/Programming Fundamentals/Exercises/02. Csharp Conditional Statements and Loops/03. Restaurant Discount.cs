using System;

namespace _03._Restaurant_Discount
{
    class Program
    {
        static void Main(string[] args)
        {
            int group_size = int.Parse(Console.ReadLine());
            string package = Console.ReadLine();

            double priceHall;
            int discount = 0;
            int price = 0;
            string hallName = "";

            if (group_size <= 50)
            {
                priceHall = 2500;
                hallName = "Small Hall";
            }
            else if (group_size > 50 && group_size <= 100)
            {
                priceHall = 5000;
                hallName = "Terrace";
            }
            else if (group_size > 100 && group_size <= 120)
            {
                priceHall = 7500;
                hallName = "Great Hall";
            }
            else
            {
                Console.WriteLine("We do not have an appropriate hall.");
                return;
            }


            if (package == "Normal")
            {
                discount = 5;
                price = 500;
            }
            else if (package == "Gold")
            {
                discount = 10;
                price = 750;
            }
            else if (package == "Platinum")
            {
                discount = 15;
                price = 1000;
            }

            double totalPrice = priceHall + price;
            totalPrice -= totalPrice * (discount / 100.00);

            double pricePerPerson = totalPrice / group_size;
            Console.WriteLine($"We can offer you the {hallName}");
            Console.WriteLine($"The price per person is {pricePerPerson:f2}$");
        }
    }
}
