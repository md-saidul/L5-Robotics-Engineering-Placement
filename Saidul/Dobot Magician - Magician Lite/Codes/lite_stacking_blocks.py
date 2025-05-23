from DobotEDU import *

m_lite.set_homecmd()

m_lite.set_endeffector_suctioncup(enable=True, on=False)
m_lite.set_ptpcmd(ptp_mode=2, x=336, y=-30, z=-42.38, r=0)
m_lite.set_endeffector_suctioncup(enable=True, on=True)
m_lite.set_ptpcmd(ptp_mode=9, x=336, y=-30, z=20, r=0)
m_lite.set_ptpcmd(ptp_mode=9, x=336, y=-69, z=20, r=0)
m_lite.set_ptpcmd(ptp_mode=9, x=336, y=-69, z=-42.38, r=0)
m_lite.set_endeffector_suctioncup(enable=True, on=False)

m_lite.set_homecmd()
m_lite.set_ptpcmd(ptp_mode=2, x=317.65, y=-30, z=-42.38, r=0)
m_lite.set_endeffector_suctioncup(enable=True, on=True)
m_lite.set_ptpcmd(ptp_mode=9, x=317.65, y=-30, z=20, r=0)
m_lite.set_ptpcmd(ptp_mode=9, x=336, y=-69, z=20, r=0)
m_lite.set_ptpcmd(ptp_mode=9, x=336, y=-69, z=-30, r=0)
m_lite.set_endeffector_suctioncup(enable=True, on=False)

m_lite.set_homecmd()
m_lite.set_ptpcmd(ptp_mode=2, x=299.30, y=-30, z=-42.38, r=0)
m_lite.set_endeffector_suctioncup(enable=True, on=True)
m_lite.set_ptpcmd(ptp_mode=9, x=299.30, y=-30, z=20, r=0)
m_lite.set_ptpcmd(ptp_mode=9, x=336, y=-69, z=20, r=0)
m_lite.set_ptpcmd(ptp_mode=9, x=336, y=-69, z=-20, r=0)
m_lite.set_endeffector_suctioncup(enable=True, on=False)

m_lite.set_homecmd()
m_lite.set_ptpcmd(ptp_mode=2, x=285, y=-30, z=-42.38, r=0)
m_lite.set_endeffector_suctioncup(enable=True, on=True)
m_lite.set_ptpcmd(ptp_mode=9, x=285, y=-30, z=20, r=0)
m_lite.set_ptpcmd(ptp_mode=9, x=336, y=-69, z=20, r=0)
m_lite.set_ptpcmd(ptp_mode=9, x=336, y=-69, z=-10, r=0)
m_lite.set_endeffector_suctioncup(enable=True, on=False)

m_lite.set_homecmd()