"""Unit tests for RobotState class."""

import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.state import RobotState
from src.problem import WarehouseProblem


def test_state_equality():
    """Test state equality check."""
    state1 = RobotState((0, 0), frozenset([(1, 1)]))
    state2 = RobotState((0, 0), frozenset([(1, 1)]))
    state3 = RobotState((0, 1), frozenset([(1, 1)]))
    
    assert state1 == state2
    assert state1 != state3
    print("✓ test_state_equality passed")


def test_state_hash():
    """Test state hashing."""
    state1 = RobotState((0, 0), frozenset([(1, 1)]))
    state2 = RobotState((0, 0), frozenset([(1, 1)]))
    
    assert hash(state1) == hash(state2)
    print("✓ test_state_hash passed")


def test_neighbors_basic():
    """Test neighbor generation."""
    grid = [['S', '.'], ['.', 'D']]
    problem = WarehouseProblem(grid, [], (1, 1))
    state = RobotState((0, 0))
    neighbors = state.get_neighbors(problem)
    
    assert len(neighbors) == 2  # Down and Right
    print("✓ test_neighbors_basic passed")


def test_package_collection():
    """Test package collection works."""
    grid = [['S', 'P'], ['.', 'D']]
    problem = WarehouseProblem(grid, [(0, 1)], (1, 1))
    state = RobotState((0, 0))
    neighbors = state.get_neighbors(problem)
    
    # Moving to package should collect it
    package_collected = False
    for neighbor in neighbors:
        if neighbor.position == (0, 1):
            if (0, 1) in neighbor.collected:
                package_collected = True
    
    assert package_collected == True
    print("✓ test_package_collection passed")


if __name__ == "__main__":
    # Run tests manually
    test_state_equality()
    test_state_hash()
    test_neighbors_basic()
    test_package_collection()
    print("\n✅ All tests passed!")