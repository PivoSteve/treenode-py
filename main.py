import os
from libraries.json import massive
from libraries.treenode import TreeNode

def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)

    for i, c1 in enumerate(s1):
        current_row = [i + 1]

        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))

        previous_row = current_row

    return previous_row[-1]

def closest_word(target_word, word_list, used_words):
    closest = None
    min_distance = float('inf')

    for word in word_list:
        if len(word) == len(target_word) and word not in used_words:
            distance = levenshtein_distance(target_word, word)
            if distance < min_distance:
                closest = word
                min_distance = distance
            elif distance == min_distance and closest is not None:
                closest = max(closest, word)

    if closest is not None:
        used_words.add(closest)
    return closest if min_distance <= (len(target_word) - 1) else "Слово не найдено!"

words = massive().load_words_from_json()
branches_iterations = 1
iterations = 151
target_word = input("Введите слово на русском языке: ")

def generate_branch(iterations, target_word, used_words):
    branch = []
    closest = None
    for i in range(iterations):
        if closest is None:
            closest = closest_word(target_word, words, used_words)
            branch.append("©")
        else:
            closest = closest_word(closest, words, used_words)
            branch.append(closest)
        target_word = closest
    return branch

def generate_tree_for_branches(branches_iterations, iterations, target_word):
    root = TreeNode(f"Оригинальное слово: {target_word}")
    used_words_set = set()
    used_words_for_branches = [set() for _ in range(branches_iterations)]
    for i in range(1, branches_iterations + 1):
        used_words = used_words_for_branches[i - 1]
        branch = generate_branch(iterations, target_word, used_words)
        branch_node = TreeNode(f"Ветка {i}:")
        unique_branch_words = set()
        for j, word in enumerate(branch):
            if word != "©":
                if word not in unique_branch_words and word not in used_words_set:
                    branch_node.add_child(TreeNode(f"[{j}] Ближайшее слово: {word}"))
                    unique_branch_words.add(word)
                    used_words_set.add(word)
            elif word == "Слово не найдено!":
                break
        root.add_child(branch_node)
    return root

tree = generate_tree_for_branches(branches_iterations, iterations, target_word)
print(tree)
