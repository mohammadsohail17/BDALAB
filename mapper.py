
#!/usr/bin/env python 
  
#mapper logic
import sys

for line in sys.stdin:
    line=line.strip()
    words=line.split()

    for word in words:
        print(f"{word}\t1")