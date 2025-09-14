#rule set:
# 0 = delivery modules
# 1 = Straight modules
# 2 = Left Curves modules 
# 3 = Right Curves modules
# 5 = Chicane modules
# 6 = left Hair pin modules
# 6 = right Hair pin modules
# 7 = crossroad modules
# 8 = T junction left modules
# 8 = T junction right modules
# 9 = Stright modules (bin)
# 10 = Left Curves modules (bin)
# 11 = Right Curves modules (bin)
# 12 = Left Chicane modules (bin)
# 13 = Right Chicane modules (bin)
# 14 = Hair pin modules (bin)
# 15 = crossroad modules (bin)
# 16 = T junction left modules (bin)
 

class road:
    def __init__(self,starting_pos_x,starting_pos_y):
            self.starting_pos_x = starting_pos_x
            self.starting_pos_y = starting_pos_y

    def delivery_modules(self):
        #empty bin
        return 0
    
    def straight_modules(self):
        #go straight
        return 1 
    
    def left_curve_modules(self):
        #turn left
        return 2
    
    def right_curve_modules(self):
        #turn right
        return 3
    
    def chicane_modules(self):
        #go straight (with curves)
        return 4
    
    def left_hair_pin_modules(self):
        #turn left (with curves)
        return 5
    
    def right_hair_pin_modules(self):
        #turn right (with curves)
        return 6
    
    def crossroad_modules(self):
        #left right straight
        return 7
    
    def t_junction_left_modules(self):
        #left straight
        return 8
    
    def t_junction_right_modules(self):
        #right straight
        return 9
    
    def straight_modules_bin(self):
        #go straight slowly and pick up bin
        return 10
    
    def left_curve_modules_bin(self):
        #turn left slowly and pick up bin
        return 11
    
    def right_curve_modules_bin(self):
        #turn right slowly and pick up bin
        return 12
    
    def left_chicane_modules_bin(self):
        #go straight (with curves) slowly and pick up bin
        return 13
