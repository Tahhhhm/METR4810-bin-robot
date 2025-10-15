import numpy as np

class nav:
    def __init__(self):
        self.orientation= 1 #1 is forward, 2 is right, 3 is back, 4 is left
        self.map=np.zeros((5,5), dtype=int)
        self.current_pos = [2,2]
        self.map[self.current_pos[0], self.current_pos[1]] = -1
        self.starting_pos = self.current_pos
        self.set_current_on_map()
    
    def get_orientation(self):
        return self.orientation
    
    def turn_right(self):
        if self.orientation < 4:
            self.orientation = self.orientation + 1
        else:
            self.orientation = 1

    def turn_left(self):
        if self.orientation > 1:
            self.orientation = self.orientation -1
        else:
            self.orientation = 4

    def get_current_pos(self):
        return self.current_pos
    
    def update_current_pos(self, new_pos):
        self.current_pos = new_pos 

    def set_current_on_map(self):
        print("setting current position on map", self.current_pos)
        self.map[self.current_pos[0], self.current_pos[1]]+=100
    
    def get_forward_cord(self):
        if self.orientation == 1 and self.current_pos[0]-1 >= 0:
            forward_cord = [self.current_pos[0]-1, self.current_pos[1]]
            return forward_cord
        elif self.orientation == 2 and self.current_pos[1]+1 <= self.map.shape[1]-1:
            forward_cord = [self.current_pos[0], self.current_pos[1]+1]
            return forward_cord
        elif self.orientation == 3 and self.current_pos[0]+1 <= self.map.shape[0]-1:
            forward_cord = [self.current_pos[0]+1, self.current_pos[1]]
            return forward_cord
        elif self.orientation == 4 and self.current_pos[1]-1 >= 0:
            forward_cord = [self.current_pos[0], self.current_pos[1]-1]
            return forward_cord
        else:
            self.extend_map()
            return self.get_forward_cord()


    def whats_ahead(self):
        try:
            t = input("what is ahead?")
            return np.array([[int(t)]])
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.whats_ahead()
        
    def adding_to_map(self):
        self.what_direction_turning()
        x = self.get_forward_cord()
        z=self.whats_ahead()
        forward_x=x[0]
        forward_y=x[1]
        self.map[forward_x,forward_y]=z.item()    
        
    def what_direction_turning(self):
        t = input("which direction?")
        if t == 'left':
            self.turn_left()
            print("orientation is", self.orientation)
        elif t == 'right':
            self.turn_right()
            print("orientation is", self.orientation)
        elif t == 'forward':
            print("orientation is", self.orientation)
            return
        else:
            print("Invalid input. Please enter left, right or forward.")
            return self.what_direction_turning()
                
    def move_ahead(self):
        self.map[self.current_pos[0], self.current_pos[1]]+=-100
        x= self.get_forward_cord()
        print ("moving to", x)
        self.current_pos = x
        self.set_current_on_map()


    def extend_map(self):
        print("extending map")
        self.map=np.pad(self.map, pad_width=1, mode='constant', constant_values=0)
        self.current_pos[0]+=1
        self.current_pos[1]+=1
        self.starting_pos[0]+=1
        self.starting_pos[1]+=1    

test_map = nav()
i=0
while i in range(10):
    print(test_map.map)
    test_map.adding_to_map()
    test_map.move_ahead()
    i+=1
print(test_map.map)
#while True:
    
    #test_map.adding_to_map()
    #test_map.move_ahead()
    #print("current position is", test_map.current_pos)
    #print(test_map.map)
