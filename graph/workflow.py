from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.planner import create_plan
from agents.coder import generate_code
from agents.reviewer import review_code
from tools.logger import logger


class AgentState(TypedDict):
    task: str
    plan: str
    code: str
    review: str
    retries: int


def planner_node(state: AgentState):

    logger.info("Planner Agent Started")
    print("\n========== PLANNER NODE ==========")

    plan = create_plan(state["task"])

    return {
        "plan": plan
    }


def coder_node(state: AgentState):

    logger.info("Coder Agent Started")
    print("\n========== CODER NODE ==========")

    code = generate_code(
    "Create a production-ready FastAPI CRUD application for employee management."
)

    return {
        "code": code
    }


def reviewer_node(state: AgentState):

    logger.info("Reviewer Agent Started")
    print("\n========== REVIEWER NODE ==========")

    review = review_code(state["code"])

    return {
        "review": review,
        "retries": state["retries"] + 1
    }


def review_decision(state: AgentState):

    if state["retries"] >= 2:
        print("Maximum retries reached.")
        return "approved"

    if state["review"].startswith("STATUS: APPROVED"):
        return "approved"

    return "rejected"


graph = StateGraph(AgentState)

graph.add_node("planner", planner_node)
graph.add_node("coder", coder_node)
graph.add_node("reviewer", reviewer_node)

graph.set_entry_point("planner")

graph.add_edge("planner", "coder")
graph.add_edge("coder", "reviewer")
graph.add_edge("reviewer", END)

workflow = graph.compile()