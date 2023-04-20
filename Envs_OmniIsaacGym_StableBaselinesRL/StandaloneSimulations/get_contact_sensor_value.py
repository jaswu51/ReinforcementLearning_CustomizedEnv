from omni.isaac.kit import SimulationApp
simulation_app = SimulationApp({"headless": False}) # we can also run as headless.

from omni.isaac.core import World
from omni.isaac.core.objects import DynamicSphere
from omni.isaac.isaac_sensor import _isaac_sensor
from omni.isaac.core.utils.viewports import set_camera_view
import omni.physxdemos as demo
import omni.physx as _physx
import numpy as np
from pxr import Gf
import omni.kit.commands


world = World(stage_units_in_meters=1.0)
world.scene.add_default_ground_plane()
set_camera_view(eye=np.array([30, 30, 40]), target=np.array([0, 0, 0]))

sphere = world.scene.add(
                    DynamicSphere(
                        prim_path="/World/Sphere", 
                        name="sphere",
                        position=np.array([0, 0, 15.91708]), # Using the current stage units which is in meters by default.
                        radius=0.3, # most arguments accept mainly numpy arrays.
                        color=np.array([0, 0, 1.0]),
                        mass = 100,
                        visible = True,
                            # RGB channels, going from 0-1
                        )
                    )
sensor_path = "/World/Sphere"       


world.reset()



sphere_egg_breaker = world.scene.get_object("sphere_egg_breaker")


result, sensor = omni.kit.commands.execute(
                "IsaacSensorCreateContactSensor",
                path="/sensor",
                parent= sensor_path,
                min_threshold=0,
                max_threshold=10000000,
                color= (1, 0, 0, 1),
                radius=0.4, #0.01
                sensor_period=0.5,
                visualize=True,)

_cs = _isaac_sensor.acquire_contact_sensor_interface()   


i = 0
while simulation_app.is_running():
    world.step(render=True)
    readings = _cs.get_sensor_sim_reading(sensor_path +"/sensor")
    print("Contact sensor: ", readings.inContact, readings.time, readings.value)
    print(i)       
    
simulation_app.close() # close Isaac Sim