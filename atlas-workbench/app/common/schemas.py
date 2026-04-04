from pydantic import BaseModel, Field
from typing import Literal


class ObjectivePlan(BaseModel):
    mission_summary: str
    acceptance_criteria: list[str] = Field(default_factory=list)
    seed_research_questions: list[str] = Field(default_factory=list)


class SandboxCard(BaseModel):
    card_id: str
    title: str
    content: str
    source_urls: list[str] = Field(default_factory=list)
    agent_role: str
    cluster_id: str | None = None


class ClusterSummary(BaseModel):
    cluster_id: str
    title: str
    summary: str
    card_ids: list[str] = Field(default_factory=list)


class ExpertTask(BaseModel):
    task_id: str
    cluster_id: str
    expert_role: Literal["market", "technical", "legal", "pricing", "general"]
    question: str
    rationale: str


class FinalSynthesis(BaseModel):
    executive_summary: str
    key_findings: list[str] = Field(default_factory=list)
    unresolved_risks: list[str] = Field(default_factory=list)
    recommendation: str