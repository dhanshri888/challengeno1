# Challenge 1: Square Numbers and Return Their Sum
# Sample properties 1, 3, 5
# Sample method output 35


class point:
    def __init__(self):
        self.x = x
        self.y = y
        self.z = z

    def sqsum(self):
        return ((self.x **2), (self.y **2), (self.z **2))

    def sum(self):
        return ((self.x **2) + (self.y **2) + (self.z **2))

x = int(input("Enter the first number:"))
y = int(input("Enter the second number :"))
z = int(input("Enter the third number:"))

a = point()

print("square of the number are:",a.sqsum())
print("sum of the square are :",a.sum())


































# class point:
#     def __init__(self):
#         self.x = x
#         self.y = y
#         self.z = z
    
#     def sqsum(self):
#         sq_x = self.x ** 2
#         sq_y = self.y ** 2
#         sq_z = self.z ** 2
#         self.square = sq_x + sq_y + sq_z

#     def __str__(self):
#         return f"sum of square of three number :{self.square}"

# x = int(input("Enter first number:"))
# y = int(input("Enter second number:"))
# z = int(input("Enter third number :"))

# point_obj = point()
# point_obj.sqsum()
# print(point_obj)