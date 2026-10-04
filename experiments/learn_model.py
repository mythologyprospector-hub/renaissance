"""Minimal Learn capability vertical slice.

This experiment owns only the learning-process boundary. It deliberately does
not prescribe pedagogy, a learner model, content store, scoring system, or UI.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class LearningMaterial:
    content: str
    epistemic_status: str
    provenance: str


@dataclass(frozen=True)
class CapabilityEvidence:
    status: str
    statement: str
    goal: str
    capability_target: str
    transfer_task_id: str
    support_level: str


@dataclass(frozen=True)
class Performance:
    task_id: str
    response: Any
    support_level: str
    demonstrated: bool
    rationale: str = ""


@dataclass(frozen=True)
class Feedback:
    basis: str
    message: str
    source: str = "instruction"


@dataclass(frozen=True)
class Transfer:
    task_id: str
    performance: Performance
    materially_different: bool
    reduced_scaffolding: bool


@dataclass
class LearningEpisode:
    goal: str
    capability_target: str
    baseline: Performance
    activities: list[LearningMaterial] = field(default_factory=list)
    performances: list[Performance] = field(default_factory=list)
    feedback: list[Feedback] = field(default_factory=list)
    adaptations: list[str] = field(default_factory=list)
    transfer: Transfer | None = None

    def add_activity(self, activity: LearningMaterial) -> None:
        if not activity.content.strip():
            raise ValueError("activity content must be non-empty")
        if not activity.epistemic_status.strip():
            raise ValueError("activity epistemic status must be non-empty")
        if not activity.provenance.strip():
            raise ValueError("activity provenance must be non-empty")
        self.activities.append(activity)

    def record_performance(self, performance: Performance) -> None:
        self.performances.append(performance)

    def add_feedback(self, feedback: Feedback) -> None:
        if not feedback.message.strip():
            raise ValueError("feedback message must be non-empty")
        self.feedback.append(feedback)

    def adapt(self, change: str) -> None:
        if not change.strip():
            raise ValueError("adaptation must be non-empty")
        self.adaptations.append(change)

    def record_transfer(self, transfer: Transfer) -> None:
        if not transfer.materially_different:
            raise ValueError("transfer task must be materially different")
        if not transfer.reduced_scaffolding:
            raise ValueError("transfer task must reduce or change scaffolding")
        self.transfer = transfer

    def capability_evidence(self) -> CapabilityEvidence | dict[str, str]:
        if self.transfer is None:
            return {
                "status": "unresolved",
                "reason": "no valid transfer demonstration",
            }
        if not self.transfer.performance.demonstrated:
            return {
                "status": "unresolved",
                "reason": "transfer performance did not demonstrate target capability",
            }
        return CapabilityEvidence(
            status="bounded",
            statement=("Target capability was demonstrated under the recorded transfer conditions."),
            goal=self.goal,
            capability_target=self.capability_target,
            transfer_task_id=self.transfer.task_id,
            support_level=self.transfer.performance.support_level,
        )
