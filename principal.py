import sys
if len(sys.argv)==4:
  script_name=sys.arvg[0]
principal = sys.argv[1]
rate = sys.argv[2]
time =sys.argv[3]
else:
  simple_interest =(principal * rate * time)/100
  print("Principal Amount:",principal)
  print("Rate of Interest:",rate)
  print("Time period:",time)
  print("Simple Interest:",simple_inerest)
