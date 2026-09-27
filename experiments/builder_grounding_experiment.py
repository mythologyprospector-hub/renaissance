"""Bounded experiment for Renaissance targeted builder grounding.

This models document-routing decisions. It does not measure model token usage.
It exists to test whether task classification can avoid unnecessary authority
preloading while broadening when the task crosses a relevant boundary.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

AUTHORITY_MAP = {
    "STATUS.md", "CHARTER.md", "CONSTITUTION.md", "PRINCIPLES.md",
    "BOUNDARIES.md", "EPISTEMOLOGY.md", "GOVERNANCE.md",
    "CHANGE_CONTROL.md", "DECISIONS/", "ARCHITECTURE.md",
}

class TaskClass(str, Enum):
    ROUTINE = "routine"
    ARCHITECTURAL = "architectural"
    FOUNDATIONAL = "foundational"
    UNCERTAIN = "uncertain"

@dataclass(frozen=True)
class Mission:
    task_class: TaskClass
    source_of_truth: str
    applicable_decisions: tuple[str, ...] = ()
    architectural_boundary: bool = False
    foundational_boundary: bool = False
    repository_wide: bool = False
    unresolved_conflict: bool = False
    experiment_promotion: bool = False
    reconsider_decision: bool = False

def required_grounding(mission: Mission) -> set[str]:
    """Return the minimum authority set this experiment says to inspect."""
    required = {mission.source_of_truth}
    required.update(mission.applicable_decisions)
    broad = (
        mission.task_class in {TaskClass.FOUNDATIONAL, TaskClass.UNCERTAIN}
        or mission.foundational_boundary
        or mission.repository_wide
        or mission.unresolved_conflict
        or mission.experiment_promotion
        or mission.reconsider_decision
    )
    if mission.architectural_boundary or mission.task_class == TaskClass.ARCHITECTURAL:
        required.add("ARCHITECTURE.md")
    if broad:
        required.update(AUTHORITY_MAP)
    return required

def should_reopen_decision(*, new_evidence=False, contradiction=False,
                           implementation_failure=False, changed_requirement=False,
                           explicit_reconsideration=False,
                           boundary_crossing_consequence=False) -> bool:
    """Reopen only when an established trigger exists."""
    return any((new_evidence, contradiction, implementation_failure,
                changed_requirement, explicit_reconsideration,
                boundary_crossing_consequence))