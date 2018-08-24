using System;
using System.Collections.Generic;
using System.Linq;

namespace _08._Objects__Classes__Files_and_Exceptions___More
{
    class Program
    {
        static void Main(string[] args)
        {
            List<User> users = new List<User>();

            while (true)
            {
                string[] tokens = Console.ReadLine().Split();
                if (tokens[0] == "End") break;

                User user = new User();
                user.Name = tokens[0];
                user.ID = tokens[1];
                user.Age = int.Parse(tokens[2]);

                users.Add(user);
            }

            foreach (var user in users.OrderBy(u => u.Age))
            {
                Console.WriteLine($"{user.Name} with ID: {user.ID} is {user.Age} years old.");
            }

        }
    }

    class User
    {
        public string Name { get; set; }
        public string ID { get; set; }
        public int Age { get; set; }
    }
}
