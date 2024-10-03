from tests import test_function

def area_perimetr_rectangle(a,b):
    """
    Calculate the area and perimeter of a rectangle with sides a and b.
    """
    area = a * b
    perimeter = 2 * (a + b)
    return area,perimeter

def area_perimetr_square(a):
    """
    Calculate the area and perimeter of a square with side a.
    """
    area = a ** 2
    perimeter = 4 * a
    return area,perimeter

def savings(salary,percent_mortgage,percent_life):
    """
    Calculate the annual savings for a person with a given salary, mortgage interest rate, and life insurance rate.
    """
    mortgage_cost = salary * percent_mortgage / 100
    life_insurance_cost = salary * percent_life / 100
    total_cost = mortgage_cost + life_insurance_cost
    savings_year = (salary - total_cost)*12
    return savings_year

test_function(area_perimetr_rectangle,(30,22),5,6)
test_function(area_perimetr_rectangle,(42,26),7,6)
test_function(area_perimetr_rectangle,(25,20),5,5)

test_function(area_perimetr_square,(25,20),5)
test_function(area_perimetr_square,(49,28),7)
test_function(area_perimetr_square,(1,4),1)

test_function(savings,240000,100000,30,50)
test_function(savings,64800,60000,41,50)
test_function(savings,16800,70000,41,57)
