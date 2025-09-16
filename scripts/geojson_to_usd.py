# Example: GeoJSON -> USD (simplified)
# Note: For full USD/Omniverse use, run inside Omniverse Kit or an environment with pxr USD.

import json
import os

try:
    from pxr import Usd, UsdGeom, Gf
    USD_AVAILABLE = True
except Exception:
    USD_AVAILABLE = False

INPUT = os.path.join('..','sample_data','buildings.geojson')
OUTPUT = os.path.join('..','output','buildings.usd')


def load_geojson(path):
    with open(path,'r',encoding='utf-8') as f:
        return json.load(f)


def create_usd_from_geojson(geojson, out_path):
    if not USD_AVAILABLE:
        print('USD Python bindings not available in this environment. Run this script inside Omniverse Kit or an environment with pxr.')
        return
    stage = Usd.Stage.CreateNew(out_path)
    for i,feature in enumerate(geojson.get('features',[])):
        geom = feature.get('geometry')
        props = feature.get('properties',{})
        prim_path = '/Feature_{}'.format(i)
        mesh = UsdGeom.Xform.Define(stage, prim_path)
        mesh_prim = UsdGeom.Mesh.Define(stage, prim_path + '/Mesh')
        # Simplified: create a bounding box as mesh
        bbox = props.get('bbox')
        if bbox:
            minx,miny,maxx,maxy = bbox
            size_x = maxx - minx
            size_y = maxy - miny
            points = [Gf.Vec3f(0,0,0), Gf.Vec3f(size_x,0,0), Gf.Vec3f(size_x,size_y,0), Gf.Vec3f(0,size_y,0)]
            mesh_prim.CreatePointsAttr(points)
    stage.GetRootLayer().Save()
    print('USD written to', out_path)


if __name__ == '__main__':
    if not os.path.exists(INPUT):
        print('Place a GeoJSON file at', INPUT)
    else:
        geo = load_geojson(INPUT)
        os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
        create_usd_from_geojson(geo, OUTPUT)
