from networkx.classes.digraph import DiGraph
from typing import (
    Any,
    Callable,
    ClassVar,
    Collection,
    Dict,
    Generic,
    Hashable,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
    Tuple,
    TypeVar,
    Union,
    overload,
)
from typing_extensions import TypeAlias
from networkx.classes.coreviews import AdjacencyView
from networkx.classes.reportviews import (
    DiDegreeView,
    NodeView,
    OutEdgeView,
)
from networkx.convert import Data


Node = TypeVar("Node", bound=Hashable)
# Note that `TypeAlias` doesn't work in the current version of Mypy
# So I will `type: ignore` these lines.
# However, the rest of the file is still checked statically.
# https://github.com/microsoft/pylance-release/issues/2019
Edge = Tuple[Node, Node]
EdgePlus = Union[Edge[Node], Tuple[Node, Node, Dict[str, Any]]]
MapFactory = Callable[[], MutableMapping[str, Any]]
NBunch = Union[None, Node, Iterable[Node]]

class Graph(Collection[Node], Generic[Node]):
    node_dict_factory: ClassVar[MapFactory] = ...
    node_attr_dict_factory: ClassVar[MapFactory] = ...
    adjlist_outer_dict_factory: ClassVar[MapFactory] = ...
    adjlist_inner_dict_factory: ClassVar[MapFactory] = ...
    edge_attr_dict_factory: ClassVar[MapFactory] = ...
    graph_attr_dict_factory: ClassVar[MapFactory] = ...

    def to_directed_class(self) -> type[DiGraph[Node]]: ...
    def to_undirected_class(self) -> type[Graph[Node]]: ...

    def __init__(self, incoming_graph_data: Data[Node] | None = None, **attr: Any) -> None: ...

    adj: AdjacencyView[Node, Node, Dict[str, Any]]
    name: str

    def __getitem__(self, n: Node) -> MutableMapping[Hashable, Any]: ...
    def __iter__(self) -> Iterator[Node]: ...
    def __contains__(self, n: object) -> bool: ...
    def __len__(self) -> int: ...

    def add_node(self, node_for_adding: Node, **attr: Any) -> None: ...
    def add_nodes_from(self, nodes_for_adding: Iterable[Node | Tuple[Node, Dict[str, Any]]], **attr: Any) -> None: ...
    def remove_node(self, n: Node) -> None: ...
    def remove_nodes_from(self, nodes: Iterable[Node]) -> None: ...
    nodes: NodeView[Node]
    def number_of_nodes(self) -> int: ...
    def order(self) -> int: ...
    def has_node(self, n: Node) -> bool: ...

    def add_edge(self, u_of_edge: Node, v_of_edge: Node, **attr: Any) -> None: ...
    def add_edges_from(self, ebunch_to_add: Iterable[EdgePlus[Node]], **attr: Any) -> None: ...
    def add_weighted_edges_from(
        self,
        ebunch_to_add: Iterable[tuple[Node, Node, Any]],
        weight: str = ...,
        **attr: Any,
    ) -> None: ...
    def remove_edge(self, u: Node, v: Node) -> None: ...
    def remove_edges_from(self, ebunch: Iterable[EdgePlus[Node]]) -> None: ...

    @overload
    def update(self, edges: Graph[Node], nodes: None = None) -> None: ...
    @overload
    def update(
        self,
        edges: Graph[Node] | Iterable[EdgePlus[Node]] | None = ...,
        nodes: Iterable[Node] | None = ...,
    ) -> None: ...

    def has_edge(self, u: Node, v: Node) -> bool: ...
    def neighbors(self, n: Node) -> Iterable[Node]: ...
    edges: OutEdgeView[Node]
    def get_edge_data(self, u: Node, v: Node, default: Any = ...) -> Mapping[str, Any]: ...
    def adjacency(self) -> Iterable[tuple[Node, Mapping[Node, Mapping[str, Any]]]]: ...

    degree: DiDegreeView[Node]

    def clear(self) -> None: ...
    def clear_edges(self) -> None: ...

    def is_multigraph(self) -> bool: ...
    def is_directed(self) -> bool: ...

    _T = TypeVar("_T", bound=Graph[Node])
    def copy(self: _T, as_view: bool = ...) -> _T: ...

    def to_directed(self, as_view: bool = ...) -> DiGraph[Node]: ...
    def to_undirected(self, as_view: bool = ...) -> Graph[Node]: ...
    def subgraph(self, nodes: Iterable[Node]) -> Graph[Node]: ...
    def edge_subgraph(self, edges: Iterable[Edge[Node]]) -> Graph[Node]: ...

    @overload
    def size(self, weight: None = ...) -> int: ...
    @overload
    def size(self, weight: str) -> float: ...
    def number_of_edges(self, u: Node | None = ..., v: Node | None = ...) -> int: ...

    def nbunch_iter(self, nbunch: NBunch[Node] = ...) -> Iterable[Node]: ...
