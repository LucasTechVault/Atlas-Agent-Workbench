from typing import TypedDict, Any

class WorkspaceState(TypedDict, total=False):
    mission: str
    mission_summary: str
    acceptance_criteria: list[str]

    sandbox_cards: list[dict]
    clusters: list[dict]
    research_tasks: list[dict]

    current_solution: str
    final_report: dict[str, Any] | None

    round_num: int
    max_rounds: int
    auto_approve: bool