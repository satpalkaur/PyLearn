# import packages (DO NOT MODIFY)
import sys

# Your code - START >
def compress_string(s: str) -> str:
    # write here...
    count=1
    outputstring=""
    for i in range(1,len(s)):
      current_char = s[i]
      previous_char = s[i-1]
      if current_char == previous_char:
        count=count+1
      else:
        if count>1:
          outputstring=outputstring+previous_char+str(count)
        else:
          outputstring=outputstring+previous_char
        count=1

    if count>1:
      outputstring=outputstring+current_char+str(count)
    else:
      outputstring=outputstring+current_char
    return(outputstring)
# Your code - END >

# main function (DO NOT MODIFY) changed....mybranch change
if __name__ == "__main__":
    s = str(sys.argv[1]).strip()  # Read input from command line
    print(compress_string(s))  # Print the result
