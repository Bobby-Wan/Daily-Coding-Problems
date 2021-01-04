# This problem was asked by Google.
# The power set of a set is the set of all its subsets. 
# Write a function that, given a set, generates its 
# power set.
# For example, given the set {1, 2, 3}, it should 
# return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, 
# {1, 2, 3}}.
# You may also use a list or array to represent a set.

class static_holder:
    power_set = []
        
def recursive_power_set(elements, index):
    current_element = elements[index]
    subsets_to_add = []
    for subset in static_holder.power_set:
        new_subset = list(subset)
        new_subset.append(current_element)
        subsets_to_add.append(new_subset)
    static_holder.power_set.extend(subsets_to_add)

    if index > 0:
        recursive_power_set(elements, index-1)

def power_set(elements):
    static_holder.power_set.append([])
    if len(elements) == 0:
        return
    recursive_power_set(elements, len(elements)-1)
    return static_holder.power_set

if __name__ == "__main__":
    elements = [1,2,3,4]
    print(power_set(elements))
