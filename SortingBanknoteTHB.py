import math

print('-'*70)
print("This is a program for identifying the number of Thai banknote used for the amount of money you provide")

money = int(input("Enter the amount of money:"))
note1k = money//1000
amountLeft = money%1000

note500 = amountLeft//500
amountLeft%=500

note100 = amountLeft//100
amountLeft%=100

note50 = amountLeft//50
amountLeft%=50

note20 = amountLeft//20
amountLeft%=20

coin10 = amountLeft//10
amountLeft%=10

coin5 = amountLeft//5
amountLeft%=5

coin1 = amountLeft

print("1kNote: ", note1k, "= ",note1k*1000)
print("500Note: ", note500, "= ", note500*500)
print("100Note: ", note100, "= ", note100*100)
print("50Note: ", note50, "= ", note50*50)
print("20Note: ", note20, "= ", note20*20)
print("10coin: ", coin10, "= ", coin10*10)
print("5coin: ", coin5, "= ", coin5*5)
print("1coin: ", coin1, "= ", coin1*1)
print("TotalNote: ",(note1k+note500+note100+note50+note20))
print("TotalCoin: ", (coin10+coin5+coin1))
print("TotalAmountofMoney: ", money)

print('-'*70)

print("The following is the number of each type of note and coin you need for the amount of money provided")
aNote1k = math.ceil(money/ 1000)
aNote500 = math.ceil(money/ 500)
aNote100 = math.ceil(money/ 100)
aNote50 = math.ceil(money/ 50)
aNote20 = math.ceil(money/ 20)
aCoin10 = math.ceil(money/ 10)
aCoin5 = math.ceil(money/ 5)
aCoin1 = math.ceil(money)

print("You need to use ", aNote1k, "1kNote, the change you will get: ", abs(1000-(money%1000)))
print("You need to use ", aNote500, "500Note, the change you will get: ", abs(500-(money%500)))
print("You need to use ", aNote100, "100Note, the change you will get: ", abs(100-(money%100)))
print("You need to use ", aNote50, "50Note, the change you will get: ", abs(50-(money%50)))
print("You need to use ", aNote20, "20Note, the change you will get: ", abs(20-(money%20)))
print("You need to use ", aCoin10, "10Coin, the change you will get: ", abs(10-(money%10)))
print("You need to use ", aCoin5, "5Coin, the change you will get: ", abs(5-(money%5)))
print("You need to use ", aCoin1, "1Coin, the change you will get: 0")
