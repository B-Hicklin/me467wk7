from hazardous_warehouse_env import HazardousWarehouseEnv
from hazardous_warehouse_viz import configure_rn_example_layout
from warehouse_z3_FOL_agent import WarehouseZ3Agent
env = HazardousWarehouseEnv(seed=0)
configure_rn_example_layout(env)
print("True state (hidden from agent):")
print(env.render(reveal=True))
agent = WarehouseZ3Agent(env)
agent.run(verbose=True)