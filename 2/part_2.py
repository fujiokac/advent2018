def read_file():
    try:
        with open('input.txt','r') as file:
            return file.read().splitlines()
    finally:
        file.close()

def find_matching_id():
    ids = read_file()
    trie = {}
    for boxId in ids:
        match = match_id(boxId, trie, False)
        if match is not None:
            return match

def match_id(id, trie, different):
    '''
        Parse IDs adding letters to trie
        Branches into alternate matching on first difference
        Otherwise returns None
    '''
    if len(id) == 0:
        return None if different else ""
    letter = id[0]
    if letter not in trie:
        # boxId is different from previous on this letter
        if different is None:
            # Matching search, no difference tolerated
            return None
        if not different:
            # No previous differences
            # Searching through other letters for a match with 0 tolerance
            for other_letter in trie:
                match = match_id(id[1:], trie[other_letter], None)
                if match is not None:
                    return match
            different = True
        # Match not found, continuing to build data
        trie[letter] = {}
    # Continue matching/building data recursively
    match = match_id(id[1:], trie[letter], different)
    return None if match is None else letter + match


print(find_matching_id())