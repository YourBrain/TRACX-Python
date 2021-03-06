# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:48:08 2016

@author: pss02ca
"""

import tracx

tracx1 = tracx.Tracx() 

#pr int(tracx1.fahlmanOffset)
#print(tracx1.bias)
#print(tracx1.sentenceRepetitions)

#data = open('input.txt', 'r').read() # should be simple plain text file
#tracx1.set_training_data(data)

# Simulation 1 from French, Addyman and Mareschal, 2011
#Saffran et al. 1996
tracx1.set_training_data("ghidefghijklghidefabcdefabcdefabcghidefghiabcghiabcjklghiabcjklabcghijklghidefghidefjkldefabcghidefabcjklghidefjklghiabcdefjklghidefabcdefabcdefabcghiabcjklabcghiabcjklabcjklabcjkldefghidefabcghijklabcjklghiabcghidefjkldefabcdefghiabcghidefabcghiabcjkldefabcdefabcdefabcjkldefabcjkldefabcjklabcghidefjklghiabcghidefabcdefghiabcjkldefjklabcjkldefjklghijklabcdefghiabcjklghijklabcdefghidefghiabcjklghiabcghiabcdefghidefjklabcdefabcjklabcjklghidefjkldefghidefjkldefabcdefghiabcjklghiabcghiabcghijkldefghijklghiabcjklabcghijkldefabcghijklghidef")
tracx1.set_tracking_words(["ab", "af"]) 
tracx1.testWords = ["abc","def","ghi","jkl"] 
tracx1.testPartWords= ["cde","fgh","ijk","lab"] 
tracx1.testNonWords = ["aei","dhl","gkc","jbf"]

# Simulation 2
#Aslin et al. 1998
tracx1.set_training_data("abcdefghidefabcghijklabcjklghijklabcjklghiabcjklghiabcdefghiabcghijklabcghijklabcdefghidefabcghiabcdefjklghiabcdefghiabcjklghiabcghidefabcjklghiabcdefghijklabcghiabcghidefabcghiabcghijklabcghiabcjklghiabcdefghidefabcghiabcjklghidefabcghiabcjklghiabcghijklabcghiabcdefabcdefghidefabcghijklabcjklghijklabcjklghiabcjklghiabcdefghiabcghijklabcghijklabcdefghidefabcghiabcdefjklghiabcdefghiabcjklghiabcghighidefabcghidefabcjklghiabcghidefabcghidefabcghiabcdefghiabcjklghiabcghijklabcghiabcdefghiabcghidefabcghidefabcjklghiabcghidefabcghijklabcjklghiabcdefghiabcghiabcghijklabcdefabcjklghiabcdefghijklabcghidefabcjklghidefabcghiabcdefghiabcghijklghijklabcdefghijklabcjklghidefabcghidefabcjklghiabcghidefabcghidefabcghiabcdefghiabcjklghiabcghijklabcghiabcdefghiabcghidefabcghidefabcjklghiabcghidefabcghi")
tracx1.set_tracking_words("ab,gh,be,hk")
tracx1.testWords = "abc,def,ghi,jkl"
tracx1.testPartWords= "cde,fgh,ijk,lab" 
tracx1.testNonWords = "aei,dhl,gkc,jbf"

# Simulation 3
# Peruchet and Desaulty 2008 Forward TPs
tracx1.set_training_data("dygzfycxhzhzgzdydydyfyfygzfydyizdyaxizaxizcxgzdygzbxaxaxdydygzhzgzdyaxizdyeydygzhzgzizcxdybxizfydycxaxgzgzeyhzgzgzdygzgzcxfybxaxeyhzcxcxgzcxdygzcxaxfyfydygzaxgzdygzaxaxdycxbxfydyaxbxaxcxdycxgzhzaxaxgzaxfydyaxgzaxdygzaxizcxdyeyizaxcxcxaxdydyeyizbxaxbxcxizhzdyaxdybxgzgzcxfydyaxhzgzizizaxdyhzgzaxhzdydydygzdyaxdygzaxfyfygzbxbxgzaxdyaxhzbxfyeyeygzbxbxizhzgzaxfyaxdyaxhzcxfygzaxdyhzaxaxbxcxbxhzdygzbxaxizdybxdyizaxdyeyaxeyaxbxfydyaxaxfycxbxcxaxaxbxgzdygzdydyaxdygzdyeygzdyaxdydybxhzizbxdygzeyizaxgzcxgzeyaxaxizaxaxdydyhzdygzgzgzdyfyfydyeygzgzgzgzdyfydybxizaxgzizdydyizaxeydyhzcxfyaxcxdycxeyaxaxdygzeyeydyhzeyeyaxbxhzdygzdydyaxgzhzdydydyaxfydyeydygzaxgzgzaxgzdydygzgzgzizaxaxeyaxdydygzizgzbxgzaxaxaxizdyizdygzbxdycxgzgzaxbxizizaxdyaxdyaxdyizizaxhzfybxdyeybxgzizgzdyfyizeygzdybxgzaxgzdyhzeyaxbxaxdybxgzgzeycxizdygzbxeydygzaxcxgzdygzgzdydygzgzbxdyizdydygzdygzcxaxhzgzgzhzgzaxaxfyeyizaxaxgzdydycxfyhzfyaxaxcxhzeygzhzaxgzaxizgzaxfyfygzdydyaxgzgzcxbxaxcxhzeycxbxgzdydyfyaxaxbxhzdyaxaxdyeydyhzizaxbxgzbxdydyaxhzdyaxcxizaxeycxgzdybxdyaxcxgzizbxhzgzaxizfydygzfyeydygzizaxfydydyaxdydycxbxdygzbxfyaxbxfygzgzcxaxgzgzdybxbxizbxaxgzgzcxcxizaxaxeycxfyhzizaxdyaxaxaxdydyaxaxaxfyaxdydyaxaxdycxaxaxbxcxgzcxaxdyfyfyhzcxcxdygzgzgzgzgzhzgzgzeyeyaxgzdyaxizgzgzgzbxgzaxaxdycxbxeyaxbxaxhzaxhzdyeygzgzgzeyaxaxhzgzaxdyaxaxizaxaxhzgzgzeygzgzdygzaxbxgzaxdyfydyhzbxbxeybxdyaxaxhzaxdyaxaxgzbxgzcxdyaxhzgzaxgzdyaxcxdydydyizgzdydyfyaxhzdyhzdyhzdydygzhzhzfyfydyfyaxdygzdydybxgzeyeycxaxizgzgzaxaxgzaxaxgzgzcxizdydyaxgzeyizizdyhzizcxgzfyeydygzaxaxeydyaxhzgzgzaxgzhzdydycxaxaxaxhzgzgzdycxdyeyizeydyaxaxhzaxfyaxhzbxbxfydydygzgzgzdycxaxdyizgzdygzdyeyizcxeyfydyhzdycxbxaxizaxeyaxeydybxgzgzdycxgzdydyaxaxgzdydygzfyaxgzaxaxcxgzaxdycxdydydydygzhzaxgzaxizaxeyeyaxfygzizaxbxaxgzdyaxaxdyeyaxgzdybxfyfygzfyaxhzaxgzbxaxgzfycxgzgzizizdydygzdyhzgzgzgzaxgzaxdyaxaxeyfyeyfyfyaxdyaxfyeybxgzbxaxaxgzgzaxdygzaxeyaxgzhzaxdydyizdyizdycxgzizfyeygzbxgzfyizcxdygzcxaxizaxcxfyfyfyeyeybxgzizfydyaxbxaxdygzfyhzhzhzgzaxdyaxaxgzdyaxdygzgzeyizcxhzizeyfyizhzfygzdyeydygzbxhzdyhzaxgzgzhzcxizeyaxfygzeyhzdygzaxgzcxizfygzdygzaxgzgzaxaxeygzgzgzhzgzdyeycxdygzdyaxeydydygzdyey")
tracx1.set_tracking_words("bx,ey,xa,yd")
tracx1.testWords = "bx,cx,ey,fy,hz,iz"
tracx1.testPartWords= "xa,xd,yd,yg,za,zg"
tracx1.testPartWords= "xx,yy,zz"

# Simulation 4
# Peruchet and Desaulty 2008 Backward TPs
tracx1.set_training_data("ydzgyfxczhzhzgydydydyfyfzgyfydziydxazixazixczgydzgxbxaxaydydzgzhzgydxaziydyeydzgzhzgzixcydxbziyfydxcxazgzgyezhzgzgydzgzgxcyfxbxayezhxcxczgxcydzgxcxayfyfydzgxazgydzgxaxaydxcxbyfydxaxbxaxcydxczgzhxaxazgxayfydxazgxaydzgxazixcydyezixaxcxcxaydydyezixbxaxbxczizhydxaydxbzgzgxcyfydxazhzgzizixaydzhzgxazhydydydzgydxaydzgxayfyfzgxbxbzgxaydxazhxbyfyeyezgxbxbzizhzgxayfxaydxazhxcyfzgxaydzhxaxaxbxcxbzhydzgxbxaziydxbydzixaydyexayexaxbyfydxaxayfxcxbxcxaxaxbzgydzgydydxaydzgydyezgydxaydydxbzhzixbydzgyezixazgxczgyexaxazixaxaydydzhydzgzgzgydyfyfydyezgzgzgzgydyfydxbzixazgziydydzixayeydzhxcyfxaxcydxcyexaxaydzgyeyeydzhyeyexaxbzhydzgydydxazgzhydydydxayfydyeydzgxazgzgxazgydydzgzgzgzixaxayexaydydzgzizgxbzgxaxaxaziydziydzgxbydxczgzgxaxbzizixaydxaydxaydzizixazhyfxbydyexbzgzizgydyfziyezgydxbzgxazgydzhyexaxbxaydxbzgzgyexcziydzgxbyeydzgxaxczgydzgzgydydzgzgxbydziydydzgydzgxcxazhzgzgzhzgxaxayfyezixaxazgydydxcyfzhyfxaxaxczhyezgzhxazgxazizgxayfyfzgydydxazgzgxcxbxaxczhyexcxbzgydydyfxaxaxbzhydxaxaydyeydzhzixaxbzgxbydydxazhydxaxczixayexczgydxbydxaxczgzixbzhzgxaziyfydzgyfyeydzgzixayfydydxaydydxcxbydzgxbyfxaxbyfzgzgxcxazgzgydxbxbzixbxazgzgxcxczixaxayexcyfzhzixaydxaxaxaydydxaxaxayfxaydydxaxaydxcxaxaxbxczgxcxaydyfyfzhxcxcydzgzgzgzgzgzhzgzgyeyexazgydxazizgzgzgxbzgxaxaydxcxbyexaxbxazhxazhydyezgzgzgyexaxazhzgxaydxaxazixaxazhzgzgyezgzgydzgxaxbzgxaydyfydzhxbxbyexbydxaxazhxaydxaxazgxbzgxcydxazhzgxazgydxaxcydydydzizgydydyfxazhydzhydzhydydzgzhzhyfyfydyfxaydzgydydxbzgyeyexcxazizgzgxaxazgxaxazgzgxcziydydxazgyeziziydzhzixczgyfyeydzgxaxayeydxazhzgzgxazgzhydydxcxaxaxazhzgzgydxcydyeziyeydxaxazhxayfxazhxbxbyfydydzgzgzgydxcxaydzizgydzgydyezixcyeyfydzhydxcxbxazixayexayeydxbzgzgydxczgydydxaxazgydydzgyfxazgxaxaxczgxaydxcydydydydzgzhxazgxazixayeyexayfzgzixaxbxazgydxaxaydyexazgydxbyfyfzgyfxazhxazgxbxazgyfxczgzgziziydydzgydzhzgzgzgxazgxaydxaxayeyfyeyfyfxaydxayfyexbzgxbxaxazgzgxaydzgxayexazgzhxaydydziydziydxczgziyfyezgxbzgyfzixcydzgxcxazixaxcyfyfyfyeyexbzgziyfydxaxbxaydzgyfzhzhzhzgxaydxaxazgydxaydzgzgyezixczhziyeyfzizhyfzgydyeydzgxbzhydzhxazgzgzhxcziyexayfzgyezhydzgxazgxcziyfzgydzgxazgzgxaxayezgzgzgzhzgydyexcydzgydxayeydydzgydye")
tracx1.set_tracking_words("xb,ye,ax,dy")
tracx1.testWords = "bx,cx,ey,fy,hz,iz"
tracx1.testPartWords= "ax,ay,dy,dz,gx,gz"
tracx1.testNonWords= "aa,bb,cc,dd"


# Simulation 11
# French, Addyman and Mareschal 2011 - Equiprobable forward TPs
tracx1.set_training_data("dfabdegidfgiacghdfgiabdeacdeacdfabdfabdfabdfgideabghacgidfacdeghdeabgiacdfabdfabgiacdeghabdfghacgiacdeabdfacdfgiabdegidegiacghacgidfghdfabdeacdegiabgiabdfabdeacdfghdfacdegiabgideghabdfabdfghdfabdfgiabdfgiabgiabghdfgideghdfghdfghdfacdegidfghacdeghabgiabdeghdeabghdegiacdfacdfabgiacghacdeabgiacdegiabghdfgidfghdfacgidegiacdfacdegiabdegiabgideabgidfghdfabghacghacghabdeacghacghacdfghabgiabgiacdeabdegiacdeacgideabgiabdfabghacgiacgideghdeabghabdeghabghabghabghabdeacgideghdeacdeacdeabdfabghdeghacghdfgiabgideabdeabdfgideacgidfghacghdfgiabghabghabgidfacgiabdfghdeacghdeacdfghdeghabghdeghacdeabdfabdfabdegiabgiacdfabdegiacdegiabdfabghacghabgiacdeghdeacghabgiabdeghdfghdeghdfacgiabdfgideabghdeabdeacdeabghabdeabdfgiacgideacghabgidfgiabdfgidfacgiabdegiacdfgiabdfacghdfgideacgiabgiacghdeabghdfabghdeghacgiabgideacgiacg")
tracx1.set_tracking_words("ab,ac,de,df,gh,gi")
tracx1.testWords = "bd,bg,cd,cg,eg,ea,fg,fa,ha,hd,ia,id"
tracx1.testPartWords= "ab,ac,bd,bg"
tracx1.testNonWords= "aa,bb,cc,dd"

# Simulation 12
#kirkham et al. 2002
#tracx1.set_training_data("babefefcdabefabababefcdefefcdefabefabefababefcdefabcdefcdcdcdefefcdcdabefabefcdefcdcdababefcdabcdefcdefababcdabefefcdabefabcdefcdababefcdefcdefabefefcdcdcdcdefefababababefcdcdefefc")
#tracx1.set_tracking_words(["ab", "af"]) 
#tracx1.testWords = ["ab", "ef"] 
#tracx1.testPartWords= ["bc", "fa"] 
#tracx1.testNonWords = ["af", "ca"]

print(tracx1.get_unique_items())  

print(tracx1.inputWidth)

#print(tracx1.decimal_to_binary(101))

tracx1.initialize_weights()
tracx1.create_input_encodings()

##print(tracx1.layer[0])
#
ret = tracx1.run_full_simulation()
#
print(ret) 
#
ret = tracx1.test_strings(tracx1.testWords)
print(ret)
