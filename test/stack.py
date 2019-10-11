data = {'school':'DAV', 'class': '7', 'name': 'abc', 'city': 'pune'}


def my_function(**data):
    schoolname  = data['school']
    cityname = data['city']
    standard = data['class']
    studentname = data['name']
    #You can call the function like this:
    print data,
my_function(**data)
