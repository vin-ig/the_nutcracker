import enum
from dataclasses import dataclass
from typing import List

import marshmallow


class Appearance(enum.Enum):
	ugly = 'ugly'
	beautiful = 'beautiful'


class Mood(enum.Enum):
	grief = 'grief'
	sad = 'sad'
	happy = 'happy'
	fear = 'fear'


class Color(enum.Enum):
	white = 'white'
	black = 'black'


class Size(enum.Enum):
	extra_small = 'extra_small'
	small = 'small'
	medium = 'medium'
	large = 'large'
	extra_large = 'extra_large'

	thin = 'thin'
	thick = 'thick'


@dataclass
class PartOfBody:
	size: List[Size]

	class Meta:
		unknown = marshmallow.EXCLUDE


@dataclass
class Beard(PartOfBody):
	color: List[Color]

	class Meta:
		unknown = marshmallow.EXCLUDE


@dataclass
class Arm(PartOfBody):
	pass


@dataclass
class Head(PartOfBody):
	appearance: List[Appearance]
	beard: Beard

	class Meta:
		unknown = marshmallow.EXCLUDE


@dataclass
class Body(PartOfBody):
	head: Head
	arm: Arm

	class Meta:
		unknown = marshmallow.EXCLUDE
