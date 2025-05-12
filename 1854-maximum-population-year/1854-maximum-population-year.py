class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0] * 101  # Index 0 means year 1950, index 100 means year 2050

    # Step 1: Har saal ke liye population count karo
        for birth, death in logs:
            for year in range(birth, death):  # death year NOT included
             population[year - 1950] += 1

    # Step 2: Max population dhoondo
        max_pop = max(population)
        earliest_year = population.index(max_pop) + 1950

        return earliest_year