from typing import Optional, List, Any

from dataclasses_ import Mood, Body
from exceptions import BrokenTeethError


class Person:
	_mood: Mood
	_body: Body

	def __init__(self, name: str):
		self._name: str = name

	@property
	def name(self) -> str:
		return self._name

	@property
	def mood(self) -> Mood:
		return self._mood

	@mood.setter
	def mood(self, mood: Mood):
		self._mood = mood


class Participant(Person):
	def __init__(self, name: str, damage: int):
		super().__init__(name)
		self._damage = damage

	@property
	def damage(self) -> int:
		return self._damage

	def __repr__(self):
		return f'Желающий разгрызть орех {self.name}'


class Princess(Person):
	def __init__(self, name: str):
		super().__init__(name)
		self._spouse: Optional[Participant] = None

	def get_married(self, object: Participant):
		self._spouse = object

	@property
	def spouse(self) -> Participant:
		return self._spouse

	@property
	def body(self) -> Body:
		return self._body

	@body.setter
	def body(self, body: Body):
		self._body = body

	def __repr__(self) -> str:
		return f'Принцесса {self.name}'


class Wanderer(Person):
	def __init__(self, name: str, things: List[Any]):
		super().__init__(name)
		self._things = things

	def see(self, object: Person):
		pass

	def __repr__(self):
		return f'Странник {self.name}'


class Nut:
	def __init__(self, hp: int):
		self._hp = hp  # Условные очки прочности скорлупы
		self._nut_shell: bool = True
		self._cracker: Optional[Participant] = None

	def crack(self, object: Participant):
		if object.damage > self._hp:
			self._nut_shell = False
			self._cracker = object
		else:
			raise BrokenTeethError

	@property
	def cracker(self) -> Participant:
		return self._cracker

	@property
	def nut_shell(self) -> bool:
		return self._nut_shell

	def __repr__(self) -> str:
		if self._nut_shell:
			return f'Орех не расколот'
		return f'Орех расколот!'
