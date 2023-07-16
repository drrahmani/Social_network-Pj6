#Muhammad Rahmani
#SocialNetwork Pj6
#Session 8
import random
import matplotlib.pyplot as plt

num_nodes = 10000
out_degree = 10

support_you = [0, 2, 4, 6]
support_rival = [1, 3, 5, 7]
undecided = [8, 9]

graph1 = {i: [] for i in range(num_nodes)}
graph2 = {i: [] for i in range(num_nodes)}
for i in range(num_nodes):
    friends = random.sample(range(num_nodes), out_degree)  # Randomly select out_degree friends for each node
    graph1[i] = friends
    graph2[i] = friends

voter_preferences1 = {}
voter_preferences2 = {}
for node_id in range(num_nodes):
    last_digit = node_id % 10
    if last_digit in support_you:
        voter_preferences1[node_id] = 'You'
        voter_preferences2[node_id] = 'You'
    elif last_digit in support_rival:
        voter_preferences1[node_id] = 'Rival'
        voter_preferences2[node_id] = 'Rival'
    else:
        voter_preferences1[node_id] = 'Undecided'
        voter_preferences2[node_id] = 'Undecided'

support_you_count1 = sum(1 for pref in voter_preferences1.values() if pref == 'You')
support_rival_count1 = sum(1 for pref in voter_preferences1.values() if pref == 'Rival')

support_you_count2 = sum(1 for pref in voter_preferences2.values() if pref == 'You')
support_rival_count2 = sum(1 for pref in voter_preferences2.values() if pref == 'Rival')

undecided_count = num_nodes - support_you_count1 - support_rival_count1

print("Initial support (Graph 1):")
print("You:", support_you_count1)
print("Rival:", support_rival_count1)
print("Undecided:", undecided_count)

undecided_count = num_nodes - support_you_count2 - support_rival_count2

print("\nInitial support (Graph 2):")
print("You:", support_you_count2)
print("Rival:", support_rival_count2)
print("Undecided:", undecided_count)

spending_values = []
votes_diff_graph1 = []

for k in range(1000, 10000, 1000):
    voters_to_persuade = min(k // 100, 10)

    persuaded_voters = set(range(3000, 3000 + voters_to_persuade * 10))
    for voter_id in persuaded_voters:
        voter_preferences1[voter_id] = 'You'

    for iteration in range(10):
        updates = {}
        for node_id in range(num_nodes):
            if voter_preferences1[node_id] == 'Undecided':
                support_you_friends = 0
                support_rival_friends = 0


                for friend_id in graph1[node_id]:
                    friend_preference = voter_preferences1[friend_id]
                    if friend_preference == 'You':
                        support_you_friends += 1
                    elif friend_preference == 'Rival':
                        support_rival_friends += 1


                if support_you_friends > support_rival_friends:
                    updates[node_id] = 'You'
                elif support_rival_friends > support_you_friends:
                    updates[node_id] = 'Rival'
                else:
                    if iteration % 2 == 0:
                        updates[node_id] = 'You'
                    else:
                        updates[node_id] = 'Rival'

        for node_id, preference in updates.items():
            voter_preferences1[node_id] = preference

    support_you_count1 = sum(1 for pref in voter_preferences1.values() if pref == 'You')
    support_rival_count1 = sum(1 for pref in voter_preferences1.values() if pref == 'Rival')

    votes_you = support_you_count1 + len(persuaded_voters)
    votes_rival = support_rival_count1

    spending_values.append(k)
    votes_diff_graph1.append(votes_you - votes_rival)

votes_diff_graph2 = []

for k in range(1000, 10000, 1000):
    high_rollers = sorted(graph2.keys(), key=lambda x: len(graph2[x]), reverse=True)
    high_rollers_to_invite = min(k // 1000, 10)  # Calculate the number of high rollers to invite based on available funding

    persuaded_voters = set(high_rollers[:high_rollers_to_invite])
    for voter_id in persuaded_voters:
        voter_preferences2[voter_id] = 'You'

    for iteration in range(10):
        updates = {}
        for node_id in range(num_nodes):
            if voter_preferences2[node_id] == 'Undecided':
                support_you_friends = 0
                support_rival_friends = 0

                for friend_id in graph2[node_id]:
                    friend_preference = voter_preferences2[friend_id]
                    if friend_preference == 'You':
                        support_you_friends += 1
                    elif friend_preference == 'Rival':
                        support_rival_friends += 1

                if support_you_friends > support_rival_friends:
                    updates[node_id] = 'You'
                elif support_rival_friends > support_you_friends:
                    updates[node_id] = 'Rival'
                else:
                    if iteration % 2 == 0:
                        updates[node_id] = 'You'
                    else:
                        updates[node_id] = 'Rival'

        for node_id, preference in updates.items():
            voter_preferences2[node_id] = preference

    support_you_count2 = sum(1 for pref in voter_preferences2.values() if pref == 'You')
    support_rival_count2 = sum(1 for pref in voter_preferences2.values() if pref == 'Rival')

    votes_you = support_you_count2 + len(persuaded_voters)
    votes_rival = support_rival_count2

    votes_diff_graph2.append(votes_you - votes_rival)

plt.plot(spending_values, votes_diff_graph1, label="Graph a")
plt.plot(spending_values, votes_diff_graph2, label="Graph b")
plt.xlabel("Amount Spent (Rs. k)")
plt.ylabel("Votes Difference (You - Rival)")
plt.title("Effect of Spending on Election Results")
plt.legend()
plt.show()

min_spending_graph1 = spending_values[votes_diff_graph1.index(max(votes_diff_graph1))]
min_spending_graph2 = spending_values[votes_diff_graph2.index(max(votes_diff_graph2))]

print("Minimum amount required to win the election (Graph 1): Rs.", min_spending_graph1)
print("Minimum amount required to win the election (Graph 2): Rs.", min_spending_graph2)
