good = r"""  .--,       .--,
    ( (  \.---./  ) )
     '.__/o   o\__.'
        {=  ^  =}
         >  -  <
        /       \
       //       \\
      //|   .   |\\
      "'\       /'"_.-~^`'-.
         \  _  /--'         `
   jgs ___)( )(___"""
bad = r"""
        ()()         ____
        (..)        /|o  |
        /\/\       /o|  o|
       c\db/o...  /o_|_o_|"""
torch_lit = True
if torch_lit:
    outcome = ("Flicker: Go on and pass through!")
    print(good)
else:
    outcome = ("Doom: Die Die Die Die Die")
    print(bad)
print(outcome)
