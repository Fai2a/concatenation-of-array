class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        max_defense = 0
        weak_characters = 0
        # Step 2: Traverse list
        for attack, defense in properties:
            if defense < max_defense:
                weak_characters += 1  # current is weak
            else:
                max_defense = defense  # update max defense seen so far

        return weak_characters