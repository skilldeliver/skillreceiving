using System;
using System.Globalization;
using System.Linq;
using System.Collections.Generic;

namespace _08._Mentor_Group
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Student> students = new List<Student>();

            while (true)
            {
                string line = Console.ReadLine();
                if (line == "end of dates") break;

                string[] info = line.Split(' ', ',');
                string name = info[0];
                List<DateTime> dates = new List<DateTime>();

                for (int i = 1; i < info.Length; i++)
                {
                    dates.Add(DateTime.ParseExact(info[i], "dd/MM/yyyy", CultureInfo.InvariantCulture));
                }

                students = FillList(students, name, dates);
            }

            while (true)
            {
                string line = Console.ReadLine();
                if (line == "end of comments") break;

                string[] info = line.Split('-');
                string name = info[0];
                string comment = info[1];

                students = FillList(students, name, comment);
            }

            foreach (Student std in students.OrderBy(x => x.Name))
            {
                Console.WriteLine(std.Name);
                Console.WriteLine("Comments:");
                if (std.Comments != null)
                {
                    foreach (string com in std.Comments)
                    {
                        Console.WriteLine("- " + com);
                    }
                }

                Console.WriteLine("Dates attended:");
                foreach (DateTime date in std.Dates.OrderBy(x => x.Date))
                {
                    Console.WriteLine($"-- {date.Day:D2}/{date.Month:D2}/{date.Year}");
                }
            }

        }

        static List<Student> FillList(List<Student> students, string name, List<DateTime> dates)
        {
            foreach (Student student in students)
            {
                if (student.Name == name)
                {
                    foreach (DateTime date in dates)
                    {
                        student.Dates.Add(date);
                    }
                    return students;
                }
            }

            Student newStudent = new Student();
            newStudent.Name = name;
            newStudent.Dates = new List<DateTime>();

            foreach (DateTime date in dates)
            {
                newStudent.Dates.Add(date);
            }
            students.Add(newStudent);

            return students;
        }

        static List<Student> FillList(List<Student> students, string name, string comment)
        {
            foreach (Student std in students)
            {
                if (std.Name == name)
                {
                    if (std.Comments == null)
                    {
                        std.Comments = new List<string>();
                        std.Comments.Add(comment);
                    }
                    else
                    {
                        std.Comments.Add(comment);
                    }
                }
            }

            return students;
        }
    }

    class Student
    {
        public string Name { get; set; }
        public List<DateTime> Dates { get; set; }
        public List<string> Comments { get; set; }
    }
}
