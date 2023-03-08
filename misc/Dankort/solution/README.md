# Dankort

## Description

the flag for this challenge is a **valid visa card** number that can be devided by **57568390651**. (ps: the number is unique)
format: AlphaCTF{credit_card_number}

## Write up

The challenge can be split into 3 parts:

1. **Valid visa card:**
    
    let’s google “how to determine a valid credit card number”, we’ll find an algorith is used to determine our valid credit card number, it’s called **Luhn's algorithm,** we dont actually need to write the algorithm, we can just find it online
    
2. **The number is devided by 57568390651:**
    
    this is one is easy, we just brute force all values till we find our credit card, easy isn’t it ? well it isn’t because credit card numbers are very long (from 10 to 16) which makes it impossible to find the correct flag, but if we can have just a small part of the card number, it would make our life easier
    
3. **Dankort:**
    
    back to google, this time we searching for “**Dankort**” we find 
    
    > The Dankort is the national debit card of Denmark. Today it is usually combined with a Visa card and functions as a Visa debit card abroad and in stores that don't accept DanKort.

    notice the visa card part, now let’s try to look for more info about credit cards, after searching we find each bank have it's own prefix, now lets get our bank's prefix, again google “dankort card number prefix” and we get this table:
    
    | Card | Card type | Prefix |
    | --- | --- | --- |
    | Dankort | DK | 5019 |
    | VISA/Dankort | V-DK | 4571 |
    | VISA (SE) | VISA(SE) | 402005 |
    | VISA | VISA | 4711 |
    
    notice the prefix number is different, but going back to our description "**valid visa card**" so our prefix is 4571
    
now lets group everything in one code:

```python
def checkLuhn(cardNo):
	nDigits = len(cardNo)
	nSum = 0
	isSecond = False
	for i in range(nDigits - 1, -1, -1):
		d = ord(cardNo[i]) - ord('0')
		if (isSecond == True):
			d = d * 2
		nSum += d // 10
		nSum += d % 10
		isSecond = not isSecond
	if (nSum % 10 == 0):
		return True
	else:
		return False

#now lets determine our range
#max possible value is 457199999999999, devide it by the given number = 79418.58
#min possible value is 457100000000000, devide it by the given number = 79401.21
#we can start from 0 till 100000 aswell, but it is not a cool
for i in range(79402, 79419):
		#the correct card must be devided by 57568390651
    a = i*57568390651

		#the dankort visa card contains 16 numbers, starts with 457 and 
		#must be valid by luhn'salgo
    if(len(str(a))==16 and str(a).startswith("4571") and checkLuhn(str(a))):
        print("This is a valid card: ",a)
```

run the script and voila: 

> This is a valid card: 4571793743549165
> 

and finally follow the format: **AlphaCTF{4571793743549165}**