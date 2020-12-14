# Pete the baker
# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

def cakes(recipe, available):
    ans = 0
    minAvailable = 9999999
    for item,value in recipe.items():
        try:
            canMake = available[item]//value
            if canMake<minAvailable :
                minAvailable = canMake 
        except:
            return 0

    ans = minAvailable      
    return ans





recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
cakes(recipe, available)

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
cakes(recipe, available)