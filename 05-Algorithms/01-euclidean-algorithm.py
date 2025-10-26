"""
Euclidean Algorithm for GCD (Greatest Common Divisor)
===================================================

The Euclidean Algorithm is an efficient method for finding the greatest common divisor
(GCD) of two integers. It's based on the principle that GCD(a, b) = GCD(b, a mod b).

Time Complexity: O(log(min(a, b)))
Space Complexity: O(1) iterative, O(log(min(a, b))) recursive

Mathematical Principle:
- GCD of two numbers doesn't change if smaller number is subtracted from larger
- Instead of subtraction, we can use modulo operation for efficiency
- GCD(a, 0) = a (base case)

Applications:
- Simplifying fractions
- Cryptography (RSA algorithm)
- Finding LCM: LCM(a, b) = (a * b) / GCD(a, b)
- Solving linear Diophantine equations

KEY TAKEAWAYS:
1. Euclidean Algorithm is highly efficient: O(log(min(a, b)))
2. Based on principle: GCD(a, b) = GCD(b, a mod b)
3. Extended version finds coefficients for ax + by = GCD(a, b)
4. Applications: fraction simplification, LCM, cryptography
5. Fundamental algorithm in number theory and computer science
6. Much faster than naive approaches for large numbers

Time Complexity Analysis:
- Each step reduces the larger number by at least half
- After at most log₂(min(a, b)) steps, algorithm terminates
- Fibonacci numbers give worst case: consecutive Fibonacci numbers
- Time complexity: O(log(min(a, b)))

Why Modulo is Better than Subtraction:
- Subtraction version: O(min(a, b)) - could be very slow
- Modulo version: O(log(min(a, b))) - much faster
- Example: GCD(1000000, 1) takes 1M steps vs ~20 steps

Space Complexity:
- Iterative version: O(1) - constant space
- Recursive version: O(log(min(a, b))) - call stack depth
"""

def gcd_euclidean_basic(a, b):
    """
    Basic Euclidean Algorithm using subtraction
    
    Args:
        a, b: Two positive integers
    
    Returns:
        GCD of a and b
    
    Time: O(min(a, b)), Space: O(1)
    Note: This is less efficient than modulo version
    """
    # Make sure a >= b for consistency
    if a < b:
        a, b = b, a
    
    # Keep subtracting smaller from larger until one becomes 0
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    return a

def gcd_euclidean_optimized(a, b):
    """
    Optimized Euclidean Algorithm using modulo operation
    
    Args:
        a, b: Two positive integers
    
    Returns:
        GCD of a and b
    
    Time: O(log(min(a, b))), Space: O(1)
    """
    while b != 0:
        a, b = b, a % b
    
    return a

def gcd_euclidean_recursive(a, b):
    """
    Recursive implementation of Euclidean Algorithm
    
    Args:
        a, b: Two positive integers
    
    Returns:
        GCD of a and b
    
    Time: O(log(min(a, b))), Space: O(log(min(a, b)))
    """
    # Base case
    if b == 0:
        return a
    
    # Recursive case: GCD(a, b) = GCD(b, a mod b)
    return gcd_euclidean_recursive(b, a % b)

def extended_euclidean_algorithm(a, b):
    """
    Extended Euclidean Algorithm
    
    Finds GCD(a, b) and coefficients x, y such that ax + by = GCD(a, b)
    
    Args:
        a, b: Two integers
    
    Returns:
        Tuple (gcd, x, y) where gcd = ax + by
    
    Applications: Finding modular inverse, solving Diophantine equations
    """
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
    
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y

def gcd_applications():
    """
    Real-world applications of GCD and Euclidean Algorithm
    """
    
    def simplify_fraction(numerator, denominator):
        """Simplify a fraction using GCD"""
        gcd = gcd_euclidean_optimized(numerator, denominator)
        return numerator // gcd, denominator // gcd
    
    def lcm(a, b):
        """Calculate LCM using GCD: LCM(a,b) = (a*b)/GCD(a,b)"""
        return (a * b) // gcd_euclidean_optimized(a, b)
    
    def modular_inverse(a, m):
        """
        Find modular inverse of a modulo m using Extended Euclidean Algorithm
        Returns x such that (a * x) ≡ 1 (mod m)
        """
        gcd, x, y = extended_euclidean_algorithm(a, m)
        
        if gcd != 1:
            return None  # Modular inverse doesn't exist
        
        return (x % m + m) % m  # Make sure result is positive
    
    def solve_linear_diophantine(a, b, c):
        """
        Solve ax + by = c using Extended Euclidean Algorithm
        Returns one solution (x, y) if exists, None otherwise
        """
        gcd, x, y = extended_euclidean_algorithm(a, b)
        
        if c % gcd != 0:
            return None  # No solution exists
        
        # Scale the solution
        x *= c // gcd
        y *= c // gcd
        
        return x, y
    
    return simplify_fraction, lcm, modular_inverse, solve_linear_diophantine

def demonstrate_applications():
    """
    Demonstrate various applications of Euclidean Algorithm
    """
    print("=== EUCLIDEAN ALGORITHM APPLICATIONS ===\n")
    
    simplify, lcm_func, mod_inverse, solve_diophantine = gcd_applications()
    
    # 1. Fraction simplification
    print("1. Fraction Simplification:")
    numerator, denominator = 48, 18
    simplified_num, simplified_den = simplify(numerator, denominator)
    print(f"   {numerator}/{denominator} = {simplified_num}/{simplified_den}")
    print(f"   GCD({numerator}, {denominator}) = {gcd_euclidean_optimized(numerator, denominator)}")
    print()
    
    # 2. LCM calculation
    print("2. Least Common Multiple (LCM):")
    a, b = 12, 18
    lcm_result = lcm_func(a, b)
    gcd_result = gcd_euclidean_optimized(a, b)
    print(f"   LCM({a}, {b}) = {lcm_result}")
    print(f"   GCD({a}, {b}) = {gcd_result}")
    print(f"   Verification: {a} × {b} = {a*b}, LCM × GCD = {lcm_result * gcd_result}")
    print()
    
    # 3. Modular inverse
    print("3. Modular Inverse (Cryptography):")
    a, m = 7, 26
    inverse = mod_inverse(a, m)
    if inverse:
        print(f"   Modular inverse of {a} mod {m} = {inverse}")
        print(f"   Verification: ({a} × {inverse}) mod {m} = {(a * inverse) % m}")
    else:
        print(f"   Modular inverse of {a} mod {m} doesn't exist")
    print()
    
    # 4. Linear Diophantine equation
    print("4. Linear Diophantine Equation:")
    a, b, c = 35, 15, 5
    solution = solve_diophantine(a, b, c)
    if solution:
        x, y = solution
        print(f"   Solving {a}x + {b}y = {c}")
        print(f"   Solution: x = {x}, y = {y}")
        print(f"   Verification: {a}×{x} + {b}×{y} = {a*x + b*y}")
    else:
        print(f"   No solution exists for {a}x + {b}y = {c}")

def euclidean_algorithm_variants():
    """
    Different variants and related algorithms
    """
    
    def binary_gcd(a, b):
        """
        Binary GCD (Stein's Algorithm) - uses bit operations
        More efficient on binary computers for very large numbers
        """
        if a == 0:
            return b
        if b == 0:
            return a
        
        # Count common factors of 2
        shift = 0
        while ((a | b) & 1) == 0:
            a >>= 1
            b >>= 1
            shift += 1
        
        # Remove factors of 2 from a
        while (a & 1) == 0:
            a >>= 1
        
        while b != 0:
            # Remove factors of 2 from b
            while (b & 1) == 0:
                b >>= 1
            
            # Ensure a <= b
            if a > b:
                a, b = b, a
            
            b -= a
        
        return a << shift
    
    def gcd_multiple_numbers(numbers):
        """
        Find GCD of multiple numbers
        GCD(a, b, c) = GCD(GCD(a, b), c)
        """
        if not numbers:
            return 0
        
        result = numbers[0]
        for i in range(1, len(numbers)):
            result = gcd_euclidean_optimized(result, numbers[i])
            if result == 1:  # Early termination optimization
                break
        
        return result
    
    def lcm_multiple_numbers(numbers):
        """
        Find LCM of multiple numbers
        LCM(a, b, c) = LCM(LCM(a, b), c)
        """
        if not numbers:
            return 0
        
        result = numbers[0]
        for i in range(1, len(numbers)):
            result = (result * numbers[i]) // gcd_euclidean_optimized(result, numbers[i])
        
        return result
    
    return binary_gcd, gcd_multiple_numbers, lcm_multiple_numbers
