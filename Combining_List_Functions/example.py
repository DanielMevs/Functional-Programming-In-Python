from functools import reduce

employees = [{
    'name': 'Jane',
    'salary': 90000,
    'job_title': 'developer'
}, {
    'name': 'Bill',
    'salary': 50000,
    'job_title': 'writer'
}, {
    'name': 'Kathy',
    'salary': 120000,
    'job_title': 'executive'
}, {
    'name': 'Anna',
    'salary': 100000,
    'job_title': 'developer'
}, {
    'name': 'Dennis',
    'salary': 95000,
    'job_title': 'developer'
}, {
    'name': 'Albert',
    'salary': 70000,
    'job_title': 'marketing specialist'
}]

def is_developer(employee):
    return employee['job_title'] == 'developer'

def is_not_developer(employee):
    return employee['job_title'] != 'developer'

def get_salary(employee):
    return employee['salary']


developers1 = [devs for devs in employees if devs['job_title'] == 'developer']
developers1a = [devs for devs in employees if is_developer(devs)]
developers = list(filter(is_developer, employees))
print(developers)

non_developers1 = [nonDevs for nonDevs in employees if nonDevs['job_title'] != 'developer']
non_developers1a = [nonDevs for nonDevs in employees if is_not_developer(nonDevs)]
non_developers = list(filter(is_not_developer, employees))

def get_salary(employee):
    return employee['salary']

developer_salaries1 = [devs['salary'] for devs in developers1]
developer_salaries1a = [get_salary(devs) for devs in developers1]
developer_salaries = list(map(get_salary, developers))
developer_salaries2 = [get_salary(dev) for dev in employee if is_developer(dev)] #removes the need for an intermediate develops list
non_developer_salaries = list(map(get_salary, non_developers))
non_developer_salaries2 = [get_salary(emp) for emp in employees if is_not_developer(emp)]
print(developer_salaries)
print(non_developer_salaries)

def findSum(x, y):
    return x + y

print(reduce(findSum, developer_salaries))
total_developer_salaries = reduce(findSum, developer_salaries)
average_developer_salary = total_developer_salaries / len(developer_salaries)
average_developer_salary1 = total_developer_salaries / len(developer_salaries1)
print(average_developer_salary)

total_non_developer_salaries = reduce(get_sum, non_developer_salaries)
average_non_developer_salary = total_non_developer_salaries / len(non_developer_salaries)
print(average_non_developer_salary)