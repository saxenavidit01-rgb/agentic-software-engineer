from dotenv import load_dotenv

load_dotenv()

from agents.planner import create_plan
from agents.coder import generate_code
from agents.reviewer import review_code

task = "Build a REST API for employee management"

print("========== PLANNER ==========")

plan = create_plan(task)

print(plan[:800])

print("\n========== CODER ==========")

code = generate_code("Create a FastAPI CRUD application for employees.")

print("Coder function finished")

print(code[:1000])

print("\n========== REVIEWER ==========")

review = review_code(code)

print(review[:1000])