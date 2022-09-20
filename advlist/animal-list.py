#!/usr/bin/env python3
"""Brandon Wortham
   Created an animals list and displayed it without strings around words"""

def main():
    animals = ["dog", "cat", "cow", "hog", "fox"]

    print(animals)
    print(*animals, sep =', ')

if __name__ == "__main__":
    main()    
