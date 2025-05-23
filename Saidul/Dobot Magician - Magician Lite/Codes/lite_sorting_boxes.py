from DobotEDU import *

m_lite.set_homecmd()

m_lite.set_endeffector_gripper(enable=True, on=False)
m_lite.set_ptpcmd(ptp_mode=2, x=225.47, y=-40.26, z=19.24, r=0)
m_lite.set_endeffector_gripper(enable=True, on=True)
m_lite.set_ptpcmd(ptp_mode=9, x=225.47, y=-40.26, z=130, r=0)
m_lite.set_ptpcmd(ptp_mode=9, x=69.20, y=-209.92, z=130, r=0)
m_lite.set_ptpcmd(ptp_mode=9, x=69.20, y=-209.92, z=20, r=0)
m_lite.set_endeffector_gripper(enable=True, on=False)

m_lite.set_homecmd()
m_lite.set_endeffector_gripper(enable=True, on=False)
m_lite.set_ptpcmd(ptp_mode=2, x=225.90, y=-120, z=19.24, r=0)
m_lite.set_endeffector_gripper(enable=True, on=True)
m_lite.set_ptpcmd(ptp_mode=9, x=225.47, y=-120, z=130, r=0)
m_lite.set_ptpcmd(ptp_mode=9, x=69.20, y=-209.92, z=130, r=0)
m_lite.set_ptpcmd(ptp_mode=9, x=69.20, y=-209.92, z=40, r=0)
m_lite.set_endeffector_gripper(enable=True, on=False)

m_lite.set_homecmd()