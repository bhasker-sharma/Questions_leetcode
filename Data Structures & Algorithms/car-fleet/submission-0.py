class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = sorted((zip(position,speed)),reverse = True)
        fleet = 0
        time = 0.0
        for i,j in car:
            distance = target - i
            c_time = distance/j

            if c_time > time:
                fleet += 1
                time = c_time
        return fleet

        