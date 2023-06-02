import abc
import copy
from typing import Any, List, Union, Iterable
from generic.objects.constraints import Constraint, ConstraintSet


class Variable(abc.ABC):
	"""
	Variable Class

	A generic variable representing the domain of values that can be
	input into a given problem.

	TODO
		- Name check for variable 'solution'

	Attributes:
		name (:obj:`str`): The name of the variable.
		description (:obj:`str`): The description of the variable.
		value (:obj:`Any`): The value to bind to the variable.
		constraints (:obj:`List[Constraint]`): The list of constraints to
			apply to any binding for this variable.

	"""

	def __init__(self, name: str, description: str, value: Any = None, constraints: List[Constraint] = None) -> None:
		"""
		Generic Variable Constructor

		:param name: str, The name of the variable.
		:param description: str, The description of the variable.
		:param constraints: List[Constraint], The list of constraints to
			apply to any binding for this variable.
		:return: None

		"""

		self._binding = None
		self.name = name
		self.description = description
		self._constraint_set = ConstraintSet(constraints=constraints)
		self.bind(value=value)

	def constrain(self, constraints: Union[Iterable, Constraint]) -> None:
		"""
		Constrain the variable with the additional constraint(s).

		:param constraints: Union[Iterable, Constraint], The constraints to
			apply to the variable.
		:return: None

		"""

		constraints = [constraints] if isinstance(constraints, Constraint) else constraints
		self._constraint_set.add_constraints(constraints=constraints)
		self.bind(value=self.binding)  # Recheck binding w/ new constraint

	def unconstrain(self, constraints: Union[Iterable, Constraint]) -> None:
		"""
		Remove the specified constraints from variable.

		:param constraints: Union[Iterable, Constraint], The constraints to
			remove from the variable and any binding.
		:return: None

		"""

		constraints = [constraints] if isinstance(constraints, Constraint) else constraints
		self._constraint_set.remove_constraints(constraints=constraints)

	def bind(self, value: Any) -> None:
		"""
		Rebind with the new value.

		:param value: Any, The value to be bound to the var.
		:return: None

		:raises: ValueError

		"""

		if value is not None:
			for constraint in self.constraints:
				constraint.evaluate(value=value)

			self._binding = value

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
	def binding(self) -> Any:
		"""
		Get the bound value.

		:return: Any

		"""

		return copy.copy(self._binding)

	@property
	def value(self) -> Any:
		"""
		Get the bound value.

		:return: Any

		"""

		return self.value

	@property
	def constraints(self) -> List[Constraint]:
		"""
		Get the constraints for the variable.

		:return: List[Constraint]

		"""

		return self._constraint_set.constraints


class Solution(Variable):
	"""
	Solution Class

	A solution is an unconstrained variable with a binding provided.

	Attributes:
		value (:obj:`Any`): The solution value.
		description (:obj:`str`): The description of the solution.

	"""

	def __init__(self, value: Any, description: str) -> None:
		"""
		Solution Variable Constructor

		:param value: Any, The solution value.
		:param description: str, The description of the solution.
		:return: None

		"""

		super().__init__(
			name=Solution.__name__,
			description=description,
			value=value,
			constraints=None
		)

	def constrain(self, constraints: Union[Iterable, Constraint]) -> None:
		"""
		Constrain the variable with the additional constraint(s).

		:param constraints: Union[Iterable, Constraint], The constraints to
			apply to the variable.
		:return: None

		:raises: NotImplementedError

		"""

		raise NotImplementedError()
