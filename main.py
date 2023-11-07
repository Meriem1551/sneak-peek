def is_eligible_to_vote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("You cannot vote")


age = int(input("Enter your age "))
is_eligible_to_vote(age)
