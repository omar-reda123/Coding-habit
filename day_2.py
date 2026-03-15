"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n . The second line contains an array   A[]   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
"""
if __name__ == '__main__':
    n=int(input())
    set_scores=set(map(int,input().split()))
    maximum_score=max(set_scores)
    set_scores.discard(maximum_score)
    print(max(set_scores))
    