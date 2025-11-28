marks=50
#91 -100 :A
#71-90: B
#51-70:c
#36-50:d
#0-35:f
#invalid


if marks>90 and marks<=100 :
    print("a grade")
elif marks>70 and  marks<=90 :
    print("b grade")
elif marks>50 and marks<=70 :
    print(" c grade")
elif marks>36 and marks<=50 :
    print ("d garde")
elif marks>0 and marks<=35 :
    print ( "fail")
else :
    print("invalid marks")