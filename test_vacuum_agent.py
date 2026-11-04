"""
Tests for the Simple Reflex Vacuum Agent.

Run with:  python test_vacuum_agent.py
"""

import unittest
from vacuum_agent import VacuumEnvironment, SimpleReflexVacuumAgent


class TestVacuumEnvironment(unittest.TestCase):

    def test_percept_returns_location_and_status(self):
        env = VacuumEnvironment({'A': 'Dirty', 'B': 'Clean'}, start_location='A')
        self.assertEqual(env.percept(), ('A', 'Dirty'))

    def test_clean_action_cleans_location(self):
        env = VacuumEnvironment({'A': 'Dirty', 'B': 'Clean'}, start_location='A')
        env.execute_action('Clean')
        self.assertEqual(env.state['A'], 'Clean')

    def test_move_right(self):
        env = VacuumEnvironment({'A': 'Clean', 'B': 'Dirty'}, start_location='A')
        env.execute_action('Right')
        self.assertEqual(env.agent_location, 'B')

    def test_move_left(self):
        env = VacuumEnvironment({'A': 'Dirty', 'B': 'Clean'}, start_location='B')
        env.execute_action('Left')
        self.assertEqual(env.agent_location, 'A')

    def test_noop_does_nothing(self):
        env = VacuumEnvironment({'A': 'Clean', 'B': 'Clean'}, start_location='A')
        env.execute_action('NoOp')
        self.assertEqual(env.state, {'A': 'Clean', 'B': 'Clean'})
        self.assertEqual(env.agent_location, 'A')

    def test_is_fully_clean_true(self):
        env = VacuumEnvironment({'A': 'Clean', 'B': 'Clean'})
        self.assertTrue(env.is_fully_clean())

    def test_is_fully_clean_false(self):
        env = VacuumEnvironment({'A': 'Dirty', 'B': 'Clean'})
        self.assertFalse(env.is_fully_clean())

    def test_invalid_start_location(self):
        with self.assertRaises(ValueError):
            VacuumEnvironment({'A': 'Dirty', 'B': 'Clean'}, start_location='C')


class TestSimpleReflexAgent(unittest.TestCase):

    def setUp(self):
        self.agent = SimpleReflexVacuumAgent()

    def test_dirty_A_cleans(self):
        self.assertEqual(self.agent.choose_action(('A', 'Dirty')), 'Clean')

    def test_clean_A_moves_right(self):
        self.assertEqual(self.agent.choose_action(('A', 'Clean')), 'Right')

    def test_dirty_B_cleans(self):
        self.assertEqual(self.agent.choose_action(('B', 'Dirty')), 'Clean')

    def test_clean_B_moves_left(self):
        self.assertEqual(self.agent.choose_action(('B', 'Clean')), 'Left')

    def test_unknown_percept_raises(self):
        with self.assertRaises(ValueError):
            self.agent.choose_action(('C', 'Dirty'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
