# Atlas Agent Workbench
## Project Overview
A stateful, hierarchical multi-agent research system, designed to move beyond "chat with many agents" and solve complex problems / tasks involving long-running workflows.

Built natively using LangChain and LangGraph, Atlas Workbench operates as a visual research command center. The user defines an objective, and a structured hierarchy of agents (Supervisors, Butlers, Experts and Researchers) collaborate asynchronously to gather evidence, cluster knowledge, and synthesize living reports under the strict supervision of a Human-In-The-Loop (HITL)

## Multi-Agent Architecture
The workspace employs a **Supervisor-Subagent** and **Handoff** pattern, cleanly separating concerns into 5 core roles:

**1. Objective Agent (Mission Owner)**:
    * Interprets user goals
    * Defines acceptance criteria
    * Maintains current state of solutions
    * Determines whether sufficient evidence exists to finalize research

**2. Butler Agent (Organizer):**
    * Reads incoming raw findings from sandbox
    * Group findings by semantic similarity into knowledge clusters
    * Routs data into correct knowledge cluster to prevent context window overload

**3. Expert Agents (Domain Experts):**
    * Specialized roles (Market Expert / Legal Compliance Expert etc.)
    * Inspect specific knowledge clusters to produce summaries, identify gaps, recommend targeted next actions

**4. Researcher Agents (Evidence Collectors):**
    * Browse web / query internal docs / inspect structured sources
    * Stream provenance-rich data back to sandbox

**5. Human Commander:**
    * Oversee "command center" dashboard of all agents
    * Owns final approvals and direction
    * Edits objectives, approves researcher deployments
    * Redirects graph
    * Authorize final synthesis

## Core Technologies & Industry Protocols