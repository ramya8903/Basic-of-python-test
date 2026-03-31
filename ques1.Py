# Automated Loan Appoval system

name = input("Enter your name:")
credit_score = input("Enter Credit Score:")
income = float(input("Enter Monthly Income:"))
emi = float(input("Enter Monthly emi:"))
employment = input("Enter Employment(Salaried/Self-Employed):")

interest_rate = 0

#1.Credit Score Check
if credit_score < 600:
   status = "Rejected"

elif 600 <= credit_score <= 749:
    status = "Manual Review"
else:
    credit_score >= 750

#2. Income Check
if income < 25000:
   status = "Rejected"
elif emi > 0.5 * income:
   status = "Rejected"

#3. Employment Check
elif employment.lower() not in["Salaried","Self-employed"]:
     status = "Rejected"
else:
     status = "Approved"

# interest Rate Calculation
if credit_score >= 800:
   interest_rate = 7
elif 750 <= credit_score <= 799
   interest_rate = 8
print("\nLoan Status:",status)
if status == "Approved":
   print("Interest Rate:",interest_rate,"%")

   output:
   Enter Name: Ramya
   Enter Credit Score: 780
   Enter Monthly Income: 40000
   Enter Monthly emi: 15000
   Enter Employment: Salaried

   Loan status: Approved
   Interest rate: 8%
   
