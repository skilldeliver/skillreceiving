using System;
using System.Globalization;
using System.Linq;
using System.Collections.Generic;

namespace _06._Book_Library_Modification
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());

            List<Book> books = new List<Book>();

            for (int i = 0; i < n; i++)
            {
                string[] info = Console.ReadLine().Split();
                Book book = new Book();
                book.Title = info[0];
                book.Author = info[1];
                book.Publisher = info[2];
                book.ReleaseDate = DateTime.ParseExact(info[3], "dd.MM.yyyy", CultureInfo.InvariantCulture);
                book.ISBN = info[4];
                book.Price = double.Parse(info[5]);

                books.Add(book);
            }
            DateTime date = DateTime.ParseExact(Console.ReadLine(), "dd.MM.yyyy", CultureInfo.InvariantCulture);

            Library lib = new Library();
            lib.Name = "lib";
            lib.Books = books;

            SortedDictionary<string, DateTime> data = new SortedDictionary<string, DateTime>();

            foreach (Book book in lib.Books)
            {
                data[book.Title] = book.ReleaseDate;
            }

            foreach (var entry in data.Where(x => x.Value >date).OrderBy(x => x.Value))
            {
                Console.WriteLine($"{entry.Key} -> {entry.Value.ToString("dd.MM.yyyy")}");
            }
        }
    }

    class Library
    {
        public string Name { get; set; }
        public List<Book> Books { get; set; }

    }

    class Book
    {
        public string Title { get; set; }
        public string Author { get; set; }
        public string Publisher { get; set; }
        public DateTime ReleaseDate { get; set; }
        public string ISBN { get; set; }
        public double Price { get; set; }
    }
}
