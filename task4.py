good = r"""  
   /\   /\   Todd Vargo
  //\\_//\\     ____
  \_     _/    /   /
   / * * \    /^^^]
   \_\O/_/    [   ]
    /   \_    [   /
    \     \_  /  /
     [ [ /  \/ _/
    _[ [ \  /_/
    """
bad = r"""
              ___      .-""-.      ___
              \  "-.  /      \  .-"  /
               > -=.\/        \/.=- <
               > -='/\        /\'=- <
              /__.-'  \      /  '-.__\
         jgs           '-..-'
"""
drawbridge_raised = True
if not drawbridge_raised:
    outcome = ("Thunder: Go on and thunder through")
    print(good)
else:
    outcome = ("Doom: wow youre so dead")
    print(bad)
print(outcome)