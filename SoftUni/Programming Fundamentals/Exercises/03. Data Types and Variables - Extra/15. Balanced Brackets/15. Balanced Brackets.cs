using System;

namespace _15._Balanced_Brackets
{
    class Program
    {
        static void Main(string[] args)
        {
            int numberOfInputs = int.Parse(Console.ReadLine());

            string lastBracket = string.Empty;
            string balance = "BALANCED";

            for (int i = 0; i < numberOfInputs; i++)
            {
                string currentInput = Console.ReadLine();
                if (currentInput == "(")
                {
                    if (lastBracket == "(")
                    {
                        balance = "UNBALANCED";
                        break;
                    }
                    lastBracket = "(";
                }
                if (currentInput == ")")
                {
                    if (lastBracket != "(")
                    {
                        balance = "UNBALANCED";
                        break;
                    }
                    lastBracket = ")";
                }
            }
            if (lastBracket == "(")
            {
                balance = "UNBALANCED";
            }

            Console.WriteLine(balance);
        }
    }
}

//int n = int.Parse(Console.ReadLine());
//bool unbalanced = false;
//int openIndex = 0;
//int closeIndex = 0;
//string chr = "";

//            for (int i = 0; i<n; i++)
//            {
//                string line = Console.ReadLine();
//                for (int j = 0; j<line.Length; j++)
//                {
//                    if (line[j] + "" == "(" || line[j] + "" == ")")
//                    {
//                         chr = line[j] + "";
//                    }
//                }
//                if (chr == "(")
//                {   
//                    openIndex += 1;
//                }
//                else if (chr == ")")
//                {   
//                    closeIndex += 1;
//                }

//                if (openIndex == closeIndex)
//                {
//                    openIndex = 0;
//                    closeIndex = 0;
//                }

//                if (openIndex == 2 || closeIndex == 2)
//                {
//                    unbalanced = true;
//                }
//            }

//            if (openIndex != closeIndex || unbalanced)
//            {
//                Console.WriteLine("UNBALANCED");
//            }
//            else
//            {
//                Console.WriteLine("BALANCED");
//            }

//string result = "";
//string balanced = "";
//for (int i = 0; i < n; i++)
//{
//    string line = Console.ReadLine();

//    if (line == "(" || line == ")") result += line;
//}

//if (result.Length == 1) { Console.WriteLine("UNBALANCED"); return; }

//for (int i = 1; i <= result.Length; i++)
//{
//    if (i % 2 != 0) balanced += "(";
//    else balanced += ")";
//}

//if (balanced == result) { Console.WriteLine("BALANCED"); return; }
//Console.WriteLine("UNBALANCED");