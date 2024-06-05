partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])

all_attendees = partyA.union(partyB)

only_partyA = partyA.difference(partyB)
only_partyB = partyB.difference(partyA)

unique_attendees = only_partyA.union(only_partyB)

print("파티 A, B에 참석한 사람들:", ", ".join(sorted(all_attendees)))
print("파티 A, B에 중복 없이 참석한 사람: ", ", ".join(unique_attendees))
print("파티 A에만 참석한 사람: " + ", ".join(only_partyA))
