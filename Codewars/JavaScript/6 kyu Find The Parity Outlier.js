function findOutlier(integers){
    odds = []
    evens = []
    
    for (var i = 0; i < integers.length; i++)
    {
      if (integers[i] % 2 === 0)
      {
        evens.push(integers[i]);
      }
      else
      {
        odds.push(integers[i]);
      }
      
      if (evens.length > 1 && odds.length === 1)
      {
        return odds[0]
      }
      else if (odds.length > 1 && evens.length === 1) 
      {
        return evens[0]
      }
    }
  }