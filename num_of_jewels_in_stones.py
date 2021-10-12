class Sol:
    def num_of_jewels_in_stones(self,J,S):
        return sum(1 for s in S if s in set(J))

if __name__ == '__main__':
    p=Sol()
    print(p.num_of_jewels_in_stones(J='aA', S='aAAbbb'))
