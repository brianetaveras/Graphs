
def earliest_ancestor(ancestors, starting_node):
    ancestors_hash = {}
    
    for v, k in ancestors:
        if k in ancestors_hash:
            ancestors_hash[k].add(v)
        else:
            ancestors_hash[k] = set([v])

    if starting_node not in ancestors_hash:
        return -1

    stack = [starting_node]
    visited_nodes = set()
    earliest_ancestor = None

    while stack:
        current_node = stack.pop()

        if current_node not in visited_nodes:
            visited_nodes.add(current_node)

            if current_node in ancestors_hash:
                for ancestor in ancestors_hash[current_node]:
                    if ancestor not in ancestors_hash:
                        earliest_ancestor = ancestor
                    stack.append(ancestor)

    return earliest_ancestor


