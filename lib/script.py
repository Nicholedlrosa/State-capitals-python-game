# from capitals import states
states = [
{
    "name": "New York",
    "capital": "Albany"
}, {
    "name": "North Carolina",
    "capital": "Raleigh"
}, {
    "name": "North Dakota",
    "capital": "Bismarck"
}]

print("How well do you know the state capitals? Want to test your knowledge?")

for state in states:
  state["incorrect"] = 0

def capitals_trivia():
  score = 0
  incorrect = 0
  states.sort(key=lambda x: x["incorrect"])

  for state in states:
    state_name = state["name"]
    print("----------\n")
    print(f"Correct: {score} Incorrect: {incorrect}")
    answer = input(f"What is the capital of {state_name}? ")
    if answer.lower() == state["capital"].lower():
      score+=1
    else:
      incorrect+=1
      state["incorrect"] +=1
  print(f"Your final score is {score}")
  keep_playing = input(f"Would you like to play again? (y/n): ")
  if keep_playing.lower() == "y": capitals_trivia()
  else: print("I hope you had fun! Thanks for playing.")

capitals_trivia() 