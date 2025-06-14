import math; import random;
import time; import sys;


class point():
    def __init__(self, value_x, value_y, label):
        self.value_x=value_x; self.value_y=value_y;
        self.label=label;
        
class graph():
    def __init__(self, plot_data, origin_point):
        self.plot_data=plot_data;
        self.origin_point=origin_point;
    
    def compute(self):
        difference_from_neighbor=[0]*len(self.plot_data);
        
        for x, _ in enumerate(difference_from_neighbor):
            difference_from_neighbor[x]=abs(self.plot_data[x].value_x - self.origin_point.value_x);
            difference_from_neighbor[x]+=abs(self.plot_data[x].value_y - self.origin_point.value_y);
        
        for x, _ in enumerate(difference_from_neighbor):
            if (difference_from_neighbor[x]==min(difference_from_neighbor)): return self.plot_data[x].label;
            else: pass;