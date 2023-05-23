import abc
from typing import Iterable, Union, List, Dict, Any


class Constraint(abc.ABC):
	"""
	Constraint Class

	A generic value constraint.

	Attributes:


	"""

	def __init__(self, *args: List, **kwargs: Dict) -> None:
		"""
		Generic Constraint Constructor

		:param args: List, The list of positional args the constraint
			may accept.
		:param kwargs: Dict, The dict of key-word args the constraint
			may accept.
		:return: None

		"""

		pass

	@abc.abstractmethod
	def evaluate(self, value: Any) -> None:
		"""
		Evaluate the constraint on the provided value.

		:param value: Any, The value to check the constraint against.
		:return: None

		:raises: NotImplementedError, ValueError


		"""

		raise NotImplementedError()

	@abc.abstractmethod
	def __hash__(self) -> int:
		"""
		Calculate the hash of the constraint.

		:return: int

		:raises: NotImplementedError

		"""

		raise NotImplementedError()

	@abc.abstractmethod
	def __eq__(self, other: 'Constraint') -> bool:
		"""
		Calculate equality between this constraint and the 'other'
		constraint passed into the comparison method.

		:param other: Constraint, The constraint to be compared to.
		:return: bool

		:raises: NotImplementedError

		"""

		raise NotImplementedError()


class ConstraintSet(object):
	"""
	Constraint Set Class

	A container for a set of constraints.

	Attributes:


	"""

	def __init__(self, constraints: Union[Constraint, Iterable[Constraint]] = None) -> None:
		"""
		Constraint Set Constructor

		:param constraints: Union[Constraint, List[Constraint]], A list of
			constraints to load into the container.
		:return: None

		"""

		self._constraints = set()

		if constraints is not None:
			if isinstance(constraints, Constraint):
				constraints = [constraints]

			self.add_constraints(constraints=constraints)

	def add_constraint(self, constraint: Constraint) -> None:
		"""
		Add the constraint to the constraint set.

		:param constraint: Constraint, The constraint to add to the
			constraint set.
		:return: None

		"""

		self.add_constraints(constraints={constraint})

	def add_constraints(self, constraints: Iterable) -> None:
		"""
		Add the constraints to the constraint set.

		:param constraints: Iterable, An iterable object containing the
			constraints to add to the constraint set.
		:return: None

		"""

		constraints = set(constraints)
		self._constraints = self._constraints.union(constraints)

	def remove_constraint(self, constraint: Constraint) -> None:
		"""
		Remove the constraint from the constraint set.

		:param constraint: Constraint, The constraint to remove from
			the constraint set.
		:return: None

		"""

		self.remove_constraints(constraints={constraint})

	def remove_constraints(self, constraints: Iterable) -> None:
		"""
		Remove the specified constraints from the constraint set.

		:param constraints: Iterable, An iterable object containing the
			constraints to remove from the constraint set.
		:return: None

		"""

		constraints = set(constraints)
		self._constraints = self._constraints - constraints

	def clear(self) -> None:
		"""
		Clear the constraint set of all constraints.

		:return: None

		"""

		self._constraints = {}

	@property
	def constraints(self) -> List:
		"""
		Get the set of constraints as a list.

		:return: List

		"""

		return list(self._constraints.copy())
