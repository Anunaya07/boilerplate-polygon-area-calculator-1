class Rectangle:

     def __init__(self,width,height):
       self.height=height
       self.width=width
     def set_width(self,width):
       self.width=width
     def set_height(self,height):
       self.height=height
     def get_area(self):
       return self.width*self.height
     def get_perimeter(self):
       return 2*(self.width+self.height)
     def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
     def get_picture(self):
       if self.width>50:
         return "Too big for picture."
       return_str=''
       for i in range(self.height):
         return_str+="*"*self.width
         return_str+="\n"
       return return_str
     def get_amount_inside(self,shape):
       n=(self.width*self.height)//(shape.width*shape.height)
       return n
     def __repr__(self):
       return f"Rectangle(width={self.width}, height={self.height})"
     
class Square(Rectangle):
     def __init__(self,side):
       self.height=self.width=side
     def set_side(self,side):
       self.set_width(side)
       self.set_height(side)
     def set_width(self,side):
       self.height=self.width=side
     def set_height(self,side):
       self.height=self.width=side
     def __repr__(self):
       return f"Square(side={self.height})"
