import abc
from typing import List
from generic.objects.variables import Variable
from generic.objects.solutions import Solution


class Problem(abc.ABC):
	"""
	Problem Class

	A generic problem class to solve.

	Attributes:
		id (:obj:`int`): Id of the problem (as it appears) in the Project Euler
			list of problems.
		description (:obj:`str`): The description of the problem.
		variables (:obj:`List[Variable]`): The variables that the problem
			can take into it.

	"""

	def __init__(self, id: int, description: str, variables: List[Variable]) -> None:
		"""
		Generic Problem Constructor

		:param id: int, Id of the problem (as it appears) in the Project Euler
			list of problems.
		:param description: str, The description of the problem.
		:param variables: List[Variable], The list of variables that the
			problem accepts.
		:return: None

		"""

		self.id = id
		self.description = description
		self.variables = variables

	@abc.abstractmethod
	def solve(self) -> Solution:
		"""
		Solve the problem.

		:return: Solution

		"""

		raise NotImplementedError()

	@property
	def id(self) -> int:
		"""
		Get the id of the problem.

		:return: int

		"""

		return self._id

	@id.setter
	def id(self, id: int) -> None:
		"""
		Set the id of the problem.

		:param id: int, The description of the problem.
		:return: None

		"""

		self._id = id

	@property
	def description(self) -> str:
		"""
		Get the description of the problem.

		:return: str

		"""

		return self._description

	@description.setter
	def description(self, description: str) -> None:
		"""
		Set the description of the problem.

		:param description: str, The description of the problem.
		:return: None

		"""

		self._description = description

	@property
	def variables(self) -> List[Variable]:
		"""
		Get the list of variables that the problem accepts.

		:return: List[Variable]

		"""

		return self._variables

	@variables.setter
	def variables(self, variables: List[Variable]) -> None:
		"""
		Set the variables that can be input into the problem.

		:param variables: List[Variable], Variables.
		:return: None

		"""

		self._variables = variables

	@property
	def link(self) -> str:
		"""
		Get the link to the official problem on the Project Euler site.

		:return: str

		"""

		return "https://projecteuler.net/problem={}".format(self.id)
