import yaml

with open('data.yml', 'r') as file:
    data = yaml.safe_load(file)

for c in data['collection']:
    print(c)

def check_c(key, data=data['collection']):
    print()
    c = data[key]
    print(f"Collection {key} has type {type(c)}")
    print(f"Collection {key} has value {c}")

check_c('thing2')
check_c('thing3')
check_c('thing4')
check_c('thing5')
check_c('subthing1', data=data['collection']['thing5'])
check_c('subthing2', data=data['collection']['thing5']['subthing1'])
check_c('thing6')