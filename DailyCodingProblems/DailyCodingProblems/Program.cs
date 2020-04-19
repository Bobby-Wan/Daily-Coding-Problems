using System.Linq;

namespace DailyCodingProblems
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var result = Solutions.Problem362.BuildAllStrobogrammatic(6, 6);
            var numbers = result.Select(x => int.Parse(x)).ToList();
            foreach(var number in numbers)
            {
                System.Console.WriteLine(number);
            }
        }
    }
}
