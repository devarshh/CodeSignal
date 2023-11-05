def solution(votes, k):
    max_votes = max(votes)
    len_votes = len(votes)
    count = 0
    if k == 0 and votes.count(max_votes) == 1:
        return 1
    for i in votes:
        if (int(i) + k) > max_votes:
            count += 1
    return count