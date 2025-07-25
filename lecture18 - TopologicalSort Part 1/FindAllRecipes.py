from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes:List[str], ingridients: List[List[str]], supplies: List[str]) -> List[str]:
        
        # Create a graph and indegree count
        graph = defaultdict(list)
        in_degree = {recipe: 0 for recipe in recipes}
        
        # Build the graph
        for recipe, components in zip(recipes, ingridients):
            in_degree[recipe] = len(components)
            for component in components:
                graph[component].append(recipe)
        
        # Initialize the queue with supplies
        queue = deque(supplies)
        result = []
        
        while queue:
            supply = queue.popleft()
                        
            # Process all recipes that can be made with the current ingredient
            for recipe in graph[supply]:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    queue.append(recipe)
                    result.append(recipe)
        
        return result
       