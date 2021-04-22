from pydantic import BaseModel
from typing import List

class Iterator:
    """ Iterates through a given Model class (must extend BaseModel) """
	""" PRE: Model class extends BaseModel """
	""" POST: Model class can be iterated via iterator using .next() and .prev() """
    def __init__(self, model: BaseModel) -> None:
        self.index = 0
        self.list = dict(model).items()
        self.size = len(list)
        
    """ Returns the current index of list """
    def current(self) -> Any
        return self.list[index]

	""" Returns the next item in the list. If there is none, return null """
    def next(self) -> Any
        if self.index + 1 >= self.size:
            return None
        self.index = self.index + 1
        return self.list[self.index]
        
	""" Returns the previous item in the list. If there is none, return null """ 
    def prev(self) -> Any
        if self.index - 1 < 0
            return None
        self.index = self.index - 1
        return self.list[self.index]
