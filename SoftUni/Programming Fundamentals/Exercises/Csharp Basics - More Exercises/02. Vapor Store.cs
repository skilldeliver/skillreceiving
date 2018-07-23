using System;

namespace _02._Vapor_Store
{
    class Program
    {
        static void Main(string[] args)
        {
            double budget = double.Parse(Console.ReadLine());
            double firstBudget = budget;


            while (true)
            {
                string command = Console.ReadLine();
                
                if (command == "OutFall 4")
                {
                    if (budget - 39.99 < 0) Console.WriteLine("Too Expensive");
                    else
                    {
                        budget -= 39.99;
                        Console.WriteLine("Bought OutFall 4");
                    }

                }
                else if (command == "CS: OG")
                {
                    if (budget - 15.99 < 0) Console.WriteLine("Too Expensive");
                    else
                    {
                        budget -= 15.99;
                        Console.WriteLine("Bought CS: OG");
                    }

                }
                else if (command == "Zplinter Zell")
                {
                    if (budget - 19.99 < 0) Console.WriteLine("Too Expensive");
                    else
                    {
                        budget -= 19.99;
                        Console.WriteLine("Bought Zplinter Zell");
                    }

                }
                else if (command == "Honored 2")
                {
                    if (budget - 59.99 < 0) Console.WriteLine("Too Expensive");
                    else
                    {
                        budget -= 59.99;
                        Console.WriteLine("Bought Honored 2");
                    }

                }
                else if (command == "RoverWatch")
                {
                    if (budget - 29.99 < 0) Console.WriteLine("Too Expensive");
                    else
                    {
                        budget -= 29.99;
                        Console.WriteLine("Bought RoverWatch");
                    }

                }
                else if (command == "RoverWatch Origins Edition")
                {
                    if (budget - 39.99 < 0) Console.WriteLine("Too Expensive");
                    else
                    {
                        budget -= 39.99;
                        Console.WriteLine("Bought RoverWatch Origins Edition");
                    }

                }
                else if(command == "Game Time")
                {
                    Console.WriteLine($"Total spent: ${firstBudget - budget:f2}. Remaining: ${budget:f2}");
                    return;
                }
                else
                {
                    Console.WriteLine("Not Found");
                }

                if (budget == 0)
                {
                    Console.WriteLine("Out of money!");
                    return;
                }
            }
        }
    }
}
