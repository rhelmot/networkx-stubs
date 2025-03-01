# Stubs for networkx.algorithms.shortest_paths.generic (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, TypeVar, overload, List, Dict, Iterable

from networkx.classes.graph import Graph

_T = TypeVar('_T')

def has_path(G: Any, source: Any, target: Any): ...


@overload
def shortest_path(G: Graph[_T], source: _T, target: _T, weight: Optional[Any] = ..., method: str = ...) -> List[_T]: ...



@overload
def shortest_path(G: Graph[_T], target: _T, method: str = ...) -> Dict[_T, List[_T]]: ...

@overload
def shortest_path(G: Graph[_T], source: _T, method: str = ...) -> Dict[_T, List[_T]]: ...




def shortest_path_length(G: Any, source: Optional[Any] = ..., target: Optional[Any] = ..., weight: Optional[Any] = ..., method: str = ...): ...
def average_shortest_path_length(G: Any, weight: Optional[Any] = ..., method: str = ...): ...
def all_shortest_paths(G: Graph[_T], source: _T, target: _T, weight: Optional[Any] = ..., method: str = ...) -> Iterable[List[_T]]: ...
