import abc
import copy
from typing import Any, List, Union, Iterable
from generic.objects.constraints import Constraint, ConstraintSet


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

	def __init__(self, name: str, description: str, constraints: List[Constraint] = None) -> None:
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
		self._constraint_set = ConstraintSet(constraints=constraints)

	def constrain(self, constraints: Union[Iterable, Constraint]) -> None:
		"""
		Constrain the variable with the additional constraint(s).

		:param constraints: Union[Iterable, Constraint], The constraints to
			apply to the variable.
		:return: None

		"""

		constraints = [constraints] if isinstance(constraints, Constraint) else constraints
		self._constraint_set.add_constraints(constraints=constraints)

	def unconstrain(self, constraints: Union[Iterable, Constraint]) -> None:
		"""
		Remove the specified constraints from variable.

		:param constraints: Union[Iterable, Constraint], The constraints to
			remove from the variable and any binding.
		:return: None

		"""

		constraints = [constraints] if isinstance(constraints, Constraint) else constraints
		self._constraint_set.remove_constraints(constraints=constraints)

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

		:return: List[Constraint]

		"""

		return self._constraint_set.constraints


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
		self._variable = variable
		self.bind(value=value)

	def reassociate(self, variable: Variable) -> None:
		"""
		Associate the binding value with this variable.

		:param variable: Variable, The variable to associate the
			value with.
		:return: None

		"""

		self._variable = variable
		self.bind(value=self._value)

	def bind(self, value: Any) -> None:
		"""
		Rebind with the new value.

		:param value: Any, The value to be bound to the var.
		:return: None

		:raises: ValueError

		"""

		for constraint in self._variable.constraints:
			constraint.evaluate(value=value)

		self._value = value

	@property
	def value(self) -> Any:
		"""
		Get the bound value.

		:return: Any

		"""

		return copy.copy(self._value)

	@property
	def variable(self) -> Variable:
		"""
		Get the variable that the value is bound to.

		:return: Variable

		"""

		return copy.copy(self._variable)


class Solution(Variable):
	"""
	Solution Class

	A solution is an unconstrained variable with a binding provided.

	Attributes:
		description (:obj:`str`): The description of the solution.

	"""

	def __init__(self, description: str) -> None:
		"""
		Solution Variable Constructor

		:return: None

		"""

		super().__init__(
			name=Solution.__name__,
			description=description,
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
