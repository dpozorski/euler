import abc
import pandas as pd
from typing import List
from generic.objects.variables import Variable, Solution


class Problem(abc.ABC):
	"""
	Problem Class

	A generic problem class to solve.

	TODO:
		- Add a generic `random` function to help for generation

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

		:raises: NotImplementedError

		"""

		raise NotImplementedError()

	@abc.abstractmethod
	def randomize(self, seed: int = None) -> 'Problem':
		"""
		Generate a randomly constructed problem instance with a valid
		input binding.

		:param seed: int, The seed value to use (if any) for random
			instance generation.
		:return: Problem

		:raises: NotImplementedError

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


class ProblemGenerator(object):
	"""
	Problem Generator Class

	TODO:
		- Add a seed value for generation.
		- Batch class

	Attributes:
		base (:obj:`Problem`): The base problem to generate from.
		batch_size (:obj:`int`): The size of batches to generate
			when running in batch mode.

	"""

	def __init__(self, base: Problem, batch_size: int = 10) -> None:
		"""
		Problem Generator Constructor

		:param base: Problem, The base problem to generate from.
		:param batch_size: int, The size of batches to generate when running
			in batch mode.
		:return: None

		"""

		self.base = base
		self.batch_size = batch_size

	def __iter__(self) -> 'ProblemGenerator':
		"""
		Return the object as the iterator to move over the problems to
		generate.

		:return: ProblemGenerator

		"""

		return self

	def __next__(self) -> Problem:
		"""
		Return the next instantiation of the problem.

		:return: Problem

		"""

		return self.next()

	def next(self) -> Problem:
		"""
		Generate the next instance of the problem.

		TODO:
			- Add seed value
			- Add iter termination return

		:return: Problem

		"""

		return self.base.randomize()

	def batch(self) -> pd.DataFrame:
		"""
		Create a problem batch of size .

		:return: pd.DataFrame

		"""

		curr_batch_size, batch = 0, []

		for problem in self.__iter__():
			solution = problem.solve()
			instance = {var.name: var.binding for var in problem.variables}
			instance["solution"] = solution.value
			batch.append(instance)
			curr_batch_size += 1

		return pd.DataFrame(batch)

	@property
	def base(self) -> Problem:
		"""
		Get the base problem.

		:return: Problem

		"""

		return self._base

	@base.setter
	def base(self, base: Problem) -> None:
		"""
		Set the base problem to use as the source for the generator.

		:param base: Problem, The base problem to generate from.
		:return: None

		"""

		self._base = base

	@property
	def batch_size(self) -> int:
		"""
		Get the batch size.

		:return: int

		"""

		return self._batch_size

	@batch_size.setter
	def batch_size(self, batch_size: int) -> None:
		"""
		Set the batch size.

		:param batch_size: int, The batch size.
		:return: None

		"""

		self._batch_size = batch_size
