import pytest
from utils.util import Node, StackFrontier, QueueFrontier

def test_node():
    node = Node(state="A", parent=None, action=None)
    assert node.state == "A"
    assert node.parent is None
    assert node.action is None

def test_stack_frontier():
    frontier = StackFrontier()
    assert frontier.empty() == True
    # Add more tests for StackFrontier methods

def test_queue_frontier():
    frontier = QueueFrontier()
    assert frontier.empty() == True
    # Add more tests for QueueFrontier methods

from utils.util import Node, StackFrontier, QueueFrontier