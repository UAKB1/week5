low = 0.00
high = 150.00
epsilon = 0.01
high = float(high)
low = float(low)
coin = input("hangi sayfada para var?")
coin = float(coin)
guess = (high+low)/2
while abs(guess - coin) > epsilon:
    if guess > coin:
        high = guess
        guess = (high+low)/2
    else:
        low = guess
        guess = (high+low)/2
print(guess)    
