def panagram(sentence) :
    for i in "abcdefghijklmnopqrstuvwxyz" :
        if i not in sentence :
            # print "Not a panagram"
            return False
    # print "Is a panagram"
    return True

# panagram("the quick brown fox jumps over the lazy dog")
