function foldArray(array, runs)
{
  for (let i = 0; i < runs; i++)
  {
    array = fold(array)
  }
  return array
}

function fold(array)
{
    newArr = []

    for (let j = 0; j < Math.floor(array.length / 2); j++)
    {
      newArr.push(array[j] + array[array.length - 1 - j])
    }
      if (array.length % 2 != 0)
      {
          newArr.push(array[Math.floor(array.length / 2)])
      }
    return newArr
}