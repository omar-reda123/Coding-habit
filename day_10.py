"""
Problem: The Perfume Factory Tank (Container With Most Water)

Description:
Given an integer array `heights` representing the heights of vertical lines.
Find two lines that together with the x-axis form a container, such that the container contains the most liquid.
Return the maximum amount of liquid a container can store.

"""

def input_heights():
    heights = list(map(int, input("Enter heights separated by space: ").split()))
    return heights

def max_area_tank(heights):
    max_area = 0
    #Two Pointers
    left = 0
    right = len(heights) - 1
    
    while left < right:
        area=(right-left) * min(heights[left],heights[right])
        if area>max_area:
            max_area=area
        
        if(heights[left] < heights[right]):
            left+=1
        else:
            right-=1
   
        
    return max_area

if __name__ == "__main__":
    print("---The Perfume Factory Tank---")
    plate_heights = input_heights()
    result = max_area_tank(plate_heights)
    print(f"\nMaximum Liquid Area you can store: {result}")