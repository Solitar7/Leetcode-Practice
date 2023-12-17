# Time Limit Exceeded Version

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.menu = dict()
        for i in range(len(foods)):
            self.menu[foods[i]] = [cuisines[i],ratings[i]]
        print(self.menu)

    def changeRating(self, food: str, newRating: int) -> None:
         self.menu[food] = [self.menu[food][0], newRating]

    def highestRated(self, cuisine: str) -> str:
        high = -1
        for i in self.menu:
            if self.menu[i][0] == cuisine:
                if self.menu[i][1] > high:
                    result = i
                    high = self.menu[i][1]
                elif self.menu[i][1] == high:
                    result = min(result, i)
        return result


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
