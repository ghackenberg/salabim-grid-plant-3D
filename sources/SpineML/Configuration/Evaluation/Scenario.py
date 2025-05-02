class Scenario:

    """Representation of scenarios for evaluation."""

    def __init__(self, name: str) -> None:

        from .Order import Order

        # Remember properties
        self.name = name

        # Remember relations, scenario: Scenario
        self.orders: list[Order] = []

        # Remember instance
        SCENARIOS.append(self)

    def __repr__(self) -> str:
        
        return f"{self.name}"

SCENARIOS: list[Scenario] = []
