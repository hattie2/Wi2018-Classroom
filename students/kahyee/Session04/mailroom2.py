
donationList = {
"Bob": [1.00, 2.00],
"Jon": [1.50, 100.00],
"Sally": [1000.00], 
"Barry": [50.00],
"Ellen": [1.25]
}

def create_report():
	print("Donor Name          | Total Given | Num Gifts | Average Gift")
	print("------------------------------------------------------------")
	for donor, amounts in donationList.items():
		giftCount = str(len(donor) - 1)
		giftTotal = "%.2f" % sum(amounts)
		giftAvg = "%.2f" % (sum(amounts) / len(donor))
		print(donor \
			+ " " * (20 - len(donor)) \
			+ " $" + " " * (12 - len(giftTotal)) + giftTotal \
			+ " " * 10 + str(giftCount) \
			+ " $" + " " * (12 - len(giftAvg)) + giftAvg)


def thank_you():
    donorName = input("Donor's Full Name: ")
    exist = False
    while donorName.lower() == "list":
        for donor in donationList.keys():
            print(donor)
        donorName = input("Donor's Full Name: ")
    donationAmt = float(input("How much did they donate?"))
    for donor, amounts in donationList.items():
        if donor == donorName:
            amounts.append(donationAmt)
            exists = True
            break
    if not exist:
        donationList[donorName] = [donationAmt]
    email(donorName)

  
def email(donorName):
	print("\nDear " + donorName + "," + \
  	    "\n\n Thank you for your generous donation."+ \
  	    "Your kindness knows no bounds. Yada yada yada." + \
  	    "Please send more money soon \n\n Best, \n Kahyee \n")

def default_prompt():
    return int(input("Select Action \n 1. Send a Thank You \n 2. Create a Report \n 3. Send Letters to Everyone \n 4. Quit \n"))    
      
def all_email():
  for donor in donationList.keys():
    email(donor)

userPrompt = default_prompt()


switch_prompt_dict = {
  1: thank_you,
  2: create_report,
  3: all_email
}



while userPrompt != 4:
  if userPrompt in [1, 2, 3]:
    switch_prompt_dict[userPrompt]()
    
  userPrompt = default_prompt()