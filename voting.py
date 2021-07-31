age=int(input("enter the age"))
if age>=18:
    print("you are eligible to fill online form")
    Apply=input("enter the document")
    if Apply=="Aadhar card" or Apply=="pan card":
        print("Apply document successfull")
        print("Thank you for submitting form")
        Blo=input("enter the voter")
        if Blo=="office":
            print("blo appointed")
            field=input("enter the field")
            if field=="worker" or "farmer" or "gov survant" or "other":
                print("field verified")
                Document=input("enter the document")
                if Document=="again check":
                    print("your form accept")
                    Card=input("enter the card")
                    if Card=="voting card":
                        print("ok your process sucessfull we are sending voting card by post")
                    else:
                        print("your card not made")
                else:
                    print("your form reject")
            else:
                print("field not verified")
        else:
            print("no blo appointed")
    else:
        print("your document unsuccessfull")
else:
    print("you are minor you can't fill form")                                        



