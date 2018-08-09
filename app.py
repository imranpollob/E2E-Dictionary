import json
from difflib import get_close_matches

def meaning( word ):
  data = json.load( open( "data.json" ) )
  data = { k.lower():v for k,v in data.items() }
  word = word.lower()

  if word in data:
    return "\n".join(data[ word ])

  elif len( get_close_matches( word, data.keys(), 1, 0.8 ) ) > 0:
    matched_word = get_close_matches( word, data.keys() )[0]
    answer = input( "Did you mean '{}'? Enter y or n: ".format( matched_word ) )

    if answer == 'y':
      return "\n".join(data[ matched_word ])

    elif answer == 'n':
      return "Word doesn't exist! Try Again"

    else:
      return "I can't understand your input"

  else:
    return "Oops!! word not found"

print( " - - My Dictionary - - " )

while True:
  print( meaning( input("\nEnter a word: ") ) ) 