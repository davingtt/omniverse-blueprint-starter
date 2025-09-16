# Minimal LAS/LAZ loader example using laspy — converts point cloud to simple mesh (placeholder)
import os
import laspy
import numpy as np

INPUT = os.path.join('..','sample_data','site.las')
OUTPUT = os.path.join('..','output','site_points.npy')


def load_las(path):
    with laspy.open(path) as fh:
        points = fh.read().points
        xyz = np.vstack((points['X'], points['Y'], points['Z'])).T
        return xyz


if __name__ == '__main__':
    if not os.path.exists(INPUT):
        print('Place a LAS/LAZ file at', INPUT)
    else:
        pts = load_las(INPUT)
        os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
        np.save(OUTPUT, pts)
        print('Saved point array to', OUTPUT)
