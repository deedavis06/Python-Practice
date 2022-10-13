import re 
em = 'From: ddd6@unt.edx.edu Thurs Oct 13 14:58:15 2022'
   
    #extract the email address from string
ad = re.findall('\S+@\S+', em)
print(ad)

    #extract the domain from the email address
ad2 = re.findall('@[^ ]*', em)
print(ad2)

    #extract the domain without the @
ad3 = re.findall('^From: .*@([^ ]*)', em)
print(ad3)