good = r"""                   __       __
                  / <`     '> \
                 (  / @   @ \  )
                  \(_ _\_/_ _)/
                (\ `-/     \-' /)
                 "===\     /==="
                  .==')___(`==.    hjw
                 ' .='     `=.
"""
bad = r""" 
  __           _   
 / _|         | |  
| |_ __ _ _ __| |_ 
|  _/ _` | '__| __|
| || (_| | |  | |_ 
|_| \__,_|_|   \__|
                   """
escaped = False
if escaped:
    outcome = ("Legend: Wow nice job!")
    print(good)
else:
    outcome = ("Doom: Nice job youre dead")
    print(bad)
print(outcome)