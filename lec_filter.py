names = ['john', 'david', 'maria', 'anna']
ages = [16, 25, 19, 15]

def checker(user):
    name, age = user
    return age > 18

users = list(zip(names, ages))
can_vote = list(filter(checker, users))
print(can_vote)