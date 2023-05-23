import abc
from typing import Any, List
from generic.objects.constraints import Constraint


class Variable(abc.ABC):
	"""
	Variable Class

	A generic variable representing the domain of values that can be
	input into a given problem.

	Attributes:
		name (:obj:`str`): The name of the variable.
		description (:obj:`str`): The description of the variable.
		constraints (:obj:`List[Constraint]`): The list of constraints to
			apply to any binding for this variable.

	"""

	def __init__(self, name: str, description: str, constraints: List[Constraint]) -> None:
		"""
		Generic Variable Constructor

		:param name: str, The name of the variable.
		:param description: str, The description of the variable.
		:param constraints: List[Constraint], The list of constraints to
			apply to any binding for this variable.
		:return: None

		"""

		self.name = name
		self.description = description
		self.constraints = constraints

	@property
	def name(self) -> str:
		"""
		Get the name of the variable.

		:return: str

		"""

		return self._name

	@name.setter
	def name(self, name: str) -> None:
		"""
		Set the name of the variable.

		:param name: str, The name of the variable.
		:return: None

		"""

		self._name = name

	@property
	def description(self) -> str:
		"""
		Get the description of the variable.

		:return: str

		"""

		return self._description

	@description.setter
	def description(self, description: str) -> None:
		"""
		Set the description of the variable.

		:param description: str, The description of the variable.
		:return: None

		"""

		self._description = description

	@property
	def constraints(self) -> List[Constraint]:
		"""
		Get the constraints for the variable.

		Todo:
			- Add methods for removing/adding constraints

		:return: List[Constraint]

		"""

		return self._constraints


class Binding(object):
	"""
	Variable Binding Class

	A value binding to a variable.

	Attributes:
		variable (:obj:`Variable`): The variable to which the value is bound.
		value (:obj:`Any`): The value bound to a given variable.

	"""

	def __init__(self, variable: Variable, value: Any) -> None:
		"""
		Variable Binding Constructor

		:param variable: Variable, The variable to which the value is bound.
		:param value: Any, The value bound to a given variable.
		:return: None

		"""

		self._value = None
		self.variable = variable
		self.rebind(value=value)

	def rebind(self, value: Any) -> None:
		"""
		Rebind with the new value.

		:param value: Any, The value to be bound to the var.
		:return: None

		:raises: ValueError

		"""

		pass
