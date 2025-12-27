# Chapter 3: Recursion

This chapter introduces **recursion**, an elegant problem-solving
technique where a function calls itself to break a problem into smaller,
more manageable subproblems.

## The Two Parts of Recursion

Because a recursive function calls itself, it can easily fall into an
**infinite loop** if not written correctly. To prevent this, every
recursive function must have two distinct parts:

- **The Base Case**:  
  The simplest version of the problem where the function **stops calling
  itself**, preventing infinite recursion.

- **The Recursive Case**:  
  The part of the function where it **calls itself**, reducing the
  problem size and moving closer to the base case.

## The Call Stack

To understand recursion, it is important to understand how the computer
manages function calls using the **call stack**.

A stack is a simple data structure with two main operations:
1. **Push** – Add a new item to the top
2. **Pop** – Remove the topmost item

When a function is called, the computer allocates memory for that call
and **pushes it onto the call stack**.  
If that function calls another function (or itself), the current
function is **paused in a partially completed state** while the new
call is placed on top of the stack.

Once the top function finishes execution, it is **popped off the stack**,
and execution resumes from where the previous function left off.

## Memory and Performance

Recursion often makes solutions **clearer and easier to reason about**,
especially for problems that can be naturally divided into smaller
subproblems. However, recursion does not usually provide a performance
advantage over loops.

Each recursive call consumes additional stack memory. If recursion goes
too deep without reaching a base case, it can result in a
**stack overflow error**.

## When Recursion Is Useful
Recursion is especially useful when:
- The problem can be divided into similar subproblems
- The solution naturally follows a recursive structure
- Clarity is more important than minimal memory usage

## Example

```python
def countdown(n):
    if n <= 0:      # Base case
        return
    print(n)
    countdown(n-1)  # Recursive case

