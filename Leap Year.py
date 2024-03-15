def is_leap_year(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap Year")
      else:
        print("Not Leap Year")
    else:
      print("Not Leap Year")
  else:
    print("Not Leap Year")
# To test the corrected code snippet, you can call the function
is_leap_year(2051)