# Anatomical Categories

# ordinal suffices
def ordinal(n: int) -> str:
    return f"{n}{'th' if 11 <= n % 100 <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"

def lr(lst: list) -> list:
    bilateral = []
    for item in lst:
        bilateral.append(item+' (right)')
        bilateral.append(item+' (left)')
    return bilateral

# systems = ['skeletal', 'muscular', 'nervous', 'cardiovascular', 'respiratory', 'digestive', 'endocrine', 'reproductive', 'integumentary']

# trunk
cervical = ['c'+str(i+1) for i in range(7)]
thoracic = ['t'+str(i+1) for i in range(12)]
lumbar = ['l'+str(i+1) for i in range(5)]
vertebral_regions = [cervical, thoracic, lumbar]
vertebrae = []
for region in vertebral_regions:
    for vertebra in region:
        vertebrae.append(vertebra)
vertebrae.append('sacrum')
vertebrae.append('coccyx')

ribs = [ordinal(n+1)+str(' rib') for n in range(12)]

pelvis = ['ilium', 'ischeum', 'pubis']

print(lr(pelvis))

sternum = ['sternum (manubrium)', 'sternum (body)', 'sternum (xiphoid process)']

#skull
cranial = ['frontal', 'parietal', 'temporal', 'occipital']
facial = ['maxilla', 'mandible', 'zygomatic', 'lacrimal', 'nasal', 'turbinate', 'vomer', 'palatine']
ear = ['incus', 'malleus', 'stapes']
skull_regions = [cranial, facial, ear]
skull = []
for region in skull_regions:
    for bone in region:
        skull.append(bone)
skull.append('hyoid')

