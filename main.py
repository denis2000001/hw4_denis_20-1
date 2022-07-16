from cars.get_car_info import get_car_info
BMW = get_car_info('BMW','f32','2100 kg', '200hp', '450nm', '250km/h', 'black')
print(BMW.start_engine())
print(BMW.stop_engine())
print(BMW.car_info())