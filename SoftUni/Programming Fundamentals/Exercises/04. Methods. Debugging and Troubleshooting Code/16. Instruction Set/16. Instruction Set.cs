using System;
using System.Numerics;

namespace _16._Instruction_Set
{
    class Program
    {
        static void Main(string[] args)
        {
            string opCode = "";

            while (opCode != "END")
            {
                opCode = Console.ReadLine().ToUpper();
                string[] codeArgs = opCode.Split(' ');

                BigInteger result = 0;
                switch (codeArgs[0])
                {
                    case "INC":
                        {
                            long operandOne = long.Parse(codeArgs[1]);
                            result = operandOne + 1;
                            break;
                        }
                    case "DEC":
                        {
                            long operandOne = long.Parse(codeArgs[1]);
                            result = operandOne - 1;
                            break;
                        }
                    case "ADD":
                        {
                            long operandOne = long.Parse(codeArgs[1]);
                            long operandTwo = long.Parse(codeArgs[2]);
                            result = operandOne + operandTwo;
                            break;
                        }
                    case "MLA":
                        {
                            long operandOne = long.Parse(codeArgs[1]);
                            long operandTwo = long.Parse(codeArgs[2]);
                            result = (BigInteger)operandOne * (BigInteger)operandTwo;
                            break;
                        }
                }

                if (opCode != "END") Console.WriteLine(result);

            }
        }
    }
}
