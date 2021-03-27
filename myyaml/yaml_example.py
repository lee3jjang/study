import yaml

with open('example.yaml') as f:
    fruits = yaml.load_all(f, Loader=yaml.FullLoader)

    print(list(fruits)[0]['Name'])


fruits = {"Name": ["SangJin", "Jiwon"]}

with open('result.yaml', 'w') as f:
    yaml.dump(fruits, f)