import random

answers = ["Yep", "Nope", "Maybe"]

def charivna_kulka(question):
  if type(question) != str:
    raise Exception('Enter another type of value')
  
  if len(question) == 0:
    raise Exception('Question shouldn\'t be empty value')
  
  return f'{question}: {random.choice(answers)}'

def configure_magic_ball(new_answers: list):
  for new_answer in new_answers:
    position = random.randint(0, len(answers))
    answers.insert(position, new_answer)

configure_magic_ball(["Of course", "To be or not to be", "I have no idea"])
print(charivna_kulka("I win sub-zero in MK1?"))