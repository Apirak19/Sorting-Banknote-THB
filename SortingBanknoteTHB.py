print("This is a program to identify the number of Thai banknote usd for the amount of money you provide")

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
