#Problem 4

yours=['Yale', 'MIT', 'Berkeley']
mine=['Harvard', 'Caltech', 'Stanford']

ours1=mine + yours

ours2=[]
ours2.append(mine)
ours2.append(yours)

#Part 1
print(ours1)
print(ours2)
textans_1 = 'Using the plus operator iteratively concatenates the elements of ' \
            'mine and yours,resulting in a new list, ours1, that has six ' \
            'elements. The append method treats the list mine as one element ' \
            'and the list yours as another element and combine them into a ' \
            'list consisting of two elements (both of which are lists).'
print(textans_1)

#Part 2
yours[1] = 'UChicago'
print(ours1)
print(ours2)
textans_2 = 'With list concatenation, a new list is being created and then being ' \
            'attached to a new variable, ours1, such that changes in a former list ' \
            'do not get reflected in the new list. In the second method using append ' \
            ', there is one list that is being modified (as opposed to new list being created) '
print(textans_2)
