#Muhammad Rahmani
#SocialNetwork Pj6
#Session 8
import networkx as nx
import random

G1 = nx.gnm_random_graph(10000, 100000, seed=10)

G2 = nx.barabasi_albert_graph(10000, 10, seed=10)

for node in G1.nodes:
    last_digit = node % 10
    if last_digit in [0, 2, 4, 6]:
        G1.nodes[node]['support'] = 'you'
    elif last_digit in [1, 3, 5, 7]:
        G1.nodes[node]['support'] = 'rival'
    else:
        G1.nodes[node]['support'] = 'undecided'

for node in G2.nodes:
    last_digit = node % 10
    if last_digit in [0, 2, 4, 6]:
        G2.nodes[node]['support'] = 'you'
    elif last_digit in [1, 3, 5, 7]:
        G2.nodes[node]['support'] = 'rival'
    else:
        G2.nodes[node]['support'] = 'undecided'

for node in G1.nodes:
    if G1.nodes[node]['support'] == 'you':
        G1.nodes[node]['initial_support'] = 0.4
    elif G1.nodes[node]['support'] == 'rival':
        G1.nodes[node]['initial_support'] = 0.4
    else:
        G1.nodes[node]['initial_support'] = 0.2

for node in G2.nodes:
    if G2.nodes[node]['support'] == 'you':
        G2.nodes[node]['initial_support'] = 0.4
    elif G2.nodes[node]['support'] == 'rival':
        G2.nodes[node]['initial_support'] = 0.4
    else:
        G2.nodes[node]['initial_support'] = 0.2

for day in range(1, 11):
    for node in G1.nodes:
        if G1.nodes[node]['support'] == 'undecided':
            neighbor_support = [G1.nodes[neighbor]['initial_support'] for neighbor in G1.neighbors(node)]
            if neighbor_support.count(0.4) > neighbor_support.count(0.6):
                G1.nodes[node]['support'] = 'you'
            elif neighbor_support.count(0.4) < neighbor_support.count(0.6):
                G1.nodes[node]['support'] = 'rival'
            else:
                G1.nodes[node]['support'] = random.choice(['you', 'rival'])

    for node in G2.nodes:
        if G2.nodes[node]['support'] == 'undecided':
            neighbor_support = [G2.nodes[neighbor]['initial_support'] for neighbor in G2.neighbors(node)]
            if neighbor_support.count(0.4) > neighbor_support.count(0.6):
                G2.nodes[node]['support'] = 'you'
            elif neighbor_support.count(0.4) < neighbor_support.count(0.6):
                G2.nodes[node]['support'] = 'rival'
            else:
                G2.nodes[node]['support'] = random.choice(['you', 'rival'])

    # Print the support of each candidate on this day
    you_support1 = sum([G1.nodes[node]['initial_support'] for node in G1.nodes if G1.nodes[node]['support'] == 'you'])
    rival_support1 = sum([G1.nodes[node]['initial_support'] for node in G1.nodes if G1.nodes[node]['support'] == 'rival'])
    you_support2 = sum([G2.nodes[node]['initial_support'] for node in G2.nodes if G2.nodes[node]['support'] == 'you'])
    rival_support2 = sum([G2.nodes[node]['initial_support'] for node in G2.nodes if G2.nodes[node]['support'] == 'rival'])
    print(f"Day {day}: You - {you_support1 + you_support2:.2%}, Rival - {rival_support1 + rival_support2:.2%}")

you_votes1 = sum([1 for node in G1.nodes if G1.nodes[node]['support'] == 'you'])
rival_votes1: int = sum([1for node in G1.nodes if G1.nodes[node]['support'] == 'rival'])
you_votes2 = sum([1 for node in G2.nodes if G2.nodes[node]['support'] == 'you'])
rival_votes2 = sum([1 for node in G2.nodes if G2.nodes[node]['support'] == 'rival'])

if you_votes1 + you_votes2 > rival_votes1 + rival_votes2:
    print("You win!")
elif you_votes1 + you_votes2 < rival_votes1 + rival_votes2:
    print("Rival wins!")
else:
    print("It's a tie!")