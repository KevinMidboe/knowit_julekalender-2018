import os
from PIL import Image
from luke_04.steganography import main

path = os.path.dirname(__file__)

def test_answer():
  solution_path = os.path.join(path, 'images/solution-pokemon_jakt.png')
  solution_image = Image.open(solution_path)
  answer_image = Image.open(main())
  
  assert solution_image.tobytes == answer_image.tobytes
