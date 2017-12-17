from luke_03.steganography import main

def test_answer():
   answer = 'Steganography is awesome and you Knowit!'
   output = main()
   print(output)
   print(answer in output)
   if answer in output:
      assert True
   else:
      assert False
