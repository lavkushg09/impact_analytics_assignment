class GraduationSolution:
    """
    A class representing a solution for calculating the probability of missing the graduation ceremony.
    """

    def __init__(self):
        """
        Initializes the GraduationSolution object with empty dictionaries.
        """
        self.num_of_ways_absent = {}
        self.num_of_ways_present = {}

    def number_of_ways_absent(self, n):
        """
        Calculates the number of ways to be absent at the graduation ceremony for a given number of days.

        Args:
            n (int): The number of days in the academic year.

        Returns:
            int: The number of ways to be absent.
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        elif n == 4:
            return 7
        if n not in self.num_of_ways_absent:
            # Memoization: store previously calculated values to avoid redundant calculations
            self.num_of_ways_absent[n] = (
                self.number_of_ways_absent(n - 1)
                + self.number_of_ways_absent(n - 2)
                + self.number_of_ways_absent(n - 3)
                + self.number_of_ways_absent(n - 4)
            )
        return self.num_of_ways_absent[n]

    def number_of_ways_attend_ceremony(self, n):
        """
        Calculates the number of ways to attend the graduation ceremony for a given number of days.

        Args:
            n (int): The number of days in the academic year.

        Returns:
            int: The number of ways to attend the ceremony.
        """
        if n == 1:
            return 2
        elif n == 2:
            return 4
        elif n == 3:
            return 8
        elif n == 4:
            return 15
        if n not in self.num_of_ways_present:
            # Memoization: store previously calculated values to avoid redundant calculations
            self.num_of_ways_present[n] = (
                self.number_of_ways_attend_ceremony(n - 1)
                + self.number_of_ways_attend_ceremony(n - 2)
                + self.number_of_ways_attend_ceremony(n - 3)
                + self.number_of_ways_attend_ceremony(n - 4)
            )
        return self.num_of_ways_present[n]

    def find_probability(self, n) -> str:
        """
        Finds and returns the probability of missing the graduation ceremony for a given number of days.

        Args:
            n (int): The number of days in the academic year.

        Returns:
            str: The probability as a string in the format "numerator/denominator".
        """
        return f"{self.number_of_ways_absent(n)}/{self.number_of_ways_attend_ceremony(n)}"


# Example usage
if __name__ == "__main__":
    graduation_sol = GraduationSolution()

    # Test case for n = 5
    res1 = graduation_sol.find_probability(5)
    print(f"The probability for {5} days is: {res1}")

    # Test case for n = 10
    res2 = graduation_sol.find_probability(10)
    print(f"The probability for {10} days is: {res2}")
