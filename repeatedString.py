def repeatedString(s, n):
    # Write your code her
    a_s = s.count('a')
    copy_time= n//len(s)
    reminder =n%len(s)
  #  print(copy_time,',', reminder)
  #  print(s[:reminder])
    a_s = copy_time * a_s + s[:reminder].count('a')
    
    return a_s  

if __name__ == '__main__':

    n = 10
    s = 'abcac'
    result = repeatedString(s, n)
    print(result)
    
    n = 10
    s = 'aba'
    result = repeatedString(s, n)
    print(result)
    
    n = 1000000000000
    s = 'a'
    result = repeatedString(s, n)
    print(result)
    
