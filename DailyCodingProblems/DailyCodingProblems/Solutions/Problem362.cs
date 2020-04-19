using System;
using System.Collections.Generic;
using System.Text;

namespace DailyCodingProblems.Solutions
{
    public static class Problem362
    {
        public static bool AreStrobogrammatic(int a, int b)
        {
            if(a == 0 && b == 0)
            {
                return true;
            }
            if(a == 1 && b == 1)
            {
                return true;
            }
            if(a == 6 && b == 9)
            {
                return true;
            }
            if(a == 9 && b == 6)
            {
                return true;
            }
            if(a == 8 && b == 8)
            {
                return true;
            }

            return false;
        }

        public static bool IsStrobogrammatic(int number)
        {
            int digits = 1;

            while (true)
            {
                if(number/(10^digits) == 0)
                {
                    break;
                }

                ++digits;
            }

            int index = 1;

            while(index < digits)
            {
                if(!AreStrobogrammatic(number/(10^(digits-index)), number % (10 ^ index))){
                    return false;
                }
            }

            return true;
        }

        public static IEnumerable<string> BuildAllStrobogrammatic(uint digits, int length)
        {
            if(digits == 0 )
            {
                return new List<string> {
                ""
                };
            }
            if(digits == 1)
            {
                return new List<string>
                {
                    "0","1","8"
                };
            }

            var inner = BuildAllStrobogrammatic(digits - 2, length);
            var result = new List<string>();

            foreach(var element in inner)
            {
                if(digits != length)
                {
                    result.Add(ExpandStrobogrammatic(element, 0, 0));
                }
                result.Add(ExpandStrobogrammatic(element, 1, 1));
                result.Add(ExpandStrobogrammatic(element, 6, 9));
                result.Add(ExpandStrobogrammatic(element, 9, 6));
                result.Add(ExpandStrobogrammatic(element, 8, 8));
            }

            return result;
        }

        public static string ExpandStrobogrammatic(string number, int toAppendFront, int toAppendBack)
        {
            if(toAppendFront/10 != 0 || toAppendBack/10 != 0)
            {
                throw new ArgumentException("Value to append too big.");
            }
            return toAppendFront.ToString() + number + toAppendBack.ToString();
        }
    }
}
