import open3d as o3d
import numpy as np


filename = "outside_g03_closed (Frame 140).ply"
pcd = o3d.io.read_point_cloud(filename)
# o3d.io.write_point_cloud("outside.pcd", pcd)

# # Load your point cloud
# pcd = o3d.io.read_point_cloud("outside.pcd")

# Define floor grid with spacing for dots
x = np.arange(-10, 10, 0.5)  # grid points every 0.5m
y = np.arange(-10, 10, 0.5)
xx, yy = np.meshgrid(x, y)
zz = np.full_like(xx, -1.75)  # floor at z = -2m

floor_points = np.vstack((xx.ravel(), yy.ravel(), zz.ravel())).T
floor_pcd = o3d.geometry.PointCloud()
floor_pcd.points = o3d.utility.Vector3dVector(floor_points)

# Combine with your original cloud
combined = pcd + floor_pcd
o3d.io.write_point_cloud("outside_g03_closed.pcd", combined, write_ascii=True)
print('done')
