# Autonomous LEGO MINDSTORMS NXT Navigation Architecture

An integration of custom legacy hardware interfaces with industrial robotics middleware. This repository contains the source code, configurations, and deployment launch manifests required to operate a differential drive mobile robot built with the LEGO MINDSTORMS NXT platform under autonomous target tracking, featuring spatial mapping via 2D LiDAR sensors and trajectory processing using the ROS 2 Navigation Stack (Nav2).

---

## Technical Problem Statement & Architecture

### Data Type Incompatibility Mismatch
In modern iterations of the `ros2_control` ecosystem (such as ROS 2 Jazzy), the standard differential drive control plugin (`diff_drive_controller`) enforces strict type-checking on incoming execution buses, demanding temporal encapsulation via `geometry_msgs/msg/TwistStamped`. Conversely, standalone velocity-shaping sub-modules inside the primary Navigation pipeline—specifically the `nav2_collision_monitor` and autonomous docking subsystems—default strictly to publishing raw, un-stamped `geometry_msgs/msg/Twist` structures.

Attempting to mount both nodes onto an identical data line forces a fatal runtime-mismatch where type hashes collide, breaking programmatic telemetry.

### Middleware Gateway Resolution
To settle this structural divergence without crippling localized velocity constraints or degrading real-time control metrics, this architecture implements an isolated topic-routing network managed by a dedicated `twist_stamper` proxy node.



Nav2 Subsystems                      │
│ (MPPI Local Planner / Collision Monitor / Dock Server)  │
└────────────────────────────┬────────────────────────────┘
│
[Topic: Twist]
│
▼
[/cmd_vel_unstamped]
│
▼
┌─────────────────────────────────────────────────────────┐
│                    twist_stamper Node                   │
│   (Injects standard clock headers into raw telemetry)   │
└────────────────────────────┬────────────────────────────┘
│
[Topic: TwistStamped]
│
▼
[/cmd_vel]
│
┌───────────────────┴───────────────────┐
▼                                       ▼
┌─────────────────────────┐             ┌─────────────────────────┐
│   Hardware Controller   │             │ Manual Teleoperation   │
│  (ros2_control_node)    │             │  (stamped:=true flag)   │
└─────────────────────────┘             └─────────────────────────┘
