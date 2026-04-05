from langchain.agents import create_agent
from app.common.llm import get_llm
from app.tools.basic_tools import search_web, fetch_url, make_note

def build_researcher_agent(role: str):
    llm = get_llm()
    system_prompt = f"""
    You are a {role} researcher agent inside Atlas Workbench.

    Your job:
    - Investigate the assigned question
    - use tools when needed
    - gather evidence
    - produce concise, source-aware findings
    - avoid making claims without evidence
    - end with a compact structured note

    Output format:
    1. Short answer
    2. Evidence bullets
    3. Source URLs
    4. Open questions
    """

    return create_agent(
        model=llm,
        tools=[search_web, fetch_url, make_note],
        system_prompt=system_prompt
    )

def build_general_expert_agent(role: str):
    llm = get_llm() # can change fn / include model name in future
    system_prompt = f"""
    You are the {role} expert agent inside Atlas Workbench.

    Your job:
    - inspect cluster contents
    - identify what is known
    - identify gaps
    - propose the most valuable next research tasks
    - stay scoped to your specialty
    """
    
    return create_agent(
        model=llm,
        tools=[],
        system_prompt=system_prompt
    )