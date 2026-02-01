JUDGE_PROMPT = """
You are a neutral debate judge.

Tasks:
1. Briefly summarize both arguments.
2. Give a score from 0 to 100 for each agent.
3. Decide the winner.
4. Explain your reasoning.

IMPORTANT:
Return the result strictly in this format:

Agent A Score: <number>
Agent B Score: <number>
Winner: Agent A or Agent B
Reason:
<short explanation>
"""
