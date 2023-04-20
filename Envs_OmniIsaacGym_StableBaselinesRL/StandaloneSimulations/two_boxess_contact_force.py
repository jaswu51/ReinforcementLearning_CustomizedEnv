from omni.isaac.kit import SimulationApp
simulation_app = SimulationApp({"headless": False}) # we can also run as headless.

import asyncio
import numpy as np
from omni.isaac.core.world import World
from omni.isaac.core.prims import RigidPrimView#,RigidContactView
from omni.isaac.core.objects import DynamicCuboid

world = World()
world.scene.add_default_ground_plane()

# create three rigid cubes sitting on top of three others
for i in range(3):
    DynamicCuboid(prim_path=f"/World/bottom_box_{i+1}", size=2, color=np.array([0.5, 0, 0]), mass=1.0)
    DynamicCuboid(prim_path=f"/World/top_box_{i+1}", size=2, color=np.array([0, 0, 0.5]), mass=1.0)

# as before, create RigidContactView to manipulate bottom boxes but this time specify top boxes as filters to the view object
# this allows receiving contact forces between the bottom boxes and top boxes
bottom_box_view = RigidPrimView(
    prim_paths_expr="/World/bottom_box_*",
    positions=np.array([[0, 0, 1.0], [-5.0, 0, 1.0], [5.0, 0, 1.0]]),
    # contact_filter_prim_paths_expr=["/World/top_box_*"],
)
# create a RigidContactView to manipulate top boxes
top_box_view = RigidPrimView(
    prim_paths_expr="/World/top_box_*",
    positions=np.array([[0.0, 0, 3.0], [-5.0, 0, 3.0], [5.0, 0, 3.0]]),
    # track_contact_forces=True,
)

# bottom_box_contact_view = RigidContactView(
#     prim_paths_expr="/World/bottom_box_*",
#     positions=np.array([[0, 0, 1.0], [-5.0, 0, 1.0], [5.0, 0, 1.0]]),
#     filter_paths_expr=["/World/top_box_*"],
# )

world.scene.add(top_box_view)
world.scene.add(bottom_box_view)
# world.scene.add(bottom_box_contact_view)

# await world.reset_async()
world.reset()


for i in range(50000):
    # net contact forces acting on the bottom boxes
    print(top_box_view.get_net_contact_forces())
    # contact forces between the top and the bottom boxes
    print(top_box_view.get_contact_force_matrix())
    world.step(render=True)
simulation_app.close() # close Isaac Sim
