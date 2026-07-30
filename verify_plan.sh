echo "Checking lines around 1707"
sed -n '1705,1710p' src/universe/engine.py
echo "Checking lines around 1865"
sed -n '1863,1868p' src/universe/engine.py
echo "Checking stamina recovery"
grep -n "recovery = " src/universe/engine.py
