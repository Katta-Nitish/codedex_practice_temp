from pathlib import Path
p=Path("C:/")
for i in p.iterdir():
    if i.is_dir():
        print(i)
