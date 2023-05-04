'''
Its easier to ask forgiveness than permission (EAFP)
'''

p_details = {'name': 'Corey', 'age': 34, 'hobby': 'programming'}

try:
    print('I am {name}, my age is {age} and my hobby is {hobby}.'.format(
        **p_details))
except KeyError as e:
    print('Missing {}'.format(e))
