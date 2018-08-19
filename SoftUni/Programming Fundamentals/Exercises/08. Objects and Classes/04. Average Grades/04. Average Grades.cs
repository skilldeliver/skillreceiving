using System;
using System.Collections.Generic;
using System.Linq;

namespace _04._Average_Grades
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            List<Student> list = new List<Student>();

            for (int i = 0; i < n; i++)
            {
                string[] info = Console.ReadLine().Split();
                string name = info[0];

                if (info.Length > 2)
                {
                    double[] grades = new double[info.Length - 1];
                    for (int j = 0; j < info.Length - 1; j++)
                    {
                        grades[j] = double.Parse(info[j + 1]);
                    }
                    
                list.Add(new Student(name, grades));
                }
                else
                {
                    list.Add(new Student(name, new double[] {double.Parse(info[1])}));
                }
            }

            foreach (Student student in list.Where(s => s.AverageGrade >= 5.00).OrderByDescending(s => s.AverageGrade).OrderBy(s => s.Name))
            {
                Console.WriteLine($"{student.Name} -> {student.AverageGrade:F2}");
            }
        }
    }

    class Student
    {
        public string Name;
        public double[] Grades;
        public double AverageGrade;

        public Student(string name, double[] grades)
        {
            Name = name;
            Grades = grades;
            AverageGrade = grades.Average();
        }

    }
}
