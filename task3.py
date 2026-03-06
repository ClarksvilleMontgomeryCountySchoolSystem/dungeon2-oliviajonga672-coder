good = r""" /\
    ( /   @ @    ()
     \  __| |__  /
      -/   "   \-
     /-|       |-\
    / /-\     /-\ \
     / /-`---'-\ \     tre
      /         \
      """
bad = r"""
   _,-='"-.__               /\_/\
   `-.}       `=._,.-==-._.,  @ @._,
      `-.__   _,-.   )       _,.-'
           `"     G..m-"^m`m'        """
guard_awake = False
if not guard_awake:
    outcome = ("Shadow: Good Job player you did great")
    print(good)
else:
    outcome = ("Doom: I hope you die")
    print(bad)
print(outcome)