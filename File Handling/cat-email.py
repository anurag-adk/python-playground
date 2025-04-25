import sys

too_good_to_be_true = ["too good to be true", "free money", "pure profit", "risk free", "no obligation", "free gift"]
urgent_or_intriguing = ["limited time", "expires", "act now", "click below", "instant access", "don't delete"]
exaggerations_or_superlatives = ["fantastic deal", "special promotion", "lowest price", "best rates", "best price"]
finance_or_purchase = ["mortgage", "refinance", "interest", "lower interest rates", "insurance", "unsecured credit", "credit"]
personal_or_special = ["dear", "sir", "madam", "love", "my", "selected"]
health_related = ["weight", "muscle", "organic", "all natural"]
job_opportunity_related = ["join", "own boss", "financial freedom", "extra income", "extra cash", "no hidden costs", "no hidden charges"]
unprofessional_or_offensive = ["crazy", "psycho", "OCD", "insane", "my bad", "no biggie", "chill", "sick", "sucks", "sucked"]
curse_or_swear = ["ass", "asshole", "bastard", "bitch", "bullshit", "cunt", "dick", "dickhead", "fuck", "fucker", "nigga", "pussy", "shit", "slut", "whore"]

if len(sys.argv)==2:fname=sys.argv[1]
else: fname="cat-email.txt"

with open(fname) as email: content=email.read().lower()

flag=0
print(f"This email seems to fall within the following categories:")

for word_list, category in [
    (too_good_to_be_true, "Too good to be true"),
    (urgent_or_intriguing, "Urgent or Intriguing"),
    (exaggerations_or_superlatives, "Over Exaggeration"),
    (finance_or_purchase, "Finance and Purchase"),
    (personal_or_special, "Personal or Special"),
    (health_related, "Health Related"),
    (job_opportunity_related, "Job Opportunity Related"),
    (unprofessional_or_offensive, "Unprofessional and Offensive"),
    (curse_or_swear, "Curse and Swear Words")
]:
    for word in word_list:
        if word in content:
            print(f"-> {category}")
            flag=1
            break

if flag==0:
    sys.exit("Can't categorize the email")
