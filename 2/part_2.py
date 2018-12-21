def readFile():
    try:
        with open('input.txt','r') as file:
            return file.read().splitlines()
    finally:
        file.close()

def findCommonId():
    ids = readFile()
    trie = {}
    for boxId in ids:
        match = matchId(boxId, trie, False)
        if match is not None:
            return match

def matchId(boxId, trie, different):
    '''
        Parse IDs adding letters to trie
        Branches into alternate matching on first difference
        Otherwise returns None
    '''
    if len(boxId) == 0:
        return None if different else ""
    letter = boxId[0]
    if letter not in trie:
        # boxId is different from previous on this letter
        if different is None:
            # Matching search, no difference tolerated
            return None
        if not different:
            # No previous differences
            # Searching through other letters for a match with 0 tolerance
            for otherLetter in trie:
                match = matchId(boxId[1:], trie[otherLetter], None)
                if match is not None:
                    return match
            different = True
        # Match not found, continuing to build data
        trie[letter] = {}
    # Continue matching/building data recursively
    match = matchId(boxId[1:], trie[letter], different)
    return None if match is None else letter + match


print(findCommonId())