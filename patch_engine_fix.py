with open("src/universe/engine.py") as f:
    content = f.read()
target_search = "child_is_hypnotic, is_tracker=child_is_tracker, is_empathic=child_is_empathic)"
target_replace = "child_is_hypnotic, is_tracker=child_is_tracker, is_empathic=child_is_empathic)"
content = content.replace(target_search, target_replace)
with open("src/universe/engine.py", "w") as f:
    f.write(content)
