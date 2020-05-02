# Interview-Cake Tutorial:cake:  
*Solutions to Interview Cake questions.*


## **:hatching_chick: Where to Start**
#### 1. Use a simple example to understand the problem 
* If needed, put down your thoughts on a piece of paper
* **Helps to find how to approach the problem**
#### 2. Start Each problem with Brute-Force Method
* Come up with a Brute-Force solution to understand the problem
* **A slow solution is better than no solution at all**
#### 3. Analyze your solution based on space/time complexity and optimize for the best solution
* Check the time/space of your current solution and **try patterns with beter complexites** to improve the current solution
* **Starting with a target runtime and working backward from there can be a powerful strategy** for all kinds of coding interview questions 


## **:bar_chart: Optimize**
### 0. Question what should be optimized. *(time or space)*
* efficency depends on the situation. Use expected characteristics of the input as a reference to what needs optimization
#### 1. [Tips to Optimize your Python Code](https://www.techbeamers.com/python-code-optimization-tips-tricks/#h6)
#### 2. Use Greedy Approach
* builds up a solution by **choosing the best option for every step**
* Use this approach to **break down the question**
* **NOTE** A Greedy Algorithm doesn't garuntee the best solution, so keep that in mind.
* Include all possible input cases **(Edge Cases)**
### 3. Try a Dynamic Programming Approach


## :dizzy: Try these tips if you get stuck on a problem
#### 1. Use a simpler version of the problem
* See if this gets us closer to a solution to the original problem
* Try the solution of the simpler version **to resolve issues within the original problem.**
* Simplfy, Solve, and Adapt stradegy (Take a deep breath & don't over complicate the problem
### 2. Take a step back and try to break down the problem into sub-problems
### 3. Flag the issue, and move on
* **Skip over it** if you can't find an immediate fix to your algorithm and come back to it later.
* Leave a note for what this algorithm intends to solve
* Prioritize **Core Functionality** before small bits in the code that don't work
### :ant: **Debugging**
*check for common errors*
#### 1. off-by-one errors
#### 2. returning values by if-else conditons
#### 3. check the input of your **Edge Cases**
* Integers: Postive/negative cases, duplicates, 0 divsion, etc.
* graphs: nodes w/ no edges, cycles, loops
* stacks/queues: empty cases
* linked lists: head node, tail node, prev/current/next node pointing to an empty node
### :bookmark_tabs: **Sanity Check**
* Some of these questions will have several possible solutions *(There are no definte answers)*
* Analyze your approach, **Name the Pros and Cons**
* Acknowledge that imperfect solutions exist
  * it's okay to throw exceptions to cases where you can't solve due to input constraints
