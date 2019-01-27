#Monty Hall Problem
**Monty Hall Problem** has been one of the most well-known seemingly paradoxical problem in probability.

You can read more about this problem in this [Wikipedia Page](https://en.wikipedia.org/wiki/Monty_Hall_problem).

## What are the codes here?
The programs are written in **Python 3.7.2**.

`simulate-v1.py` is the code that shows you how one simulation of the Monty Hall Problem is run. The doors are assigned randomly 2 goats and 1 car. The player randomly picks a door in the beginning. The host opens and reveals one door with a goat behind it. Then, the player randomly decides whether to change to another door. Finally, the result is then revealed.

`simulate-v2.py` is the code that makes use of the codes in `simulate-v1.py` (with the print statements removed) and run many simulations to gather overall results. The default number of simulations is 1,000,000 and it will print out the winning rate of each strategy (whether to change or not to change the player's choice after the host opening a door with a goat behind it).

## How to use this?
With **Python 3** installed, you can simply run the code by doing `python simulate-v1.py` or `python simulate-v2.py` in your terminal and see the results.

## One of the sample result
This is one of the sample result I have got from running `simulate-v2.py`.

```
1000000 simulations have been run.
The player took 500223 times changing the choice, 499777 times not changing.
Win rate for changing choice after reveal: 66.67%.
Win rate for not changing choice after reveal: 33.37%.
```

Not surprising at all, it is true that you have a greater chance of winning if you actually choose to change the door of your choice after the host open and reveal one of the door with a goat.

## Why you make this?
Isn't it great to actually see the results with computer simulations?