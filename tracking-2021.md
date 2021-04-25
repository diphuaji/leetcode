# array
## 561 Array Partition I
## 283 Move Zeroes
### manipulate index

## 268 Missing number
### sum of arithmetic series
A less optimal solution is to sum manually

## 217 Contains Duplicate
### sort first 
### hashtable
### set

## 169 Majority Element
### hashtable
### sort first
### use a counter (best)

## 121 Best Time to Buy and Sell Stock
### updating the min and max profit along the way
### only updating the max profit and use accumulated profit to track if we encounter a lower price

## 122 Best Time to Buy and Sell Stock II
### add profit whenever there is a price drop
### beware of last day whose price is lower than the previous one

## 118 Pascal's Triangle
### bottom-up method - `118.py`
### top-down method - `118_1.py`

## 53 Maximum Subarray
### best solution - `53.py`
### kinda like the first one - `53_2.py`
### divide and conquer todo

## 26 Remove Duplicates from Sorted Array
### better solution - `26_1.py`
Starting from pos 1, let `swap_pos=1`, Check if current number is different from the previous one, if it does then
- swap the number at current pos with the one at `swap_pos`,
- set the previous value to current one
- advance `swap_pos` by 1;
if it doesn't then we don't do the swapping.

12`2`2`3`334 -> 12`3`2`2`334  
123`2`233`4`-> 123`4`233`2`


# string
## 409 Longest Palindrome
### `409.py`

## 20 Valid Parentheses
### `20.py` 