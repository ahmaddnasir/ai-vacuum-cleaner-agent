"""
AI Vacuum Cleaner Agent
=======================
A Simple Reflex Agent implementation based on the two-cell vacuum world
described in Russell & Norvig, "Artificial Intelligence: A Modern Approach."

Environment
-----------
  - Two locations: A (left) and B (right)
  - Each location can be Clean or Dirty
  - The agent starts at a given location and can perceive its current state

Percept
-------
  A tuple: (location, status)
  Example: ('A', 'Dirty') or ('B', 'Clean')

Actions
-------
  - 'Clean'  : Clean the current location
  - 'Right'  : Move from A to B
  - 'Left'   : Move from B to A
  - 'NoOp'   : Do nothing (environment is already clean)
"""


# ---------------------------------------------------------------------------
# Environment
# ---------------------------------------------------------------------------

class VacuumEnvironment:
    """
    Represents the two-cell vacuum world.

    Attributes
    ----------
    state : dict
        Maps location names to their cleanliness status ('Clean' or 'Dirty').
    agent_location : str
        The current location of the agent ('A' or 'B').
    """

    def __init__(self, initial_state: dict, start_location: str = 'A'):
        """
        Parameters
        ----------
        initial_state : dict
            Example: {'A': 'Dirty', 'B': 'Clean'}
        start_location : str
            Where the agent begins. Must be a key in initial_state.
        """
        if start_location not in initial_state:
            raise ValueError(f"start_location '{start_location}' not found in initial_state.")
        self.state = dict(initial_state)
        self.agent_location = start_location

    def percept(self) -> tuple:
        """Return what the agent currently perceives: (location, status)."""
        return (self.agent_location, self.state[self.agent_location])

    def execute_action(self, action: str):
        """
        Apply an action to the environment.

        Parameters
        ----------
        action : str
            One of 'Clean', 'Right', 'Left', 'NoOp'.
        """
        location = self.agent_location

        if action == 'Clean':
            self.state[location] = 'Clean'
        elif action == 'Right':
            if 'B' in self.state:
                self.agent_location = 'B'
        elif action == 'Left':
            if 'A' in self.state:
                self.agent_location = 'A'
        elif action == 'NoOp':
            pass  # Nothing to do
        else:
            raise ValueError(f"Unknown action: '{action}'")

    def is_fully_clean(self) -> bool:
        """Return True if every location is Clean."""
        return all(status == 'Clean' for status in self.state.values())


# ---------------------------------------------------------------------------
# Simple Reflex Agent
# ---------------------------------------------------------------------------

class SimpleReflexVacuumAgent:
    """
    A Simple Reflex Agent for the vacuum world.

    Decision logic
    --------------
    The agent maps the current percept directly to an action using a
    condition-action rule table. It has no memory of past states.

    Rule table
    ----------
    ('A', 'Dirty')  ->  'Clean'
    ('A', 'Clean')  ->  'Right'
    ('B', 'Dirty')  ->  'Clean'
    ('B', 'Clean')  ->  'Left'
    """

    # Condition-action rules (the agent's entire "policy")
    RULES = {
        ('A', 'Dirty'): 'Clean',
        ('A', 'Clean'): 'Right',
        ('B', 'Dirty'): 'Clean',
        ('B', 'Clean'): 'Left',
    }

    def choose_action(self, percept: tuple) -> str:
        """
        Select an action based solely on the current percept.

        Parameters
        ----------
        percept : tuple
            (location, status) from the environment.

        Returns
        -------
        str
            The action to take.
        """
        action = self.RULES.get(percept)
        if action is None:
            raise ValueError(f"No rule defined for percept: {percept}")
        return action


# ---------------------------------------------------------------------------
# Simulation runner
# ---------------------------------------------------------------------------

def run_simulation(initial_state: dict, start_location: str = 'A', max_steps: int = 10):
    """
    Run the vacuum agent in the given environment and print a step-by-step trace.

    Parameters
    ----------
    initial_state : dict
        Initial cleanliness of each cell, e.g. {'A': 'Dirty', 'B': 'Clean'}.
    start_location : str
        Starting position of the agent.
    max_steps : int
        Safety limit to prevent infinite loops (the simple reflex agent can
        loop once the environment is clean — this stops it).
    """
    env = VacuumEnvironment(initial_state, start_location)
    agent = SimpleReflexVacuumAgent()

    print("=" * 50)
    print("  Vacuum Cleaner Agent Simulation")
    print("=" * 50)
    print(f"  Initial state : {env.state}")
    print(f"  Agent starts  : Location {env.agent_location}")
    print("=" * 50)
    print()

    for step in range(1, max_steps + 1):
        # Stop early if the environment is fully clean
        if env.is_fully_clean():
            print(f"  All locations are clean. Stopping after {step - 1} step(s).")
            break

        percept = env.percept()
        action = agent.choose_action(percept)

        print(f"  Step {step:02d}")
        print(f"    Percept  : {percept}")
        print(f"    Action   : {action}")

        env.execute_action(action)

        print(f"    State    : {env.state}  |  Agent at: {env.agent_location}")
        print()
    else:
        # Reached max_steps without finishing
        if not env.is_fully_clean():
            print(f"  Reached step limit ({max_steps}). Environment not fully clean.")
        else:
            print(f"  Done in {max_steps} step(s).")

    print("=" * 50)
    print(f"  Final state   : {env.state}")
    clean = env.is_fully_clean()
    print(f"  Mission status: {'SUCCESS — environment is clean.' if clean else 'INCOMPLETE'}")
    print("=" * 50)


# ---------------------------------------------------------------------------
# Entry point — demo scenarios
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    print("\n--- Scenario 1: Both locations dirty, start at A ---\n")
    run_simulation(initial_state={'A': 'Dirty', 'B': 'Dirty'}, start_location='A')

    print("\n--- Scenario 2: Only B is dirty, start at A ---\n")
    run_simulation(initial_state={'A': 'Clean', 'B': 'Dirty'}, start_location='A')

    print("\n--- Scenario 3: Only A is dirty, start at A ---\n")
    run_simulation(initial_state={'A': 'Dirty', 'B': 'Clean'}, start_location='A')

    print("\n--- Scenario 4: Both locations already clean, start at A ---\n")
    run_simulation(initial_state={'A': 'Clean', 'B': 'Clean'}, start_location='A')
