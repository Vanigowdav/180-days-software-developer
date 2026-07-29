# Logical operators are used to combine conditional statements. In python , there are three logical operators:
# 1. and: Returns True if both statements are true.
# 2. or: Returns True if one of the statements is true. It is also called short-circuit operator.
# 3. not: Retunns True if the statemnet is false and vice versa. It is also called negation operator.
#Logical operators are used with boolean values (True or False). When used with non-boolean values, they return one of the operands.

#example 1:
print(5 > 3 and 10 > 5) 
print(5 > 3 or 10 < 5)
print(not(5 > 3))         #here 5 > 3 is True, so not(True) will return False  

#example 2 : 
age = 18
has_voter_id = True 
print(age >= 18 and has_voter_id)

#example 3:
age = 15
has_parental_consent = True
is_holiday = False
has_ticket_money = True
 
can_watch_alone = age >= 18
can_watch_with_consent = age < 18 and has_parental_consent
is_eligible = can_watch_alone or can_watch_with_consent
can_buy_ticket = is_eligible and has_ticket_money
is_discount_day = is_holiday or age < 12

print("Age:", age)
print("Has Parental Consent:", has_parental_consent)
print("Can Watch Alone:", can_watch_alone)
print("Can Watch With Consent:", can_watch_with_consent)
print("Is Eligible:", is_eligible)
print("Can Buy Ticket:", can_buy_ticket)
print("Is Discount Day:", is_discount_day)
print("Not Eligible:", not is_eligible)