import random
from faker import Faker
import marshmallow_dataclass

from dataclasses_ import Body, Mood
from exceptions import BrokenTeethError
from objects import Human, Nut, Wanderer, Participant, Princess

drosselmeyer = Human('Дроссельмейер')
astronom = Human('Астроном')
krakatuk = Nut()  # самый твердый орех Кракатук

wanderers = [Wanderer(name=i.name, things=[krakatuk]) for i in (drosselmeyer, astronom)]  # путешественники

participants = []  # желающие раскусить орех
for _ in range(10):
	name = Faker().name_male()
	damage = random.randint(0, 50)  # для проверки возможности расколоть орех
	participant = Participant(name, damage)
	participants.append(participant)

pr_pirlipat = Princess('Pirlipat')
BodySchema = marshmallow_dataclass.class_schema(Body)
pr_pirlipat.body = BodySchema().load(
	{
		'head': {
			'size': ['extra_large'],
			'appearance': ['ugly', 'beautiful'],
			'beard': {
				'size': ['thin'],
				'color': ['white']
			}
		},
		'arm': {
			'size': ['extra_small', 'thin'],
		},
		'size': ['small']
	})

for wander in wanderers:
	wander.see(pr_pirlipat)
	wander.mood = Mood.fear

for participant in participants:
	try:
		krakatuk.crack(participant)
		break
	except BrokenTeethError:
		participant.teeth = False
		pr_pirlipat.mood = Mood.sad
		participant.faint = True
		print('Ну! Вот так орех!')
else:
	king = Human('Король')
	king.mood = Mood.grief
	nutcracker = Participant(name='Щелкунчик', damage=300)
	try:
		krakatuk.crack(nutcracker)
		pr_pirlipat.get_married(krakatuk.cracker)
	except BrokenTeethError:
		pass

if pr_pirlipat.spouse == nutcracker:
	pr_pirlipat.mood = Mood.happy
	print('Спойлер! Щелкунчик расколет орех, но свадьбы не будет :)')
