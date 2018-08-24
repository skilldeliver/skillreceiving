using System;

namespace _08._Personal_Exception
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                int n = int.Parse(Console.ReadLine());

                if (n < 0)
                {
                    try
                    {
                        throw new NegativeNumberException();
                    }
                    catch
                    {
                        Console.WriteLine("My first exception is awesome!!!");
                        break;
                    }
                }

                Console.WriteLine(n);
            }
        }
    }

    class NegativeNumberException : System.Exception
    {
        public NegativeNumberException() : base() { }
        public NegativeNumberException(string message) : base(message) { }
    }
}
