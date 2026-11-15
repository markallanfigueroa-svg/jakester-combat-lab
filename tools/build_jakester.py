"""Officer Jakester sculpt-and-rig starter. Run in Blender 4.x:
blender --background --python tools/build_jakester.py
Produces assets/jakester_first_pass.glb. This is an authored FIRST PASS, not
a reference-perfect sculpt or fully weight-painted combat rig.
"""
import bpy, math, os
from mathutils import Vector
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
def material(name, color, metallic=0, roughness=.7):
 m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
 bs=m.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(*color,1)
 bs.inputs['Metallic'].default_value=metallic;bs.inputs['Roughness'].default_value=roughness
 return m
skin=material('warm reddish pig skin',(.66,.27,.22));snout=material('pig snout',(.79,.37,.32))
shirt=material('burnt orange plaid base',(.43,.17,.09));black=material('black leather tactical',(.055,.045,.04))
pants=material('charcoal cargo fabric',(.085,.087,.11));gold=material('gold sheriff insignia',(.8,.49,.09),.72)
hair=material('dark hair and beard',(.042,.025,.02));metal=material('steel hardware',(.32,.32,.32),.75)
def ell(name,loc,scale,mat,segments=32,rings=20):
 bpy.ops.mesh.primitive_uv_sphere_add(segments=segments,ring_count=rings,location=loc)
 o=bpy.context.object;o.name=name;o.scale=scale;o.data.materials.append(mat)
 bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
 bpy.ops.object.shade_smooth();return o
def capsule(name,a,b,r,mat):
 a,b=Vector(a),Vector(b);mid=(a+b)/2;v=b-a
 o=ell(name,mid,(r,r,v.length/2+r*.35),mat);o.rotation_euler=v.to_track_quat('Z','Y').to_euler();return o
# Natural broad shoulder-to-waist silhouette; pieces intentionally separate for later skinning.
ell('massive tapered ribcage',(0,0,2.33),(.79,.45,.66),shirt)
ell('tactical chest armor',(0,-.12,2.38),(.70,.45,.49),black)
ell('pelvis',(0,0,1.57),(.51,.34,.35),pants)
ell('thick neck',(0,0,2.93),(.28,.28,.30),skin)
ell('head',(0,-.025,3.28),(.42,.37,.43),skin)
ell('projecting pig muzzle',(0,-.36,3.20),(.30,.23,.17),snout)
for x in [-.12,.12]:ell('nostril', (x,-.56,3.21),(.055,.021,.065),hair)
ell('beard jaw',(0,-.10,3.03),(.36,.34,.22),hair)
ell('spiky hair mass',(0,.025,3.63),(.40,.31,.14),hair)
for side in [-1,1]:
 ell('pig ear', (side*.43,-.015,3.49),(.19,.09,.17),skin)
 ell('angry brow',(side*.19,-.34,3.43),(.18,.05,.06),hair)
 ell('eye',(side*.19,-.375,3.35),(.075,.035,.045),black)
 capsule('bulging upper arm',(side*.73,0,2.69),(side*.88,-.03,2.12),.265,shirt)
 capsule('muscular forearm',(side*.88,-.03,2.12),(side*.72,-.29,1.72),.22,skin)
 ell('fingerless glove',(side*.72,-.29,1.68),(.19,.16,.19),black)
 capsule('cargo thigh',(side*.31,0,1.49),(side*.37,-.06,.88),.30,pants)
 capsule('calf',(side*.37,-.06,.88),(side*.37,-.11,.34),.23,pants)
 ell('knee armor',(side*.37,-.30,.86),(.23,.12,.21),metal)
 ell('combat boot',(side*.37,-.24,.19),(.24,.40,.22),black)
 ell('vest pouch',(side*.30,-.53,2.17),(.19,.13,.22),black)
ell('sheriff badge',( .31,-.55,2.61),(.14,.06,.14),gold)
ell('star belt buckle',(0,-.37,1.67),(.17,.08,.17),gold)
ell('radio',(-.53,-.35,2.75),(.14,.14,.23),black)
ell('side holster',(-.53,-.20,1.31),(.16,.18,.32),black)
# Bone structure is a scaffold. Mesh skin weights and animation clips are NOT finished.
bpy.ops.object.armature_add(enter_editmode=True,location=(0,0,0))
rig=bpy.context.object;rig.name='Jakester_rig_scaffold'
eb=rig.data.edit_bones;eb.remove(eb[0])
def bone(name,a,b,parent=None):
 q=eb.new(name);q.head=a;q.tail=b
 if parent:q.parent=eb[parent]
bone('hips',(0,0,1.55),(0,0,1.9))
bone('spine',(0,0,1.9),(0,0,2.6),'hips')
bone('neck',(0,0,2.6),(0,0,3.12),'spine')
bone('head',(0,0,3.12),(0,0,3.7),'neck')
for s,label in [(-1,'L'),(1,'R')]:
 bone('upper_arm_'+label,(s*.60,0,2.68),(s*.88,0,2.12),'spine')
 bone('forearm_'+label,(s*.88,0,2.12),(s*.72,-.29,1.7),'upper_arm_'+label)
 bone('thigh_'+label,(s*.30,0,1.55),(s*.37,-.06,.88),'hips')
 bone('shin_'+label,(s*.37,-.06,.88),(s*.37,-.11,.3),'thigh_'+label)
bpy.ops.object.mode_set(mode='OBJECT')
out=os.path.abspath('assets/jakester_first_pass.glb');os.makedirs(os.path.dirname(out),exist_ok=True)
bpy.ops.export_scene.gltf(filepath=out,export_format='GLB')
print('Exported first-pass Jakester GLB:',out)
