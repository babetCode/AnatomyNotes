# Anatomical Categories

systems = ['skeletal', 'muscular', 'nervous', 'cardiovascular', 'respiratory', 'digestive', 'endocrine', 'reproductive', 'integumentary']

skeletal = []

axial = []

# vertebrae
cervical = ['c'+str(i+1) for i in range(7)]
thoracic = ['t'+str(i+1) for i in range(12)]
lumbar = ['l'+str(i+1) for i in range(5)]
vertebral_regions = [cervical, thoracic, lumbar]
vertebrae = []
for region in vertebral_regions:
    for vertebra in region:
        vertebrae.append(vertebra)
vertebrae.append('sacrum')

# ordinal suffices
def ordinal(n: int) -> str:
    return f"{n}{'th' if 11 <= n % 100 <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"

# ribs
ribs = [ordinal(n+1)+str(' rib') for n in range(12)]

# pelvis
pelvis = ['ilium', 'ischeum', 'pubis']

#skull
cranial = ['frontal', 'parietal']


