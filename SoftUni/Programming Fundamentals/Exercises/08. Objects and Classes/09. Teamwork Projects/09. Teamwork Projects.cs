using System;
using System.Globalization;
using System.Linq;
using System.Collections.Generic;

namespace _09._Teamwork_Projects
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Team> teams = new List<Team>();
            int n = int.Parse(Console.ReadLine());

            for (int i = 0; i < n; i++)
            {
                string[] tokens = Console.ReadLine().Split('-');
                Team team = new Team();
                team.Name = tokens[1];
                team.CreatorName = tokens[0];
                team.Members = new List<string>();

                if (!teams.Select(x => x.Name).Contains(team.Name))
                {
                    if (!teams.Select(x => x.CreatorName).Contains(team.CreatorName))
                    {
                        teams.Add(team);
                        Console.WriteLine($"Team {tokens[1]} has been created by {tokens[0]}!");
                    }
                    else
                    {
                        Console.WriteLine($"{team.CreatorName} cannot create another team!");
                    }
                }
                else
                {
                    Console.WriteLine($"Team {team.Name} was already created!");
                }
            }

            while (true)
            {
                string line = Console.ReadLine();
                if (line == "end of assignment") break;

                string[] tokens = line.Split("->".ToCharArray(), StringSplitOptions.RemoveEmptyEntries);
                string user = tokens[0];
                string teamName = tokens[1];

                if (!teams.Select(x => x.Name).Contains(teamName))
                {
                    Console.WriteLine($"Team {teamName} does not exist!");
                }
                else if (teams.Select(x => x.Members).Any(x => x.Contains(user)) || teams.Select(x => x.CreatorName).Contains(user))
                {
                    Console.WriteLine($"Member {user} cannot join team {teamName}!");
                }
                else
                {
                    int teamIndex = teams.FindIndex(x => x.Name == teamName);
                    teams[teamIndex].Members.Add(user);
                }
            }


            var teamsDisband = teams.OrderBy(x => x.Name).Where(x => x.Members.Count == 0);

            foreach (Team team in teams.OrderByDescending(x => x.Members.Count).ThenBy(x => x.Name).Where(x => x.Members.Count > 0))
            {
                Console.WriteLine(team.Name);
                Console.WriteLine("- " + team.CreatorName);
                foreach (string member in team.Members.OrderBy(x => x))
                {
                    Console.WriteLine("-- " + member);
                }
            }
            Console.WriteLine("Teams to disband:");
            foreach (Team team in teamsDisband)
            {
                Console.WriteLine(team.Name);
            }
        }
    }

    class Team
    {
        public string Name { get; set; }
        public List<string> Members { get; set; }
        public string CreatorName { get; set; }
    }
}