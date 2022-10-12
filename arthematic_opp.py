def arithmetic_arranger(prob):
    terms={}
    ops=[]

    for v in prob:
        plus=v.find("+")
        minus=v.find("-")
        if plus!=-1 :           
            ops.append(v[plus])
        if minus!=-1 :           
            ops.append(v[minus])
        if plus>=0:
            a_b=v.split(" + ")
        else:
            a_b=v.split(" - ")
        terms.update({int(a_b[0]):int(a_b[1])})
    print(terms)
    print(ops)
            
       
        
        

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
'''
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474


'''