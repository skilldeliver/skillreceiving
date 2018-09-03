function reverseWords(str) {
    word = "";
    arr = str.split(" ");
    
    for (var i = 0; i < arr.length; i++)
    {
      word += arr[i].split("").reverse().join("");
      
      if (i != arr.length - 1)
      {
        word += " ";
      }
    }
    
    return word;
  }