
#My incorrect solution
import re

print(sorted(dir(re)))

#correct solution
import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))
