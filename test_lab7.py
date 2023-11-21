from lab7 import charivna_kulka, answers

def test_correct_answer():
  result = charivna_kulka("Today i will play Dota 2")
  expected_answers = [*answers]
  assert result.split(": ")[1] in expected_answers

def test_empty_str():
  result_empty = charivna_kulka("1231")
  assert isinstance(result_empty, str)

def test_return_str():
  result = charivna_kulka("Will the piano fall on me today?")
  assert isinstance(result, str)

def test_wrong_type():
  try:
    charivna_kulka("1")
  except Exception as e:
    raise TypeError(e)