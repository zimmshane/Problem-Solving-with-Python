class Fraction:
    def __init__(self,top,bottom) -> None:
        common=gcd(top,bottom)
        self.num=top//common
        self.den=bottom//common
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self,other):
        new_num=(self.num * other.den) + (self.den * other.num)
        new_den=(self.den * other.den)
        return Fraction(new_num,new_den)
    
    def __eq__(self,other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num
    
    def __mul_(self,other):
        new_num=self.num*other.num
        new_den=self.den*other.den
        return Fraction(new_num,new_den)
    
    def __div__(self,other):
        new_num=self.num*other.den
        new_den=self.den*other.num
        common=gcd(new_num,new_den)
        return Fraction(new_num,new_den)
    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.den
    

def gcd(m,n):
    while m % n != 0:
        old_m= m
        old_n=n
        m=old_n
        n=old_m %old_n
    return n

my_fraction=Fraction(3,7)
frac_2=Fraction(4,32)
f3=my_fraction+frac_2
print(my_fraction,"+", frac_2,"=",f3)