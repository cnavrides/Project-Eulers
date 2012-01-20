#returns if the number supplied is a palindrome
def isPalindrome(number)
  offset = 0
  numString = number.to_s().split('')
  while offset < (number.to_s().length/2) do
    if numString[offset] != numString[number.to_s().length - offset - 1]
      return false
    end
    offset += 1
  end
  return true
end

highest = 0
#Go down from 999 to 100
999.downto(100) {|i| 
  999.downto(100) {|j| 
    if isPalindrome(i * j) and (i * j) > highest
      highest = i * j
    end
  }
}
puts highest