"""
860. Lemonade Change

Problem Statement:
------------------
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note: You start with no change in hand.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

Examples:
---------
Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
- Customers 1-3 pay with $5. Now you have three $5 bills.
- Customer 4 pays with $10, you give back $5 as change, now: two $5, one $10.
- Customer 5 pays $20. You give $10+$5 (prefer handing out larger first if possible), left with one $5.
Since all customers got correct change, output is true.

Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
- Customers 1-2: get two $5, have two $5.
- Customers 3-4: both pay $10, need to give one $5 each. After both, have no $5 left, two $10.
- Customer 5 pays $20, but you can't give back $15 (no $5 left).
So output is false.

Constraints:
------------
- 1 <= bills.length <= 10^5
- bills[i] is either 5, 10, or 20
"""


# Approach & Intuition:
# ---------------------
"""
- We always need to try to keep as many $5 bills as possible because that's the most needed change.
- For $5: Just add to the count of $5 bills.
- For $10: Need to give a $5 as change. Only possible if we have at least one $5.
- For $20: Need to give $15 as change. Prioritize giving one $10 and one $5 if possible, otherwise give three $5s.
  - (Giving $10+$5 is preferred over three $5s, because $5 is the "small change" for the next people.)

Dry Run Example:
----------------
bills = [5, 5, 5, 10, 20]
After each bill:
  5: five=1, ten=0
  5: five=2, ten=0
  5: five=3, ten=0
 10: Give back 5. five=2, ten=1
 20: Prefer ten+five (have both): ten=0, five=1

All successful => True.


Implementation:
----------------
Time Complexity: O(n) where n is number of bills
Space Complexity: O(1) aux (tracking only two counters)

"""

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0   # Number of $5 bills in hand
        ten = 0    # Number of $10 bills in hand
        
        for bill in bills:
            if bill == 5:
                # Received $5, no change to give
                five += 1
            elif bill == 10:
                # Need to give back $5 change
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                # Need to give $15 change
                # Prefer $10+$5 if possible
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
