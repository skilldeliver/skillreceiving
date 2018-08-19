using System;
using System.Globalization;
using System.Linq;
using System.Collections.Generic;

namespace _10._Student_Groups
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Town> towns = ReadTownsAndStudents();
            List<Group> groups = DistributeStudentsIntoGroups(towns);
            Print(towns, groups);

        }

        static void Print(List<Town> towns, List<Group> groups)
        {
            Console.WriteLine($"Created {groups.Count} groups in {towns.Distinct().ToList().Count} towns:");
            foreach (Group group in groups.OrderBy(g => g.Town.Name))
            {
                Console.Write(group.Town.Name + " => ");
                Console.WriteLine(string.Join(", ", group.Students.Select(s => s.Email)));
            }
        }

        static List<Town> ReadTownsAndStudents()
        {
            List<Town> towns = new List<Town>();

            while (true)
            {
                string line = Console.ReadLine();
                if (line == "End") break;

                //If line is Town
                if (line.IndexOf('>') != -1 && line.IndexOf('=') != -1)
                {
                    Town town = new Town();
                    string[] tokens = line.Split("=>".ToCharArray(), StringSplitOptions.RemoveEmptyEntries);

                    town.Name = tokens[0].Trim();
                    town.SeatsCount = int.Parse(tokens[1].Trim().Split()[0].Trim());
                    town.Students = new List<Student>();

                    towns.Add(town);
                }
                else //Else it is a student
                {
                    Student student = new Student();
                    string[] tokens = line.Split('|');

                    student.Name = tokens[0].Trim();
                    student.Email = tokens[1].Trim();
                    student.RegistrationDate = DateTime.ParseExact(tokens[2].Trim(), "d-MMM-yyyy", CultureInfo.InvariantCulture);
                    towns[towns.Count - 1].Students.Add(student);
                }
            }

            return towns;
        }

        static List<Group> DistributeStudentsIntoGroups(List<Town> towns)
        {
            List<Group> groups = new List<Group>();

            foreach (var town in towns.OrderBy(t => t.Name))
            {
                IEnumerable<Student> students = town.Students.
                    OrderBy(s => s.RegistrationDate).
                    ThenBy(s => s.Name).
                    ThenBy(s => s.Email);

                while (students.Any())
                {
                    Group group = new Group();
                    group.Town = town;
                    group.Students = students.Take(group.Town.SeatsCount).ToList();
                    students = students.Skip(group.Town.SeatsCount);
                    groups.Add(group);
                } 
            }

            return groups;
        }
    }

    class Student
    {
        public string Name { get; set; }
        public string Email { get; set; }
        public DateTime RegistrationDate { get; set; }
    }
    
    class Town
    {
        public string Name { get; set; }
        public int SeatsCount { get; set; }
        public List<Student> Students { get; set; }
    }

    class Group
    {
        public Town Town { get; set; }
        public List<Student> Students { get; set; }
    }
}
