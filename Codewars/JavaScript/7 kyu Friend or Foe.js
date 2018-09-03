function friend(friends){
    return friends.filter(function(f)
    {
      if (f.length == 4) return f;
    }
    )
  }