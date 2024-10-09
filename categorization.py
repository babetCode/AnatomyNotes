import pandas as pd

# ordinal suffices
def ordinal(n: int) -> str:
    return f"{n}{'th' if 11 <= n % 100 <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"

def bilateral(lst: list) -> list:
    bilateral = []
    for item in lst:
        bilateral.append(item+' (right)')
        bilateral.append(item+' (left)')
    return bilateral

# systems = ['skeletal', 'muscular', 'nervous', 'cardiovascular', 'respiratory', 'digestive', 'endocrine', 'reproductive', 'integumentary']

def get_skeleton():

    # The 29 "head_bones" consist of 8 cranial bones, 14 facial bones, the hyoid bone, and 6 auditory (ear) bones.
    cranial = ['frontal', 'occipital', 'sphenoid', 'ethmoid']+bilateral(['parietal', 'temporal'])
    facial = ['mandible', 'vomer']+bilateral(['maxilla', 'zygomatic', 'lacrimal', 'nasal', 'turbinate', 'palatine'])
    auditory = bilateral(['incus', 'malleus', 'stapes'])
    head_bones = cranial + facial + auditory + ['hyoid']

    # The 53 "trunk_bones" consist of 26 vertebrae, 24 ribs and the 3 sternum bones.
    vertebrae = ['c'+str(i+1) for i in range(7)] + ['t'+str(i+1) for i in range(12)] + ['l'+str(i+1) for i in range(5)] + ['sacrum', 'coccyx']
    ribs = bilateral([ordinal(n+1)+' rib' for n in range(12)])
    sternum = ['sternum (manubrium)', 'sternum (body)', 'sternum (xiphoid process)']
    trunk_bones = vertebrae + ribs + sternum

    # The 64 "upper_extremity_bones" consist of 10 shoulder and arm, 16 wrist and 38 hand bones.
    shoulder_arm = bilateral(['clavicle', 'scapula', 'humerus', 'radius', 'ulna'])
    wrist = bilateral(['scaphoid', 'lunate', 'triquetrum', 'pisiform', 'trapezium', 'trapezoid', 'capitate', 'hamate'])
    hand = bilateral([ordinal(n+1)+' metacarpal' for n in range(5)] + [ordinal(n+1)+' proximal phalange (hand)' for n in range(5)] + [ordinal(n+2)+' middle phalange (hand)' for n in range(4)] + [ordinal(n+1)+' distal phalange (hand)' for n in range(5)])
    upper_extremity_bones = shoulder_arm + wrist + hand


    # The 66 "lower_extremity_bones" consist of 10 hip and leg, 14 ankle and 38 foot bones.
    hip_leg = bilateral(['ilium', 'ischium', 'pubis', 'femur', 'tibia', 'fibula', 'patella'])
    ankle = bilateral(['talus', 'calcaneus', 'navicular', 'cuboid', 'medial cuneiform', 'intermediate cuneiform', 'lateral cuneiform'])
    foot = bilateral([ordinal(n+1)+' metatarsal' for n in range(5)] + [ordinal(n+1)+' proximal phalange' for n in range(5)] + [ordinal(n+2)+' middle phalange' for n in range(4)] + [ordinal(n+1)+' distal phalange' for n in range(5)])
    lower_extremity_bones = hip_leg + ankle + foot


    skeleton = head_bones + trunk_bones + upper_extremity_bones + lower_extremity_bones
    return skeleton

def main():
    skeleton = get_skeleton()
    print(len(skeleton))

main()

