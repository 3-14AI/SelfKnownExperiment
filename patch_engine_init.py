with open('src/universe/engine.py', 'r') as f:
    text = f.read()

import re

search1 = "is_shelter_dweller=False):"

replace1 = "is_shelter_dweller=False, is_fire_dancer=False):"

search2 = "self.is_rain_dancer = is_rain_dancer"
replace2 = "self.is_rain_dancer = is_rain_dancer\n        self.is_fire_dancer = is_fire_dancer"

if search1 in text:
    text = text.replace(search1, replace1)
else:
    print("Match 1 not found")

if search2 in text:
    text = text.replace(search2, replace2)
else:
    print("Match 2 not found")

with open('src/universe/engine.py', 'w') as f:
    f.write(text)
