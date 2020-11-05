function alphabetPosition(text) {
  arr = []
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  
  for (let i = 0; i < text.length; i++)
  {
      if (alphabet.indexOf(text[i].toLowerCase()) != -1)
      {
        arr.push(alphabet.indexOf(text[i].toLowerCase()) + 1)
      }
  }
  return arr.join(" ");
}