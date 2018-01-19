import os

print('os.path.abspath(__file__) is: ')
print(os.path.abspath(__file__))
print()

print('os.path.dirname(os.path.abspath(__file__)) is: ')
print(os.path.dirname(os.path.abspath(__file__)))
print()

print('os.path.dirname(os.path.dirname(os.path.abspath(__file__))) (aka BASE DIR) is: ')
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('os.path.join(BASE_DIR, '../static')  is: ')
print(os.path.join(BASE_DIR, '../static'))
print()