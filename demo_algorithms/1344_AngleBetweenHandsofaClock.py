# The tricky part is determining how the minute hand affects the position of the hour hand.
# Calculate the angles separately then find the difference. 

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_new = minutes / 60
        hour_new = (hour + min_new) / 12
        
        min_angle = min_new * 360
        hour_angle = hour_new * 360
        
        res = abs(min_angle - hour_angle)
        
        return min(res, 360 - res)
