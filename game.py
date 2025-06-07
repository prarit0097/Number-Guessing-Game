import random

print("Welcome to the number guessing game")
print("I am thinking a number between 1 to 100 can you guess it")

while True:

    secret_number = random.randint(1,100)
    guesses = 0
    max_score = 100

    while True:

        try:

            guess = int(input("Enter a number fromm 1 to 100 "))
            guesses +=1

            if guess < secret_number:
                print("too low Try a high number")
            elif guess> secret_number:
                print("too high Try a lower number")
            else:

                score = max(0, max_score - (guesses -1) * 10)

                print(f"🎉 YOU WIN! The number was {secret_number}")
                print(f"You guess it in {guesses} tries")
                print(f"Your score is {score}/100 points")

                if score == 100:
                    print("🌈 PERFECT SCORE! You're a guessing genius!")
                elif score >= 80:
                    print("🔥 AWESOME! You've got eagle eyes!")
                elif score >= 60:
                    print("😎 GREAT JOB! That was impressive!")
                else:
                    print("👍 GOOD TRY! You'll do better next time!")

                break

        except ValueError:
            print("⚠️ Oops! Please enter a number between 1-100.")

    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again in ['yes', 'y', 'yeah', 'yep']:
            print("\nGreat! Starting a new game...")
            break
        elif play_again in ['no', 'n', 'nah', 'nope']:
            print("\nThanks for playing! Goodbye! 👋")
            exit()
        else:
            print("⚠️ Please answer 'yes' or 'no'")