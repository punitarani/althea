import random
import string  # noqa

import reflex as rx


class GraphVisual(rx.NoSSRComponent):
    """A custom graph visual component."""

    library = "react-force-graph-3d"
    tag = "ForceGraph3D"
    graph_data: rx.Var[dict] = {
        "nodes": [
            {"id": "1", "group": 1, "val": 1, "label": "Node 1"},
            {"id": "2", "group": 2, "val": 5},
            {"id": "3", "group": 3, "val": 10},
            {"id": "4", "group": 2, "val": 30},
            {"id": "5", "group": 1, "val": 14},
        ],
        "links": [
            {"source": "1", "target": "2"},
            {"source": "1", "target": "3"},
            {"source": "1", "target": "4"},
            {"source": "2", "target": "3"},
            {"source": "3", "target": "4"},
            {"source": "4", "target": "5"},
            {"source": "5", "target": "1"},
        ],
    }
    width: rx.Var[int]
    height: rx.Var[int]
    background_color: rx.Var[str] = "black"
    nodeAutoColorBy: rx.Var[str] = "group"
    zoom_to_fit: rx.Var[int, int, int] = (0, 10, 10)

    is_default = True


graph = GraphVisual.create


def generate_graph_data(num_nodes, max_val):
    """
    Generates graph data with a specified number of nodes and random sizes for each node.
    The links are randomly generated between nodes.

    :param num_nodes: The total number of nodes in the graph.
    :param max_val: The maximum size value for a node.
    :return: A dictionary with two keys: 'nodes' and 'links'.
    """
    # Generate nodes with random sizes
    nodes = [
        {
            "id": str(i),
            "group": 1,
            "val": random.randint(1, max_val),
            "label": f"Node {i}",
        }
        for i in range(1, num_nodes + 1)
    ]

    # Generate links with random connections between nodes
    links = [
        {
            "source": str(random.randint(1, num_nodes)),
            "target": str(random.randint(1, num_nodes)),
        }
        for _ in range(num_nodes - 1)
    ]

    # Remove links where source and target are the same
    links = [link for link in links if link["source"] != link["target"]]

    return {"nodes": nodes, "links": links}


def graph_example():
    return rx.center(
        graph(),
        background_color="black",
        width="10px",
        height="50px",
        center_at=(100, 0, 0),
    )
