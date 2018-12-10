from luke_09.hashmebaby import main as hashmebaby

answer = 'Dev: Hva er [10, 10, 10].map(parseInt) lik? JS: NaNsense.'

def test_answer():
  assert hashmebaby() == answer
