class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #n+1 dikarenakan n dimulai dari 1 bukan dari 0
        #tc adalah trust count yaitu tempat perhitungan trust
        tc = [0] * (n+1)
        #jika n adalah 2 maka tc adalah [0, 0, 0]
        #jika trust adalah [[1,2]]
        for x in trust:
            tc[x[0]] -=1
        #maka tc pada index 1 akan di berikan -1 sehingga tc menjadi [0, -1, 0]. index 1 didapat dari x[0]
            tc[x[1]] +=1
        #disini tc dengan index 2 akan di tambahkan menjadi 1 sehingga tc [0, -1, 1]. index 2 didapat dari x[1]
        #range dimulai dari 1 dikarenakan tc dimulai dari index 1
        for i in range (1,n+1):
        #n-1 dikarenakan jika ada judge, judge pasti adalah orang yang tidak percaya orang lain sehingga seharusnya judge adalah orang yang tidak punya koneksi
            if tc[i] == n-1:
                return i
        #jika dari semua n mempunyai koneksi maka -1                
        return -1
