class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Hash_ran, Hash_mag = {}, {}
        for i in ransomNote:
            Hash_ran[i] = Hash_ran.get(i, 0) + 1
        
        for j in magazine:
            Hash_mag[j] = Hash_mag.get(j, 0) + 1
            
        for key in Hash_ran.keys():
            if Hash_mag.get(key, 0) < Hash_ran[key]:
                return False

        return True