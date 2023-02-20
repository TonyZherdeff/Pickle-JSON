import pickle
import json


class Airplane:
    def __init__(self, num_of_passengers, load_capacity, max_flight_height, max_flight_length):
        self.num_of_passengers = num_of_passengers
        self.load_capacity = load_capacity
        self.max_flight_height = max_flight_height
        self.max_flight_length = max_flight_length

    def print_class(self):
        print(f'Number of passengers is {self.num_of_passengers}\n'
              f'Load capacity is {self.load_capacity}\n'
              f'Max flight height is {self.max_flight_height}\n'
              f'Max flight length is {self.max_flight_length}')

    def change_pass(self, new_nop):
        self.num_of_passengers = new_nop

    def change_load(self, new_load):
        self.load_capacity = new_load

    def change_height(self, new_height):
        self.max_flight_height = new_height

    def change_length(self, new_length):
        self.max_flight_length = new_length

    def to_pickle(self):
        return pickle.dumps(self.__dict__)

    def to_json(self):
        return json.dumps(self.__dict__)

    def from_pickle(self, pickled_data):
        step1 = pickle.loads(pickled_data)
        step2 = pickle.loads(step1)
        return step2

    def from_json(self, jsoned_data):
        return json.loads(jsoned_data)


airplane1 = Airplane(100, 180, 10000, 5000)
airplane1.print_class()
pick = airplane1.to_pickle()
with open('./data.pkl', 'wb') as f:
    pickle.dump(pick, f, protocol=5)
with open('./data.pkl', 'rb') as f:
    data = f.read()
print(airplane1.from_pickle(data))
jso = airplane1.to_json()
with open('./data.json', 'w') as f:
    json.dump(jso, f)
with open('./data.json') as f:
    data1 = f.readline()
print(airplane1.from_json(data1))
