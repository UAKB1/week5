input_prompt = float(input("the number that u want to find the square root of: "))
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.00001

while abs(guess**2 - input_prompt) >= epsilon and guess**2 <= input_prompt:
    guess += increment
    num_guesses += 1
    if num_guesses % 10000 == 0:
        print("Current guess =", guess)

if abs(guess**2 - input_prompt) >= epsilon:
    print("couldn't find the square root.")
else:
    print("Guess sayısı:", num_guesses)
    print("Yaklaşık karekök:", guess)