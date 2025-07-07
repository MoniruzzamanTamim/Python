name = 'Hello my name is tamim , Iam a small man and TAMIM'
print(len(name))
#string with use index for print specific charecter 
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print("..........................") #Last Theke start korar jonno -1 use hbe akhane 0 kaj korbe na
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print("..........................")
print(name[0:0])
print(name[0:1])
print(name[0:2])
print(name[0:3])
print(name[0:4])
print(name[0:5])
print("..........................")
print(name[-1:])
print(name[-2:])
print(name[-3:])
print(name[-4:])
print(name[-5:])


comment = 'hello he is a smart boy'
sec_comment = 'HELLO IS T KERKJDFHDSLG/KFDG J GRTRYRTYRHTR'
text = "He is TAMIM"
text2 = "         He   "
Is_alpha ="abc"
Is_rep = "tamim"


print("Convert Upercase: " + comment.upper())

print("Convert LowerCase: " + sec_comment.lower())
print("Convert Capitalized: " + comment.capitalize())
print("Convert Title: " + comment.title())
print("Convert FinD: " , text.find("A"))
print("Convert Strip: " + text2.strip())
print("Convert String as a List: " , "a,b,c".split(",") )
print("Check ITS Digis: " , text.isdigit())
print("Check letter: " , Is_alpha.isalpha())
print( "Replace Text: " + Is_rep.replace("tamim", "TARIF"))
print("Check String Or Not: ", isinstance(Is_rep,str))


